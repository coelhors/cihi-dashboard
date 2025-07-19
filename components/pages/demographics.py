"""
Demographics page layout
"""

from dash import html
from utils.config import COLORS, STYLE_CARD
from utils.chart_helpers import create_placeholder_chart

def create_layout():
    """Create Demographics page layout"""
    return html.Div([
        html.H2("👥 Demographics", style={'color': COLORS['secondary'], 'marginBottom': '30px'}),
        
        html.P("Analyze mental health hospitalization patterns by age groups and gender.", 
               style={'fontSize': '18px', 'marginBottom': '30px'}),
        
        # Visual Element 4: Age and Gender Patterns
        html.Div([
            html.H3("Age and Gender Patterns"),
            html.P("Interactive analysis showing how mental health hospitalizations vary by age and gender over time."),
            html.Div(
                id='demographics-chart',
                children=create_placeholder_chart("Age and Gender Analysis", height=500)
            )
        ], style=STYLE_CARD),
        
        # Key insights section
        html.Div([
            html.H4("Key Demographic Insights"),
            html.Ul([
                html.Li("Mental health hospitalizations increase dramatically with age"),
                html.Li("Gender differences become more pronounced in adolescence"),
                html.Li("COVID-19 impact varied significantly by demographic groups"),
                html.Li("Adolescent females show highest vulnerability rates")
            ])
        ], style=STYLE_CARD)
    ])

def register_callbacks(app):
    """Register callbacks for Demographics page (placeholder for now)"""
    pass