"""
Data loading functions for CIHI Mental Health Dashboard
"""

import pandas as pd
import json
import os
import traceback
from utils.config import DATA_FILES, FISCAL_YEARS, FISCAL_YEARS_DISPLAY

def load_table3_data():
    """Load and process Table 3 data for provincial trends"""
    print("🔄 Attempting to load Table 3 data...")
    
    try:
        # Check if file exists
        file_path = DATA_FILES['table3']
        if not os.path.exists(file_path):
            print(f"❌ ERROR: File not found: {file_path}")
            print(f"📁 Current working directory: {os.getcwd()}")
            print(f"📁 Files in current directory: {os.listdir('.')}")
            if os.path.exists('data'):
                print(f"📁 Files in data directory: {os.listdir('data')}")
            else:
                print("📁 Data directory does not exist!")
            return pd.DataFrame()
        
        print(f"✅ File found: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"✅ JSON loaded successfully")
        print(f"📊 Data keys: {list(data.keys())}")
        
        # Extract data and create DataFrame
        records = []
        
        print(f"📅 Processing years: {FISCAL_YEARS}")
        
        for i, province_data in enumerate(data['data']):
            province = province_data['province']
            print(f"🔄 Processing province {i+1}: {province}")
            
            for year, year_display in zip(FISCAL_YEARS, FISCAL_YEARS_DISPLAY):
                if year in province_data:
                    records.append({
                        'Province': province,
                        'Year': year_display,
                        'N': province_data[year]['N'],
                        'Rate': province_data[year]['Rate']
                    })
        
        df = pd.DataFrame(records)
        print(f"✅ DataFrame created successfully")
        print(f"📊 Shape: {df.shape}")
        print(f"📊 Columns: {list(df.columns)}")
        print(f"📊 Sample data:")
        print(df.head())
        
        return df
    
    except Exception as e:
        print(f"❌ ERROR loading Table 3 data: {str(e)}")
        print(f"🔍 Full error traceback:")
        traceback.print_exc()
        return pd.DataFrame()

def load_table4_data():
    """Load and process Table 4 data for other conditions"""
    print("🔄 Attempting to load Table 4 data...")
    
    try:
        # Check if file exists
        file_path = DATA_FILES['table4']
        if not os.path.exists(file_path):
            print(f"❌ ERROR: File not found: {file_path}")
            return pd.DataFrame()
        
        print(f"✅ File found: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"✅ JSON loaded successfully")
        
        # Extract data and create DataFrame
        records = []
        
        for i, province_data in enumerate(data['data']):
            province = province_data['province']
            print(f"🔄 Processing province {i+1}: {province}")
            
            for year, year_display in zip(FISCAL_YEARS, FISCAL_YEARS_DISPLAY):
                if year in province_data:
                    records.append({
                        'Province': province,
                        'Year': year_display,
                        'N': province_data[year]['N'],
                        'Rate': province_data[year]['Rate']
                    })
        
        df = pd.DataFrame(records)
        print(f"✅ Table 4 DataFrame created successfully")
        print(f"📊 Shape: {df.shape}")
        
        return df
    
    except Exception as e:
        print(f"❌ ERROR loading Table 4 data: {str(e)}")
        print(f"🔍 Full error traceback:")
        traceback.print_exc()
        return pd.DataFrame()

def combine_mental_health_other_data(table3_df, table4_df):
    """Combine mental health and other conditions data for comparison"""
    try:
        if table3_df.empty or table4_df.empty:
            print("❌ One or both dataframes are empty")
            return pd.DataFrame()
        
        # Merge the dataframes
        mental_health = table3_df.copy()
        mental_health['Condition_Type'] = 'Mental Health'
        mental_health = mental_health.rename(columns={'N': 'MH_N', 'Rate': 'MH_Rate'})
        
        other_conditions = table4_df.copy()
        other_conditions['Condition_Type'] = 'Other Conditions'
        other_conditions = other_conditions.rename(columns={'N': 'Other_N', 'Rate': 'Other_Rate'})
        
        # Merge on Province and Year
        combined = pd.merge(
            mental_health[['Province', 'Year', 'MH_N', 'MH_Rate']], 
            other_conditions[['Province', 'Year', 'Other_N', 'Other_Rate']], 
            on=['Province', 'Year'], 
            how='inner'
        )
        
        # Calculate totals and percentages
        combined['Total_N'] = combined['MH_N'] + combined['Other_N']
        combined['Total_Rate'] = combined['MH_Rate'] + combined['Other_Rate']
        combined['MH_Percentage'] = (combined['MH_N'] / combined['Total_N'] * 100).round(1)
        
        print(f"✅ Combined data created successfully")
        print(f"📊 Combined shape: {combined.shape}")
        
        return combined
    
    except Exception as e:
        print(f"❌ ERROR combining data: {str(e)}")
        traceback.print_exc()
        return pd.DataFrame()

def get_province_options(df):
    """Get province options for dropdown"""
    if df.empty:
        return [{'label': 'No data available', 'value': 'none'}]
    
    provinces = sorted(df['Province'].unique())
    return [{'label': province, 'value': province} for province in provinces]

def get_default_provinces(df):
    """Get default province selection"""
    if df.empty:
        return ['none']
    
    # Default to only Alberta
    available_provinces = df['Province'].unique()
    
    if 'Alberta' in available_provinces:
        return ['Alberta']
    else:
        # If Alberta not available, use first province
        return [list(available_provinces)[0]]