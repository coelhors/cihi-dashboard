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

# Styling configurations
STYLE_SIDEBAR = {
    'position': 'fixed',
    'top': 0,
    'left': 0,
    'bottom': 0,
    'width': '250px',
    'padding': '20px',
    'backgroundColor': COLORS['primary'],
    'color': 'white'
}

STYLE_CONTENT = {
    'marginLeft': '270px',
    'padding': '20px',
    'backgroundColor': COLORS['background'],
    'minHeight': '100vh'
}

STYLE_NAV_BUTTON = {
    'display': 'block',
    'width': '100%',
    'padding': '20px',
    'margin': '8px 0',
    'backgroundColor': 'transparent',
    'color': 'white',
    'border': '1px solid white',
    'borderRadius': '5px',
    'textDecoration': 'none',
    'textAlign': 'center',
    'fontSize': '18px',
    'cursor': 'pointer'
}

STYLE_CARD = {
    'backgroundColor': 'white',
    'border': '1px solid #dee2e6',
    'borderRadius': '8px',
    'padding': '20px',
    'margin': '20px 0',
    'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'
}

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