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
    
    # Prefer Canada, Ontario, Alberta if available
    preferred = ['Canada', 'Ontario', 'Alberta']
    available_provinces = df['Province'].unique()
    
    defaults = []
    for prov in preferred:
        if prov in available_provinces:
            defaults.append(prov)
    
    # If none of the preferred are available, use first 3
    if not defaults:
        defaults = list(available_provinces)[:3]
    
    return defaults