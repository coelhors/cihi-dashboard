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

def load_table10_data():
    """Load and process Table 10 data for age and gender analysis"""
    print("🔄 Attempting to load Table 10 data...")
    
    try:
        # Check if file exists
        file_path = DATA_FILES['table10']
        if not os.path.exists(file_path):
            print(f"❌ ERROR: File not found: {file_path}")
            return pd.DataFrame()
        
        print(f"✅ File found: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"✅ JSON loaded successfully")
        
        # Extract data and create DataFrame
        records = []
        
        for entry in data['data']:
            age_group = entry['age_group']
            sex = entry['sex']
            
            # Skip total age group for now (we'll focus on specific age groups)
            if 'Total age' in age_group:
                continue
                
            # Clean age group names
            age_clean = age_group.replace('Age ', '').replace(' years', '')
            
            for year, year_display in zip(FISCAL_YEARS, FISCAL_YEARS_DISPLAY):
                if year in entry:
                    year_data = entry[year]
                    records.append({
                        'Age_Group': age_clean,
                        'Sex': sex,
                        'Year': year_display,
                        'Rate': year_data['Rate'],
                        'CI_Lower': year_data['CI_lower'],
                        'CI_Upper': year_data['CI_upper']
                    })
        
        df = pd.DataFrame(records)
        print(f"✅ Table 10 DataFrame created successfully")
        print(f"📊 Shape: {df.shape}")
        print(f"📊 Age groups: {sorted(df['Age_Group'].unique())}")
        print(f"📊 Sex categories: {sorted(df['Sex'].unique())}")
        
        return df
    
    except Exception as e:
        print(f"❌ ERROR loading Table 10 data: {str(e)}")
        print(f"🔍 Full error traceback:")
        traceback.print_exc()
        return pd.DataFrame()

def load_table11_data():
    """Load and process Table 11 data for urban vs rural analysis"""
    print("🔄 Attempting to load Table 11 data...")
    
    try:
        # Check if file exists
        file_path = DATA_FILES['table11']
        if not os.path.exists(file_path):
            print(f"❌ ERROR: File not found: {file_path}")
            return pd.DataFrame()
        
        print(f"✅ File found: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"✅ JSON loaded successfully")
        
        # Extract data and create DataFrame
        records = []
        
        for entry in data['data']:
            residence_type = entry['residence_type']
            
            for year, year_display in zip(FISCAL_YEARS, FISCAL_YEARS_DISPLAY):
                if year in entry:
                    year_data = entry[year]
                    records.append({
                        'Residence_Type': residence_type,
                        'Year': year_display,
                        'Rate': year_data['Rate'],
                        'CI_Lower': year_data['CI_lower'],
                        'CI_Upper': year_data['CI_upper']
                    })
        
        df = pd.DataFrame(records)
        print(f"✅ Table 11 DataFrame created successfully")
        print(f"📊 Shape: {df.shape}")
        print(f"📊 Residence types: {sorted(df['Residence_Type'].unique())}")
        
        return df
    
    except Exception as e:
        print(f"❌ ERROR loading Table 11 data: {str(e)}")
        print(f"🔍 Full error traceback:")
        traceback.print_exc()
        return pd.DataFrame()

def load_table12_data():
    """Load and process Table 12 data for income quintile analysis"""
    print("🔄 Attempting to load Table 12 data...")
    
    try:
        # Check if file exists
        file_path = DATA_FILES['table12']
        if not os.path.exists(file_path):
            print(f"❌ ERROR: File not found: {file_path}")
            return pd.DataFrame()
        
        print(f"✅ File found: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"✅ JSON loaded successfully")
        
        # Extract data and create DataFrame
        records = []
        
        for entry in data['data']:
            income_quintile = f"Q{entry['income_quintile']}"
            
            for year, year_display in zip(FISCAL_YEARS, FISCAL_YEARS_DISPLAY):
                if year in entry:
                    year_data = entry[year]
                    records.append({
                        'Income_Quintile': income_quintile,
                        'Year': year_display,
                        'Rate': year_data['Rate'],
                        'CI_Lower': year_data['CI_lower'],
                        'CI_Upper': year_data['CI_upper']
                    })
        
        df = pd.DataFrame(records)
        print(f"✅ Table 12 DataFrame created successfully")
        print(f"📊 Shape: {df.shape}")
        print(f"📊 Income quintiles: {sorted(df['Income_Quintile'].unique())}")
        
        return df
    
    except Exception as e:
        print(f"❌ ERROR loading Table 12 data: {str(e)}")
        print(f"🔍 Full error traceback:")
        traceback.print_exc()
        return pd.DataFrame()

def load_table13_data():
    """Load and process Table 13 data for clinical diagnostic patterns"""
    print("🔄 Attempting to load Table 13 data...")
    
    try:
        # Load data from multiple years (we have 2021-22, 2022-23, 2023-24)
        years_data = {}
        year_files = {
            '2021-22': 'data/table_13-2021-2022.json',
            '2022-23': 'data/table_13-2022-2023.json', 
            '2023-24': 'data/table_13-2023-2024.json'
        }
        
        all_records = []
        
        for year_display, file_path in year_files.items():
            if not os.path.exists(file_path):
                print(f"⚠️ WARNING: File not found: {file_path}")
                continue
                
            print(f"✅ Loading {file_path}")
            
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Extract data and create records
            for entry in data['data']:
                diagnosis = entry['diagnosis']
                sex = entry['sex']
                
                # Process each age group
                age_groups = ['age_5_9', 'age_10_14', 'age_15_17', 'age_18_24', 'age_5_24']
                age_labels = ['5-9', '10-14', '15-17', '18-24', '5-24']
                
                for age_key, age_label in zip(age_groups, age_labels):
                    if age_key in entry:
                        age_data = entry[age_key]
                        all_records.append({
                            'Year': year_display,
                            'Diagnosis': diagnosis,
                            'Sex': sex,
                            'Age_Group': age_label,
                            'Rate': age_data['Rate'],
                            'CI_Lower': age_data['CI_lower'],
                            'CI_Upper': age_data['CI_upper']
                        })
        
        df = pd.DataFrame(all_records)
        print(f"✅ Table 13 DataFrame created successfully")
        print(f"📊 Shape: {df.shape}")
        print(f"📊 Years: {sorted(df['Year'].unique())}")
        print(f"📊 Diagnoses: {sorted(df['Diagnosis'].unique())}")
        print(f"📊 Age groups: {sorted(df['Age_Group'].unique())}")
        print(f"📊 Sex categories: {sorted(df['Sex'].unique())}")
        
        return df
    
    except Exception as e:
        print(f"❌ ERROR loading Table 13 data: {str(e)}")
        print(f"🔍 Full error traceback:")
        traceback.print_exc()
        return pd.DataFrame()

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