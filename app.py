"""
CIHI Mental Health Dashboard
Main application entry point - modular version
"""

import dash
from dash import dcc, html, callback, Input, Output
import sys

# Import our modular components
from utils.config import STYLE_CONTENT, STYLE_NAV_BUTTON, COLORS
from utils.data_loader import load_table3_data
from components.sidebar import create_sidebar
from components.pages import provincial_overview, demographics, health_equity, clinical_patterns

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
if not TABLE3_DF.empty:
    print(f"✅ Loaded Table 3: {len(TABLE3_DF)} records")
    print(f"✅ Provinces available: {sorted(TABLE3_DF['Province'].unique())}")
else:
    print("⚠️ WARNING: Table 3 data not loaded - chart will show placeholder")
print("=" * 60)

# Main app layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    
    # Sidebar navigation
    create_sidebar(),
    
    # Main content area
    html.Div(id='page-content', style=STYLE_CONTENT)
])

# Register callbacks for all pages
provincial_overview.register_callbacks(app, TABLE3_DF)
demographics.register_callbacks(app)
health_equity.register_callbacks(app)
clinical_patterns.register_callbacks(app)

# Main page routing callback
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    """Update page content based on URL path"""
    if pathname == '/demographics':
        return demographics.create_layout()
    elif pathname == '/equity':
        return health_equity.create_layout()
    elif pathname == '/clinical':
        return clinical_patterns.create_layout()
    else:  # Default to provincial overview
        return provincial_overview.create_layout(TABLE3_DF)

# Navigation highlighting callback
@app.callback(
    [Output('nav-provincial', 'style'),
     Output('nav-demographics', 'style'),
     Output('nav-equity', 'style'),
     Output('nav-clinical', 'style')],
    [Input('url', 'pathname')]
)
def update_nav_styles(pathname):
    """Update navigation button styles based on active page"""
    base_style = STYLE_NAV_BUTTON.copy()
    active_style = STYLE_NAV_BUTTON.copy()
    active_style.update({
        'backgroundColor': 'white',
        'color': COLORS['primary'],
        'fontWeight': 'bold'
    })
    
    if pathname == '/demographics':
        return base_style, active_style, base_style, base_style
    elif pathname == '/equity':
        return base_style, base_style, active_style, base_style
    elif pathname == '/clinical':
        return base_style, base_style, base_style, active_style
    else:  # Provincial overview (default)
        return active_style, base_style, base_style, base_style

# Run the app
if __name__ == '__main__':
    print(f"\n🚀 Starting CIHI Mental Health Dashboard...")
    print(f"📊 Dashboard will be available at: http://localhost:8050")
    print(f"📄 Pages: Provincial Overview, Demographics, Health Equity, Clinical Patterns")
    print(f"🧩 Modular architecture: components, utils, pages")
    
    try:
        app.run(debug=True, dev_tools_hot_reload=False, dev_tools_ui=True)
    except Exception as e:
        print(f"\n❌ CRITICAL ERROR starting app: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)