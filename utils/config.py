"""
Configuration file for CIHI Mental Health Dashboard
Contains colors, styles, and constants
"""

# Color scheme
COLORS = {
    'primary': '#2E86AB',
    'secondary': '#A23B72', 
    'accent': '#F18F01',
    'success': '#C73E1D',
    'background': '#F8F9FA',
    'text': '#212529'
}

# Enhanced styling configurations
STYLE_CONTENT = {
    'marginLeft': '300px',  # Increased for wider sidebar
    'padding': '20px',
    'backgroundColor': COLORS['background'],
    'minHeight': '100vh'
}

STYLE_CARD = {
    'backgroundColor': 'white',
    'border': '1px solid #dee2e6',
    'borderRadius': '8px',
    'padding': '20px',
    'margin': '20px 0',
    'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'
}

# Enhanced navigation button styles with better contrast
STYLE_NAV_BUTTON_BASE = {
    'display': 'flex',
    'alignItems': 'center',
    'padding': '16px 24px',
    'borderRadius': '12px',
    'transition': 'all 0.3s ease',
    'margin': '0 16px 8px 16px',
    'backgroundColor': 'transparent',
    'border': '2px solid transparent',
    'color': 'white',
    'textDecoration': 'none',
    'fontSize': '15px',
    'fontWeight': '600'
}

STYLE_NAV_BUTTON_ACTIVE = {
    'display': 'flex',
    'alignItems': 'center',
    'padding': '16px 24px',
    'borderRadius': '12px',
    'transition': 'all 0.3s ease',
    'margin': '0 16px 8px 16px',
    'backgroundColor': 'white',
    'border': '2px solid #FFD700',
    'color': COLORS['primary'],
    'textDecoration': 'none',
    'fontSize': '15px',
    'fontWeight': '700',
    'boxShadow': '0 4px 12px rgba(0, 0, 0, 0.2)'
}

# Legacy style for backward compatibility
STYLE_NAV_BUTTON = STYLE_NAV_BUTTON_BASE

# Data configuration
DATA_FILES = {
    'table3': 'data/table_03.json',
    'table4': 'data/table_04.json',
    'table10': 'data/table_10.json',
    'table11': 'data/table_11.json',
    'table12': 'data/table_12.json',
    'table13': 'data/table_13.json'
}

# Years configuration
FISCAL_YEARS = ["2018-2019", "2019-2020", "2020-2021", "2021-2022", "2022-2023", "2023-2024"]
FISCAL_YEARS_DISPLAY = ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24"]