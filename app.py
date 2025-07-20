"""
CIHI Mental Health Dashboard
Main application entry point - modular version with enhanced sidebar
"""

import dash
from dash import dcc, html, callback, Input, Output
import sys

# Import our modular components
from utils.config import STYLE_CONTENT, STYLE_NAV_BUTTON_BASE, STYLE_NAV_BUTTON_ACTIVE, COLORS
from utils.data_loader import load_table3_data, load_table4_data, load_table10_data, load_table11_data, load_table12_data, load_table13_data, combine_mental_health_other_data
from components.sidebar import create_sidebar
# Import page modules directly to avoid circular imports
from components.pages.provincial_overview import create_layout as provincial_layout, register_callbacks as provincial_callbacks
from components.pages.demographics import create_layout as demographics_layout, register_callbacks as demographics_callbacks
from components.pages.health_equity import create_layout as health_equity_layout, register_callbacks as health_equity_callbacks
from components.pages.clinical_patterns import create_layout as clinical_patterns_layout, register_callbacks as clinical_patterns_callbacks

# Initialize the Dash app
app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "CIHI Mental Health Dashboard"

# Load data on startup
print("=" * 60)
print("🚀 STARTING CIHI MENTAL HEALTH DASHBOARD")
print("=" * 60)
print("Loading CIHI Mental Health Data...")

# Test basic functionality first
try:
    print("🔧 Testing basic imports...")
    import pandas as pd
    import plotly.express as px
    print("✅ All imports successful")
except Exception as e:
    print(f"❌ Import error: {e}")
    sys.exit(1)

# Load data
TABLE3_DF = load_table3_data()
TABLE4_DF = load_table4_data()
TABLE10_DF = load_table10_data()
TABLE11_DF = load_table11_data()
TABLE12_DF = load_table12_data()
TABLE13_DF = load_table13_data()

if not TABLE3_DF.empty:
    print(f"✅ Loaded Table 3: {len(TABLE3_DF)} records")
    print(f"✅ Provinces available: {sorted(TABLE3_DF['Province'].unique())}")
else:
    print("⚠️ WARNING: Table 3 data not loaded")

if not TABLE4_DF.empty:
    print(f"✅ Loaded Table 4: {len(TABLE4_DF)} records")
else:
    print("⚠️ WARNING: Table 4 data not loaded")

if not TABLE10_DF.empty:
    print(f"✅ Loaded Table 10: {len(TABLE10_DF)} records")
    print(f"✅ Age groups available: {sorted(TABLE10_DF['Age_Group'].unique())}")
else:
    print("⚠️ WARNING: Table 10 data not loaded")

if not TABLE11_DF.empty:
    print(f"✅ Loaded Table 11: {len(TABLE11_DF)} records")
    print(f"✅ Residence types available: {sorted(TABLE11_DF['Residence_Type'].unique())}")
else:
    print("⚠️ WARNING: Table 11 data not loaded")

if not TABLE12_DF.empty:
    print(f"✅ Loaded Table 12: {len(TABLE12_DF)} records")
    print(f"✅ Income quintiles available: {sorted(TABLE12_DF['Income_Quintile'].unique())}")
if not TABLE13_DF.empty:
    print(f"✅ Loaded Table 13: {len(TABLE13_DF)} records")
    print(f"✅ Diagnoses available: {sorted(TABLE13_DF['Diagnosis'].unique())}")
else:
    print("⚠️ WARNING: Table 13 data not loaded")

# Combine datasets for comparison
COMBINED_DF = combine_mental_health_other_data(TABLE3_DF, TABLE4_DF)
if not COMBINED_DF.empty:
    print(f"✅ Combined dataset created: {len(COMBINED_DF)} records")
else:
    print("⚠️ WARNING: Combined dataset not created")

print("=" * 60)

# Main app layout with enhanced sidebar
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    
    # Enhanced sidebar navigation
    create_sidebar(),
    
    # Main content area with updated margin
    html.Div(id='page-content', style=STYLE_CONTENT)
])

# Register callbacks for all pages
provincial_callbacks(app, TABLE3_DF, COMBINED_DF)
demographics_callbacks(app, TABLE10_DF)
health_equity_callbacks(app, TABLE11_DF, TABLE12_DF)
clinical_patterns_callbacks(app, TABLE13_DF)

# Main page routing callback
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    """Update page content based on URL path"""
    if pathname == '/demographics':
        return demographics_layout(TABLE10_DF)
    elif pathname == '/equity':
        return health_equity_layout(TABLE11_DF, TABLE12_DF)
    elif pathname == '/clinical':
        return clinical_patterns_layout(TABLE13_DF)
    else:  # Default to provincial overview
        return provincial_layout(TABLE3_DF, COMBINED_DF)

# Enhanced navigation highlighting callback
@app.callback(
    [Output('nav-provincial', 'children'),
     Output('nav-demographics', 'children'),
     Output('nav-equity', 'children'),
     Output('nav-clinical', 'children')],
    [Input('url', 'pathname')]
)
def update_nav_styles(pathname):
    """Update navigation button styles based on active page"""
    
    def create_nav_item(icon_class, text, is_active=False):
        """Helper function to create navigation item with proper styling"""
        style = STYLE_NAV_BUTTON_ACTIVE if is_active else STYLE_NAV_BUTTON_BASE
        
        return html.Div([
            html.I(className=icon_class, style={
                'fontSize': '16px',
                'marginRight': '12px',
                'width': '20px',
                'textAlign': 'center'
            }),
            html.Span(text, style={'fontSize': '14px', 'fontWeight': '500'})
        ], style=style)
    
    # Determine which page is active and style accordingly
    if pathname == '/demographics':
        return (
            create_nav_item("fas fa-chart-line", "Provincial Overview", False),
            create_nav_item("fas fa-users", "Demographics", True),
            create_nav_item("fas fa-balance-scale", "Health Equity", False),
            create_nav_item("fas fa-th", "Clinical Patterns", False)
        )
    elif pathname == '/equity':
        return (
            create_nav_item("fas fa-chart-line", "Provincial Overview", False),
            create_nav_item("fas fa-users", "Demographics", False),
            create_nav_item("fas fa-balance-scale", "Health Equity", True),
            create_nav_item("fas fa-th", "Clinical Patterns", False)
        )
    elif pathname == '/clinical':
        return (
            create_nav_item("fas fa-chart-line", "Provincial Overview", False),
            create_nav_item("fas fa-users", "Demographics", False),
            create_nav_item("fas fa-balance-scale", "Health Equity", False),
            create_nav_item("fas fa-th", "Clinical Patterns", True)
        )
    else:  # Provincial overview (default)
        return (
            create_nav_item("fas fa-chart-line", "Provincial Overview", True),
            create_nav_item("fas fa-users", "Demographics", False),
            create_nav_item("fas fa-balance-scale", "Health Equity", False),
            create_nav_item("fas fa-th", "Clinical Patterns", False)
        )

# Run the app
if __name__ == '__main__':
    print(f"\n🚀 Starting CIHI Mental Health Dashboard...")
    print(f"📊 Dashboard will be available at: http://localhost:8050")
    print(f"📄 Pages: Provincial Overview, Demographics, Health Equity, Clinical Patterns")
    print(f"🧩 Modular architecture: components, utils, pages")
    print(f"✨ Enhanced UI: Modern sidebar with professional styling")
    
    try:
        app.run(debug=True, dev_tools_hot_reload=False, dev_tools_ui=True)
    except Exception as e:
        print(f"\n❌ CRITICAL ERROR starting app: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)