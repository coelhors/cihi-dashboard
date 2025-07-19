"""
Health Equity page layout
"""

from dash import html
from utils.config import COLORS, STYLE_CARD
from utils.chart_helpers import create_placeholder_chart

def create_layout():
    """Create Health Equity page layout"""
    return html.Div([
        html.H2("⚖️ Health Equity", style={'color': COLORS['accent'], 'marginBottom': '30px'}),
        
        html.P("Examine disparities in mental health hospitalizations across geographic and socioeconomic dimensions.", 
               style={'fontSize': '18px', 'marginBottom': '30px'}),
        
        # Visual Element 5: Urban vs Rural
        html.Div([
            html.H3("Urban vs Rural Disparities"),
            html.P("Comparison of mental health hospitalization rates between urban and rural/remote areas."),
            html.Div(
                id='urban-rural-chart',
                children=create_placeholder_chart("Urban vs Rural Disparities")
            )
        ], style=STYLE_CARD),
        
        # Visual Element 6: Income Gradient
        html.Div([
            html.H3("Income Inequality Patterns"),
            html.P("Mental health hospitalization rates across income quintiles showing socioeconomic gradient."),
            html.Div(
                id='income-gradient-chart',
                children=create_placeholder_chart("Income Gradient Analysis")
            )
        ], style=STYLE_CARD),
        
        # Visual Element 7: Income Contributions
        html.Div([
            html.H3("Income Quintile Contributions"),
            html.P("How different income groups contribute to overall mental health hospitalization burden."),
            html.Div(
                id='income-pie-chart',
                children=create_placeholder_chart("Income Quintile Contribution Analysis")
            )
        ], style=STYLE_CARD)
    ])

def register_callbacks(app):
    """Register callbacks for Health Equity page (placeholder for now)"""
    pass