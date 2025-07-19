"""
CIHI Mental Health Dashboard
Multi-page dashboard with navigation
"""

import dash
from dash import dcc, html, callback, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import json
import os
import traceback
import sys

# Initialize the Dash app
app = dash.Dash(__name__, suppress_callback_exceptions=True)
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

# Global variable to store data
TABLE3_DF = pd.DataFrame()

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

def load_table3_data():
    """Load and process Table 3 data for provincial trends"""
    print("🔄 Attempting to load Table 3 data...")
    
    try:
        # Check if file exists
        file_path = 'data/table_03.json'
        if not os.path.exists(file_path):
            print(f"❌ ERROR: File not found: {file_path}")
            print(f"📁 Current working directory: {os.getcwd()}")
            print(f"📁 Files in current directory: {os.listdir('.')}")
            if os.path.exists('data'):
                print(f"📁 Files in data directory: {os.listdir('data')}")
            else:
                print("📁 Data directory does not exist!")
            return pd.DataFrame()
        
        print(f"✅ File found: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"✅ JSON loaded successfully")
        print(f"📊 Data keys: {list(data.keys())}")
        
        # Extract data and create DataFrame
        records = []
        years = ["2018-2019", "2019-2020", "2020-2021", "2021-2022", "2022-2023", "2023-2024"]
        
        print(f"📅 Processing years: {years}")
        
        for i, province_data in enumerate(data['data']):
            province = province_data['province']
            print(f"🔄 Processing province {i+1}: {province}")
            
            for year in years:
                if year in province_data:
                    # Clean year format for display
                    year_clean = year.replace('2018-2019', '2018-19').replace('2019-2020', '2019-20').replace('2020-2021', '2020-21').replace('2021-2022', '2021-22').replace('2022-2023', '2022-23').replace('2023-2024', '2023-24')
                    
                    records.append({
                        'Province': province,
                        'Year': year_clean,
                        'N': province_data[year]['N'],
                        'Rate': province_data[year]['Rate']
                    })
        
        df = pd.DataFrame(records)
        print(f"✅ DataFrame created successfully")
        print(f"📊 Shape: {df.shape}")
        print(f"📊 Columns: {list(df.columns)}")
        print(f"📊 Sample data:")
        print(df.head())
        
        return df
    
    except Exception as e:
        print(f"❌ ERROR loading Table 3 data: {str(e)}")
        print(f"🔍 Full error traceback:")
        traceback.print_exc()
        return pd.DataFrame()

def create_provincial_trends_chart(selected_provinces, selected_metric, df):
    """Create the provincial trends line chart"""
    print(f"🔄 Creating chart for provinces: {selected_provinces}, metric: {selected_metric}")
    
    try:
        if df.empty:
            print("❌ DataFrame is empty")
            return create_placeholder_chart("Provincial Hospitalization Trends - Data not available")
        
        print(f"✅ DataFrame has {len(df)} records")
        
        # Filter data for selected provinces
        filtered_df = df[df['Province'].isin(selected_provinces)]
        print(f"🔍 Filtered to {len(filtered_df)} records for selected provinces")
        
        if filtered_df.empty:
            print("❌ No data after filtering")
            return create_placeholder_chart("Please select at least one province")
        
        # Determine y-axis column based on metric selection
        y_column = 'Rate' if selected_metric == 'Rate per 100,000' else 'N'
        y_title = 'Rate per 100,000 population' if selected_metric == 'Rate per 100,000' else 'Number of Cases'
        
        print(f"📊 Using column: {y_column}, title: {y_title}")
        
        # Create line chart
        fig = px.line(
            filtered_df, 
            x='Year', 
            y=y_column,
            color='Province',
            title=f'Mental Health Hospitalizations by Province ({selected_metric})',
            markers=True,
            line_shape='linear'
        )
        
        # Customize layout
        fig.update_layout(
            xaxis_title='Fiscal Year',
            yaxis_title=y_title,
            hovermode='x unified',
            plot_bgcolor='white',
            paper_bgcolor='white',
            font=dict(size=12),
            legend=dict(
                orientation="v",
                yanchor="top",
                y=1,
                xanchor="left",
                x=1.02
            ),
            margin=dict(r=150)  # Add right margin for legend
        )
        
        # Add grid lines
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
        
        print("✅ Chart created successfully")
        return fig
        
    except Exception as e:
        print(f"❌ ERROR creating chart: {str(e)}")
        print(f"🔍 Full error traceback:")
        traceback.print_exc()
        return create_placeholder_chart(f"Error creating chart: {str(e)}")

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

TABLE3_DF = load_table3_data()
if not TABLE3_DF.empty:
    print(f"✅ Loaded Table 3: {len(TABLE3_DF)} records")
    print(f"✅ Provinces available: {sorted(TABLE3_DF['Province'].unique())}")
    
    # Test chart creation
    try:
        print("🔧 Testing chart creation...")
        test_chart = create_provincial_trends_chart(['Canada'], 'Rate per 100,000', TABLE3_DF)
        print("✅ Chart creation test successful")
    except Exception as e:
        print(f"❌ Chart creation test failed: {e}")
        traceback.print_exc()
else:
    print("⚠️ WARNING: Table 3 data not loaded - chart will show placeholder")
print("=" * 60)

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
            
            # Controls
            html.Div([
                html.Div([
                    html.Label("Select Provinces/Territories:", style={'fontWeight': 'bold', 'marginBottom': '5px'}),
                    dcc.Dropdown(
                        id='province-selector',
                        options=[{'label': province, 'value': province} for province in sorted(TABLE3_DF['Province'].unique())] if not TABLE3_DF.empty else [{'label': 'No data available', 'value': 'none'}],
                        value=['Canada', 'Ontario', 'Alberta'] if not TABLE3_DF.empty else ['none'],
                        multi=True,
                        placeholder="Select provinces to compare"
                    )
                ], style={'width': '60%', 'display': 'inline-block', 'marginRight': '5%'}),
                
                html.Div([
                    html.Label("Metric:", style={'fontWeight': 'bold', 'marginBottom': '5px'}),
                    dcc.RadioItems(
                        id='metric-selector',
                        options=[
                            {'label': 'Rate per 100,000', 'value': 'Rate per 100,000'},
                            {'label': 'Number of Cases (N)', 'value': 'Number of Cases (N)'}
                        ],
                        value='Rate per 100,000',
                        inline=True
                    )
                ], style={'width': '35%', 'display': 'inline-block'})
                
            ], style={'marginBottom': '20px'}),
            
            dcc.Graph(
                id='provincial-trends-chart',
                figure=create_provincial_trends_chart(['Canada', 'Ontario', 'Alberta'], 'Rate per 100,000', TABLE3_DF) if not TABLE3_DF.empty else create_placeholder_chart("Provincial Hospitalization Trends - Data not available")
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

# Callback for provincial trends chart
@app.callback(
    Output('provincial-trends-chart', 'figure'),
    [Input('province-selector', 'value'),
     Input('metric-selector', 'value')]
)
def update_provincial_trends_chart(selected_provinces, selected_metric):
    """Update provincial trends chart based on selections"""
    print(f"🔄 Callback triggered with provinces: {selected_provinces}, metric: {selected_metric}")
    
    try:
        if not selected_provinces or 'none' in selected_provinces:
            selected_provinces = ['Canada'] if not TABLE3_DF.empty else []
            print(f"⚠️ No valid provinces selected, defaulting to: {selected_provinces}")
        
        if TABLE3_DF.empty:
            print("⚠️ TABLE3_DF is empty, showing placeholder")
            return create_placeholder_chart("Data not available - please check data/table_03.json file")
        
        result = create_provincial_trends_chart(selected_provinces, selected_metric, TABLE3_DF)
        print("✅ Callback completed successfully")
        return result
        
    except Exception as e:
        print(f"❌ ERROR in callback: {str(e)}")
        print(f"🔍 Full error traceback:")
        traceback.print_exc()
        return create_placeholder_chart(f"Callback error: {str(e)}")

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
    print(f"\n🚀 Starting CIHI Mental Health Dashboard...")
    print(f"📊 Dashboard will be available at: http://localhost:8050")
    print(f"📄 Pages: Provincial Overview, Demographics, Health Equity, Clinical Patterns")
    print(f"🐛 Debug mode: Enabled - errors will show in terminal")
    print(f"⚠️  If you see errors in browser console, check terminal output above")
    
    # Force error output to terminal
    try:
        app.run(debug=True, dev_tools_hot_reload=False, dev_tools_ui=True)
    except Exception as e:
        print(f"\n❌ CRITICAL ERROR starting app: {e}")
        traceback.print_exc()
        sys.exit(1)