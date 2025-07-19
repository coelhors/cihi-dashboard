"""
Demographics page layout and callbacks
"""

from dash import html, dcc, callback, Input, Output
import traceback
from utils.config import COLORS, STYLE_CARD, FISCAL_YEARS_DISPLAY
from utils.chart_helpers import create_placeholder_chart, create_age_gender_chart

def create_layout(table10_df=None):
    """Create Demographics page layout"""
    return html.Div([
        html.H2("👥 Demographics", style={'color': COLORS['secondary'], 'marginBottom': '30px'}),
        
        # Visual Element 4: Age and Gender Patterns
        html.Div([
            html.H3("Age and Gender Patterns"),
            html.P("Interactive analysis showing how mental health hospitalizations vary by age and gender over time."),
            
            # Controls
            html.Div([
                html.Div([
                    html.Label("Select Year:", style={'fontWeight': 'bold', 'marginBottom': '5px'}),
                    dcc.Dropdown(
                        id='demographics-year-selector',
                        options=[{'label': year, 'value': year} for year in FISCAL_YEARS_DISPLAY],
                        value='2023-24',
                        clearable=False,
                        placeholder="Select year"
                    )
                ], style={'width': '40%', 'display': 'inline-block', 'marginRight': '5%'}),
                
                html.Div([
                    html.Label("Display Option:", style={'fontWeight': 'bold', 'marginBottom': '5px'}),
                    dcc.RadioItems(
                        id='demographics-display-option',
                        options=[
                            {'label': 'Absolute Rates', 'value': 'Absolute Rates'},
                            {'label': 'Gender Ratio (F:M)', 'value': 'Gender Ratio (F:M)'}
                        ],
                        value='Absolute Rates',
                        inline=True
                    )
                ], style={'width': '55%', 'display': 'inline-block'})
                
            ], style={'marginBottom': '20px'}),
            
            dcc.Graph(
                id='demographics-chart',
                figure=create_age_gender_chart('2023-24', 'Absolute Rates', False, table10_df) if table10_df is not None and not table10_df.empty else create_placeholder_chart("Age and Gender Analysis - Data not available", height=500)
            )
        ], style=STYLE_CARD)
    ])

def register_callbacks(app, table10_df=None):
    """Register callbacks for Demographics page"""
    
    @app.callback(
        Output('demographics-chart', 'figure'),
        [Input('demographics-year-selector', 'value'),
         Input('demographics-display-option', 'value')]
    )
    def update_demographics_chart(selected_year, display_option):
        """Update demographics chart based on selections"""
        print(f"🔄 Demographics callback triggered with year: {selected_year}, option: {display_option}")
        
        try:
            if not selected_year:
                selected_year = '2023-24'
                print(f"⚠️ No year selected, defaulting to: {selected_year}")
            
            # Always disable confidence intervals since we removed the option
            show_ci = False
            
            if table10_df is None or table10_df.empty:
                print("⚠️ Table 10 DataFrame is empty, showing placeholder")
                return create_placeholder_chart("Age/gender data not available - please check data files")
            
            result = create_age_gender_chart(selected_year, display_option, show_ci, table10_df)
            print("✅ Demographics callback completed successfully")
            return result
            
        except Exception as e:
            print(f"❌ ERROR in demographics callback: {str(e)}")
            print(f"🔍 Full error traceback:")
            traceback.print_exc()
            return create_placeholder_chart(f"Demographics callback error: {str(e)}")