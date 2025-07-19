"""
Clinical Patterns page layout
"""

from dash import html
from utils.config import COLORS, STYLE_CARD
from utils.chart_helpers import create_placeholder_chart

def create_layout():
    """Create Clinical Patterns page layout"""
    return html.Div([
        html.H2("🏥 Clinical Patterns", style={'color': COLORS['success'], 'marginBottom': '30px'}),
        
        html.P("Understand diagnostic patterns and clinical service utilization across different mental health conditions.", 
               style={'fontSize': '18px', 'marginBottom': '30px'}),
        
        # Visual Element 8: Clinical Heat Map
        html.Div([
            html.H3("Clinical Diagnostic Patterns"),
            html.P("Interactive heat map showing how different mental health diagnoses affect various age groups and genders."),
            html.Div(
                id='clinical-heatmap',
                children=create_placeholder_chart("Clinical Diagnostic Heat Map", height=600)
            )
        ], style=STYLE_CARD),
        
        # Clinical insights section
        html.Div([
            html.H4("Clinical Pattern Insights"),
            html.Ul([
                html.Li("Eating disorders peak dramatically in adolescent females"),
                html.Li("Substance-related disorders more common in young adults"),
                html.Li("Mood disorders show consistent gender differences"),
                html.Li("Different conditions emerge at different developmental stages")
            ])
        ], style=STYLE_CARD)
    ])

def register_callbacks(app):
    """Register callbacks for Clinical Patterns page (placeholder for now)"""
    pass