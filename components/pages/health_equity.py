"""
Health Equity page layout and callbacks
"""

from dash import html, dcc, callback, Input, Output
import traceback
from utils.config import COLORS, STYLE_CARD
from utils.chart_helpers import create_placeholder_chart, create_urban_rural_disparity_chart, create_income_gradient_chart, create_income_quintile_contribution_pie

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
            
            # Controls
            html.Div([
                html.Label("Select Fiscal Year:", style={'fontWeight': 'bold', 'marginBottom': '5px'}),
                dcc.Dropdown(
                    id='income-pie-year-selector',
                    options=[
                        {'label': '2018-19', 'value': '2018-19'},
                        {'label': '2019-20', 'value': '2019-20'},
                        {'label': '2020-21', 'value': '2020-21'},
                        {'label': '2021-22', 'value': '2021-22'},
                        {'label': '2022-23', 'value': '2022-23'},
                        {'label': '2023-24', 'value': '2023-24'}
                    ],
                    value='2023-24',
                    clearable=False,
                    placeholder="Select year"
                )
            ], style={'width': '45%', 'marginBottom': '20px'}),
            
            dcc.Graph(
                id='income-contribution-pie-chart',
                figure=create_income_quintile_contribution_pie('2023-24', table12_df) if table12_df is not None and not table12_df.empty else create_placeholder_chart("Income Quintile Contribution Analysis")
            )
        ], style=STYLE_CARD)
    ])

def register_callbacks(app, table11_df=None, table12_df=None):
    """Register callbacks for Health Equity page"""
    
    @app.callback(
        Output('income-contribution-pie-chart', 'figure'),
        [Input('income-pie-year-selector', 'value')]
    )
    def update_income_contribution_pie_chart(selected_year):
        """Update income contribution pie chart based on year selection"""
        print(f"🔄 Income contribution pie callback triggered with year: {selected_year}")
        
        try:
            if not selected_year:
                selected_year = '2023-24'
                print(f"⚠️ No year selected, defaulting to: {selected_year}")
            
            if table12_df is None or table12_df.empty:
                print("⚠️ Table 12 DataFrame is empty, showing placeholder")
                return create_placeholder_chart("Income quintile data not available - please check data files")
            
            result = create_income_quintile_contribution_pie(selected_year, table12_df)
            print("✅ Income contribution pie callback completed successfully")
            return result
            
        except Exception as e:
            print(f"❌ ERROR in income contribution pie callback: {str(e)}")
            print(f"🔍 Full error traceback:")
            traceback.print_exc()
            return create_placeholder_chart(f"Income contribution pie callback error: {str(e)}")