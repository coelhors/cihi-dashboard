"""
Health Equity page layout and callbacks
"""

from dash import html, dcc, callback, Input, Output
import traceback
from utils.config import COLORS, STYLE_CARD
from utils.chart_helpers import create_placeholder_chart, create_urban_rural_disparity_chart, create_income_gradient_chart

def create_layout(table11_df=None, table12_df=None):
    """Create Health Equity page layout"""
    return html.Div([
        html.H2("⚖️ Health Equity", style={'color': COLORS['accent'], 'marginBottom': '30px'}),
        
        html.P("Examine disparities in mental health hospitalizations across geographic and socioeconomic dimensions.", 
               style={'fontSize': '18px', 'marginBottom': '30px'}),
        
        # Visual Element 5: Urban vs Rural
        html.Div([
            html.H3("Urban vs Rural Disparities"),
            html.P("Comparison of mental health hospitalization rates between urban and rural/remote areas."),
            
            dcc.Graph(
                figure=create_urban_rural_disparity_chart('Absolute Rates', False, True, False, table11_df) if table11_df is not None and not table11_df.empty else create_placeholder_chart("Urban vs Rural Disparities - Data not available")
            )
        ], style=STYLE_CARD),
        
        # Visual Element 6: Income Gradient Analysis
        html.Div([
            html.H3("Income Gradient Analysis"),
            html.P("Multi-line chart showing how mental health hospitalization rates vary across income quintiles."),
            
            dcc.Graph(
                id='income-gradient-chart',
                figure=create_income_gradient_chart(table12_df) if table12_df is not None and not table12_df.empty else create_placeholder_chart("Income Gradient Analysis - Data not available", height=600)
            )
        ], style=STYLE_CARD),
        
        # Visual Element 7: Income Contributions
        html.Div([
            html.H3("Income Quintile Contributions"),
            html.P("How different income groups contribute to overall mental health hospitalization burden."),
            dcc.Graph(
                figure=create_placeholder_chart("Income Quintile Contribution Analysis")
            )
        ], style=STYLE_CARD)
    ])

def register_callbacks(app, table11_df=None, table12_df=None):
    """Register callbacks for Health Equity page"""
    # No callbacks needed - all charts are now static
    pass