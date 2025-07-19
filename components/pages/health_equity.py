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
            
            # Controls
            html.Div([
                html.Div([
                    html.Label("Display Mode:", style={'fontWeight': 'bold', 'marginBottom': '5px'}),
                    dcc.RadioItems(
                        id='income-display-mode',
                        options=[
                            {'label': 'Absolute Rates', 'value': 'Absolute Rates'},
                            {'label': 'Relative to Q5', 'value': 'Relative to Q5'},
                            {'label': '% Above National Average', 'value': 'Percentage Above National Average'}
                        ],
                        value='Absolute Rates',
                        inline=True
                    )
                ], style={'width': '100%', 'marginBottom': '15px'}),
                
                html.Div([
                    html.Label("Options:", style={'fontWeight': 'bold', 'marginBottom': '5px'}),
                    dcc.Checklist(
                        id='income-options',
                        options=[
                            {'label': 'Show Confidence Intervals', 'value': 'show_ci'},
                            {'label': 'Show Q1:Q5 Ratio', 'value': 'show_ratio'},
                            {'label': 'Show Gradient Shading', 'value': 'show_shading'}
                        ],
                        value=['show_ratio', 'show_shading'],
                        inline=True
                    )
                ], style={'width': '100%', 'marginBottom': '20px'})
                
            ], style={'marginBottom': '20px'}),
            
            dcc.Graph(
                id='income-gradient-chart',
                figure=create_income_gradient_chart('Absolute Rates', False, True, True, table12_df) if table12_df is not None and not table12_df.empty else create_placeholder_chart("Income Gradient Analysis - Data not available", height=600)
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
    
    @app.callback(
        Output('income-gradient-chart', 'figure'),
        [Input('income-display-mode', 'value'),
         Input('income-options', 'value')]
    )
    def update_income_gradient_chart(display_mode, options):
        """Update income gradient chart based on selections"""
        print(f"🔄 Income gradient callback triggered with mode: {display_mode}, options: {options}")
        
        try:
            if not display_mode:
                display_mode = 'Absolute Rates'
                print(f"⚠️ No display mode selected, defaulting to: {display_mode}")
            
            if not options:
                options = []
            
            # Extract options
            show_ci = 'show_ci' in options
            show_ratio = 'show_ratio' in options
            show_shading = 'show_shading' in options
            
            if table12_df is None or table12_df.empty:
                print("⚠️ Table 12 DataFrame is empty, showing placeholder")
                return create_placeholder_chart("Income gradient data not available - please check data files")
            
            result = create_income_gradient_chart(display_mode, show_ci, show_ratio, show_shading, table12_df)
            print("✅ Income gradient callback completed successfully")
            return result
            
        except Exception as e:
            print(f"❌ ERROR in income gradient callback: {str(e)}")
            print(f"🔍 Full error traceback:")
            traceback.print_exc()
            return create_placeholder_chart(f"Income gradient callback error: {str(e)}")