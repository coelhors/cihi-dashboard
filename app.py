"""
CIHI Mental Health Dashboard
Multi-page dashboard with navigation
"""

import dash
from dash import dcc, html, callback, Input, Output
import plotly.express as px
import plotly.graph_objects as go

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "CIHI Mental Health Dashboard"

# Color scheme
COLORS = {
    'primary': '#2E86AB',
    'secondary': '#A23B72', 
    'accent': '#F18F01',
    'success': '#C73E1D',
    'background': '#F8F9FA',
    'text': '#212529'
}

# Styling
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

def create_placeholder_chart(title, height=400):
    """Create a placeholder chart"""
    fig = go.Figure()
    fig.add_annotation(
        text=f"{title}<br><br>Visualization will be implemented here",
        xref="paper", yref="paper",
        x=0.5, y=0.5,
        xanchor='center', yanchor='middle',
        showarrow=False,
        font=dict(size=16, color=COLORS['primary'])
    )
    fig.update_layout(
        title=title,
        xaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
        yaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
        plot_bgcolor='white',
        paper_bgcolor='white',
        height=height
    )
    return fig

# Define page layouts
def provincial_overview_layout():
    """Page 1: Provincial Overview"""
    return html.Div([
        html.H2("📊 Provincial Overview", style={'color': COLORS['primary'], 'marginBottom': '30px'}),
        
        html.P("Explore mental health hospitalization trends across Canadian provinces and territories.", 
               style={'fontSize': '18px', 'marginBottom': '30px'}),
        
        # Visual Element 1: Provincial Trends
        html.Div([
            html.H3("Provincial Hospitalization Trends"),
            html.P("Interactive line chart showing hospitalization rates by province over time."),
            dcc.Graph(
                id='provincial-trends-chart',
                figure=create_placeholder_chart("Provincial Hospitalization Trends")
            )
        ], style=STYLE_CARD),
        
        # Visual Element 2: Mental Health vs Other Conditions
        html.Div([
            html.H3("Mental Health vs Other Conditions"),
            html.P("Comparison of mental health hospitalizations with other medical conditions."),
            dcc.Graph(
                id='comparison-chart',
                figure=create_placeholder_chart("Mental Health vs Other Conditions Comparison")
            )
        ], style=STYLE_CARD),
        
        # Visual Element 3: Provincial Contributions
        html.Div([
            html.H3("Provincial Contribution Analysis"),
            html.P("Each province's share of total mental health hospitalizations."),
            dcc.Graph(
                id='provincial-pie-chart',
                figure=create_placeholder_chart("Provincial Contribution Pie Chart")
            )
        ], style=STYLE_CARD)
    ])

def demographics_layout():
    """Page 2: Demographics"""
    return html.Div([
        html.H2("👥 Demographics", style={'color': COLORS['secondary'], 'marginBottom': '30px'}),
        
        html.P("Analyze mental health hospitalization patterns by age groups and gender.", 
               style={'fontSize': '18px', 'marginBottom': '30px'}),
        
        # Visual Element 4: Age and Gender Patterns
        html.Div([
            html.H3("Age and Gender Patterns"),
            html.P("Interactive analysis showing how mental health hospitalizations vary by age and gender over time."),
            dcc.Graph(
                id='demographics-chart',
                figure=create_placeholder_chart("Age and Gender Analysis", height=500)
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

def health_equity_layout():
    """Page 3: Health Equity"""
    return html.Div([
        html.H2("⚖️ Health Equity", style={'color': COLORS['accent'], 'marginBottom': '30px'}),
        
        html.P("Examine disparities in mental health hospitalizations across geographic and socioeconomic dimensions.", 
               style={'fontSize': '18px', 'marginBottom': '30px'}),
        
        # Visual Element 5: Urban vs Rural
        html.Div([
            html.H3("Urban vs Rural Disparities"),
            html.P("Comparison of mental health hospitalization rates between urban and rural/remote areas."),
            dcc.Graph(
                id='urban-rural-chart',
                figure=create_placeholder_chart("Urban vs Rural Disparities")
            )
        ], style=STYLE_CARD),
        
        # Visual Element 6: Income Gradient
        html.Div([
            html.H3("Income Inequality Patterns"),
            html.P("Mental health hospitalization rates across income quintiles showing socioeconomic gradient."),
            dcc.Graph(
                id='income-gradient-chart',
                figure=create_placeholder_chart("Income Gradient Analysis")
            )
        ], style=STYLE_CARD),
        
        # Visual Element 7: Income Contributions
        html.Div([
            html.H3("Income Quintile Contributions"),
            html.P("How different income groups contribute to overall mental health hospitalization burden."),
            dcc.Graph(
                id='income-pie-chart',
                figure=create_placeholder_chart("Income Quintile Contribution Analysis")
            )
        ], style=STYLE_CARD)
    ])

def clinical_patterns_layout():
    """Page 4: Clinical Patterns"""
    return html.Div([
        html.H2("🏥 Clinical Patterns", style={'color': COLORS['success'], 'marginBottom': '30px'}),
        
        html.P("Understand diagnostic patterns and clinical service utilization across different mental health conditions.", 
               style={'fontSize': '18px', 'marginBottom': '30px'}),
        
        # Visual Element 8: Clinical Heat Map
        html.Div([
            html.H3("Clinical Diagnostic Patterns"),
            html.P("Interactive heat map showing how different mental health diagnoses affect various age groups and genders."),
            dcc.Graph(
                id='clinical-heatmap',
                figure=create_placeholder_chart("Clinical Diagnostic Heat Map", height=600)
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

# Main app layout with sidebar navigation
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    
    # Sidebar navigation
    html.Div([
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
        
    ], style=STYLE_SIDEBAR),
    
    # Main content area
    html.Div(id='page-content', style=STYLE_CONTENT)
])

# Callback to update page content based on URL
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    """Update page content based on URL path"""
    if pathname == '/demographics':
        return demographics_layout()
    elif pathname == '/equity':
        return health_equity_layout()
    elif pathname == '/clinical':
        return clinical_patterns_layout()
    else:  # Default to provincial overview
        return provincial_overview_layout()

# Callback to highlight active navigation button
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
    print("🚀 Starting CIHI Mental Health Dashboard...")
    print("📊 Dashboard available at: http://localhost:8050")
    print("📄 Pages: Provincial Overview, Demographics, Health Equity, Clinical Patterns")
    app.run(debug=True)