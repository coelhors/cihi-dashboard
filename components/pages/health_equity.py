"""
Health Equity page layout and callbacks
"""

from dash import html, dcc, callback, Input, Output
import traceback
from utils.config import COLORS, STYLE_CARD
from utils.chart_helpers import create_placeholder_chart, create_urban_rural_disparity_chart

def create_layout(table11_df=None):
    """Create Health Equity page layout"""
    return html.Div([
        html.H2("⚖️ Health Equity", style={'color': COLORS['accent'], 'marginBottom': '30px'}),
        
        html.P("Examine disparities in mental health hospitalizations across geographic and socioeconomic dimensions.", 
               style={'fontSize': '18px', 'marginBottom': '30px'}),
        
        # Visual Element 5: Urban vs Rural
        html.Div([
            html.H3("Urban vs Rural Disparities"),
            html.P("Comparison of mental health hospitalization rates between urban and rural/remote areas."),
            
            # Controls
            html.Div([
                html.Div([
                    html.Label("Display Mode:", style={'fontWeight': 'bold', 'marginBottom': '5px'}),
                    dcc.RadioItems(
                        id='urban-rural-display-mode',
                        options=[
                            {'label': 'Absolute Rates', 'value': 'Absolute Rates'},
                            {'label': 'Ratio View (Rural:Urban)', 'value': 'Ratio View (Rural:Urban)'},
                            {'label': 'Percentage Above Urban', 'value': 'Percentage Above Urban'}
                        ],
                        value='Absolute Rates',
                        inline=True
                    )
                ], style={'width': '100%', 'marginBottom': '15px'}),
                
                html.Div([
                    html.Label("Options:", style={'fontWeight': 'bold', 'marginBottom': '5px'}),
                    dcc.Checklist(
                        id='urban-rural-options',
                        options=[
                            {'label': 'Show Confidence Intervals', 'value': 'show_ci'},
                            {'label': 'Highlight Disparity Gap', 'value': 'highlight_gap'},
                            {'label': 'Show Percentage Difference', 'value': 'show_percentage'}
                        ],
                        value=['highlight_gap'],
                        inline=True
                    )
                ], style={'width': '100%'})
                
            ], style={'marginBottom': '20px'}),
            
            dcc.Graph(
                id='urban-rural-chart',
                figure=create_urban_rural_disparity_chart('Absolute Rates', False, True, False, table11_df) if table11_df is not None and not table11_df.empty else create_placeholder_chart("Urban vs Rural Disparities - Data not available")
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

def register_callbacks(app, table11_df=None):
    """Register callbacks for Health Equity page"""
    
    @app.callback(
        Output('urban-rural-chart', 'figure'),
        [Input('urban-rural-display-mode', 'value'),
         Input('urban-rural-options', 'value')]
    )
    def update_urban_rural_chart(display_mode, options):
        """Update urban vs rural chart based on selections"""
        print(f"🔄 Urban/rural callback triggered with mode: {display_mode}, options: {options}")
        
        try:
            if not display_mode:
                display_mode = 'Absolute Rates'
                print(f"⚠️ No display mode selected, defaulting to: {display_mode}")
            
            # Parse options
            show_ci = 'show_ci' in options if options else False
            highlight_gap = 'highlight_gap' in options if options else False
            show_percentage = 'show_percentage' in options if options else False
            
            if table11_df is None or table11_df.empty:
                print("⚠️ Table 11 DataFrame is empty, showing placeholder")
                return create_placeholder_chart("Urban/rural data not available - please check data files")
            
            result = create_urban_rural_disparity_chart(display_mode, show_ci, highlight_gap, show_percentage, table11_df)
            print("✅ Urban/rural callback completed successfully")
            return result
            
        except Exception as e:
            print(f"❌ ERROR in urban/rural callback: {str(e)}")
            print(f"🔍 Full error traceback:")
            traceback.print_exc()
            return create_placeholder_chart(f"Urban/rural callback error: {str(e)}")