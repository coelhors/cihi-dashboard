"""
Enhanced sidebar navigation component for CIHI Mental Health Dashboard
"""

from dash import dcc, html
from utils.config import COLORS

def create_sidebar():
    """Create modern, aesthetically pleasing sidebar navigation component with better contrast"""
    return html.Div([
        # Navigation menu - starting right away
        html.Nav([
            # Provincial Overview
            dcc.Link([
                html.Div([
                    html.I(className="fas fa-chart-line", style={
                        'fontSize': '18px',
                        'marginRight': '15px',
                        'width': '24px',
                        'textAlign': 'center',
                        'color': 'inherit'
                    }),
                    html.Span("Provincial Overview", style={
                        'fontSize': '15px', 
                        'fontWeight': '600',
                        'color': 'inherit'
                    })
                ], style={
                    'display': 'flex',
                    'alignItems': 'center',
                    'padding': '16px 24px',
                    'borderRadius': '12px',
                    'transition': 'all 0.3s ease',
                    'margin': '0 16px 8px 16px',
                    'backgroundColor': 'transparent',
                    'border': '2px solid transparent',
                    'color': 'white'
                }, className='nav-item')
            ], href='/', id='nav-provincial', style={'textDecoration': 'none'}),
            
            # Demographics
            dcc.Link([
                html.Div([
                    html.I(className="fas fa-users", style={
                        'fontSize': '18px',
                        'marginRight': '15px',
                        'width': '24px',
                        'textAlign': 'center',
                        'color': 'inherit'
                    }),
                    html.Span("Demographics", style={
                        'fontSize': '15px', 
                        'fontWeight': '600',
                        'color': 'inherit'
                    })
                ], style={
                    'display': 'flex',
                    'alignItems': 'center',
                    'padding': '16px 24px',
                    'borderRadius': '12px',
                    'transition': 'all 0.3s ease',
                    'margin': '0 16px 8px 16px',
                    'backgroundColor': 'transparent',
                    'border': '2px solid transparent',
                    'color': 'white'
                }, className='nav-item')
            ], href='/demographics', id='nav-demographics', style={'textDecoration': 'none'}),
            
            # Health Equity
            dcc.Link([
                html.Div([
                    html.I(className="fas fa-balance-scale", style={
                        'fontSize': '18px',
                        'marginRight': '15px',
                        'width': '24px',
                        'textAlign': 'center',
                        'color': 'inherit'
                    }),
                    html.Span("Health Equity", style={
                        'fontSize': '15px', 
                        'fontWeight': '600',
                        'color': 'inherit'
                    })
                ], style={
                    'display': 'flex',
                    'alignItems': 'center',
                    'padding': '16px 24px',
                    'borderRadius': '12px',
                    'transition': 'all 0.3s ease',
                    'margin': '0 16px 8px 16px',
                    'backgroundColor': 'transparent',
                    'border': '2px solid transparent',
                    'color': 'white'
                }, className='nav-item')
            ], href='/equity', id='nav-equity', style={'textDecoration': 'none'}),
            
            # Clinical Patterns
            dcc.Link([
                html.Div([
                    html.I(className="fas fa-th", style={
                        'fontSize': '18px',
                        'marginRight': '15px',
                        'width': '24px',
                        'textAlign': 'center',
                        'color': 'inherit'
                    }),
                    html.Span("Clinical Patterns", style={
                        'fontSize': '15px', 
                        'fontWeight': '600',
                        'color': 'inherit'
                    })
                ], style={
                    'display': 'flex',
                    'alignItems': 'center',
                    'padding': '16px 24px',
                    'borderRadius': '12px',
                    'transition': 'all 0.3s ease',
                    'margin': '0 16px 8px 16px',
                    'backgroundColor': 'transparent',
                    'border': '2px solid transparent',
                    'color': 'white'
                }, className='nav-item')
            ], href='/clinical', id='nav-clinical', style={'textDecoration': 'none'})
            
        ], style={
            'display': 'flex',
            'flexDirection': 'column',
            'gap': '0px',
            'paddingTop': '30px'
        })
        
    ], style={
        'position': 'fixed',
        'top': 0,
        'left': 0,
        'bottom': 0,
        'width': '280px',
        'background': f'linear-gradient(135deg, {COLORS["primary"]} 0%, #1a4d5c 50%, #0f2a33 100%)',
        'boxShadow': '4px 0 20px rgba(0, 0, 0, 0.15)',
        'zIndex': 1000,
        'fontFamily': '"Segoe UI", Tahoma, Geneva, Verdana, sans-serif'
    })