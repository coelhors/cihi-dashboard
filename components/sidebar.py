"""
Sidebar navigation component for CIHI Mental Health Dashboard
"""

from dash import dcc, html
from utils.config import STYLE_SIDEBAR, STYLE_NAV_BUTTON

def create_sidebar():
    """Create sidebar navigation component"""
    return html.Div([
        html.H2("CIHI Mental Health Dashboard", 
                style={'color': 'white', 'textAlign': 'center', 'marginBottom': '30px', 'fontSize': '20px'}),
        
        html.Hr(style={'borderColor': 'white', 'margin': '20px 0'}),
        
        # Navigation buttons
        dcc.Link('📊 Provincial Overview', href='/', 
                style=STYLE_NAV_BUTTON, id='nav-provincial'),
        dcc.Link('👥 Demographics', href='/demographics', 
                style=STYLE_NAV_BUTTON, id='nav-demographics'),
        dcc.Link('⚖️ Health Equity', href='/equity', 
                style=STYLE_NAV_BUTTON, id='nav-equity'),
        dcc.Link('🏥 Clinical Patterns', href='/clinical', 
                style=STYLE_NAV_BUTTON, id='nav-clinical'),
        
        html.Hr(style={'borderColor': 'white', 'margin': '30px 0 20px 0'})
        
    ], style=STYLE_SIDEBAR)