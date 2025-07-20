"""
Provincial Overview page layout and callbacks - Updated with checklist for province selection
"""

from dash import dcc, html, callback, Input, Output
import traceback
from utils.config import COLORS, STYLE_CARD
from utils.chart_helpers import create_placeholder_chart, create_provincial_trends_chart, create_mental_health_vs_other_chart, create_provincial_contribution_pie_chart
from utils.data_loader import get_province_options, get_default_provinces

def create_layout(table3_df, combined_df=None):
    """Create Provincial Overview page layout with checklist for province selection"""
    return html.Div([
        html.H2("📊 Provincial Overview", style={'color': COLORS['primary'], 'marginBottom': '30px'}),
        
        # Visual Element 1: Provincial Trends
        html.Div([
            html.H3("Provincial Hospitalization Trends"),
            html.P("Interactive line chart showing hospitalization rates by province over time."),
            
            # Controls - Simplified with only province selection
            html.Div([
                html.Div([
                    html.Label("Select Provinces/Territories:", style={'fontWeight': 'bold', 'marginBottom': '10px', 'display': 'block'}),
                    dcc.Checklist(
                        id='province-selector',
                        options=[
                            {'label': 'Alberta', 'value': 'Alberta'},
                            {'label': 'British Columbia', 'value': 'British Columbia'},
                            {'label': 'Manitoba', 'value': 'Manitoba'},
                            {'label': 'New Brunswick', 'value': 'New Brunswick'},
                            {'label': 'Newfoundland and Labrador', 'value': 'Newfoundland and Labrador'},
                            {'label': 'Northwest Territories', 'value': 'Northwest Territories'},
                            {'label': 'Nova Scotia', 'value': 'Nova Scotia'},
                            {'label': 'Nunavut', 'value': 'Nunavut'},
                            {'label': 'Ontario', 'value': 'Ontario'},
                            {'label': 'Prince Edward Island', 'value': 'Prince Edward Island'},
                            {'label': 'Quebec', 'value': 'Quebec'},
                            {'label': 'Saskatchewan', 'value': 'Saskatchewan'},
                            {'label': 'Yukon', 'value': 'Yukon'},
                            {'label': 'Canada', 'value': 'Canada'}
                        ],
                        value=['Alberta'],  # Default to Alberta only
                        inline=False,
                        style={'fontSize': '12px', 'marginBottom': '10px'}
                    )
                ], style={
                    'width': '45%', 
                    'display': 'inline-block', 
                    'verticalAlign': 'top',
                    'padding': '12px',
                    'backgroundColor': '#f8f9fa',
                    'borderRadius': '5px',
                    'border': '1px solid #dee2e6'
                })
                
            ], style={'marginBottom': '20px'}),
            
            dcc.Graph(
                id='provincial-trends-chart',
                figure=create_provincial_trends_chart(['Alberta'], 'Rate per 100,000', table3_df) if not table3_df.empty else create_placeholder_chart("Provincial Hospitalization Trends - Data not available")
            )
        ], style=STYLE_CARD),
        
        # Visual Element 2: Mental Health vs Other Conditions
        html.Div([
            html.H3("Mental Health vs Other Conditions"),
            html.P("Comparison of mental health hospitalizations with other medical conditions."),
            
            # Controls for comparison chart - Simplified with radio items
            html.Div([
                html.Div([
                    html.Label("Select Province/Territory:", style={'fontWeight': 'bold', 'marginBottom': '10px', 'display': 'block'}),
                    dcc.RadioItems(
                        id='comparison-province-selector',
                        options=[
                            {'label': 'Canada', 'value': 'Canada'},
                            {'label': 'Alberta', 'value': 'Alberta'},
                            {'label': 'British Columbia', 'value': 'British Columbia'},
                            {'label': 'Ontario', 'value': 'Ontario'},
                            {'label': 'Quebec', 'value': 'Quebec'},
                            {'label': 'Manitoba', 'value': 'Manitoba'},
                            {'label': 'Saskatchewan', 'value': 'Saskatchewan'},
                            {'label': 'Nova Scotia', 'value': 'Nova Scotia'},
                            {'label': 'New Brunswick', 'value': 'New Brunswick'},
                            {'label': 'Newfoundland and Labrador', 'value': 'Newfoundland and Labrador'},
                            {'label': 'Prince Edward Island', 'value': 'Prince Edward Island'},
                            {'label': 'Northwest Territories', 'value': 'Northwest Territories'},
                            {'label': 'Yukon', 'value': 'Yukon'},
                            {'label': 'Nunavut', 'value': 'Nunavut'}
                        ],
                        value='Canada',  # Default to Canada
                        inline=False,
                        style={'fontSize': '12px'}
                    )
                ], style={
                    'width': '45%', 
                    'display': 'inline-block', 
                    'padding': '12px',
                    'backgroundColor': '#f8f9fa',
                    'borderRadius': '5px',
                    'border': '1px solid #dee2e6'
                })
                
            ], style={'marginBottom': '20px'}),
            
            dcc.Graph(
                id='comparison-chart',
                figure=create_mental_health_vs_other_chart('Canada', 'Rate per 100,000', combined_df) if combined_df is not None and not combined_df.empty else create_placeholder_chart("Mental Health vs Other Conditions Comparison - Data not available")
            )
        ], style=STYLE_CARD),
        
        # Visual Element 3: Provincial Contributions
        html.Div([
            html.H3("Provincial Contribution Analysis"),
            html.P("Each province's share of total mental health hospitalizations."),
            
            # Controls for pie chart - Simplified with radio items (reduced width)
            html.Div([
                html.Div([
                    html.Label("Select Fiscal Year:", style={'fontWeight': 'bold', 'marginBottom': '10px', 'display': 'block'}),
                    dcc.RadioItems(
                        id='pie-year-selector',
                        options=[
                            {'label': '2018-19', 'value': '2018-19'},
                            {'label': '2019-20', 'value': '2019-20'},
                            {'label': '2020-21', 'value': '2020-21'},
                            {'label': '2021-22', 'value': '2021-22'},
                            {'label': '2022-23', 'value': '2022-23'},
                            {'label': '2023-24', 'value': '2023-24'}
                        ],
                        value='2023-24',  # Default to most recent year
                        inline=False,
                        style={'fontSize': '12px'}
                    )
                ], style={
                    'width': '25%', 
                    'display': 'inline-block', 
                    'padding': '12px',
                    'backgroundColor': '#f8f9fa',
                    'borderRadius': '5px',
                    'border': '1px solid #dee2e6'
                })
                
            ], style={'marginBottom': '20px'}),
            
            dcc.Graph(
                id='provincial-pie-chart',
                figure=create_provincial_contribution_pie_chart('2023-24', 'Rate per 100,000', table3_df) if not table3_df.empty else create_placeholder_chart("Provincial Contribution Pie Chart - Data not available")
            )
        ], style=STYLE_CARD)
    ])

def register_callbacks(app, table3_df, combined_df=None):
    """Register callbacks for Provincial Overview page"""
    
    @app.callback(
        Output('provincial-trends-chart', 'figure'),
        [Input('province-selector', 'value')]
    )
    def update_provincial_trends_chart(selected_provinces):
        """Update provincial trends chart based on province selection (fixed to Rate per 100,000)"""
        print(f"🔄 Callback triggered with provinces: {selected_provinces}")
        
        try:
            if not selected_provinces or len(selected_provinces) == 0:
                selected_provinces = ['Alberta']
                print(f"⚠️ No provinces selected, defaulting to: {selected_provinces}")
            
            if table3_df.empty:
                print("⚠️ TABLE3_DF is empty, showing placeholder")
                return create_placeholder_chart("Data not available - please check data/table_03.json file")
            
            # Always use "Rate per 100,000" as the metric
            result = create_provincial_trends_chart(selected_provinces, 'Rate per 100,000', table3_df)
            print("✅ Callback completed successfully")
            return result
            
        except Exception as e:
            print(f"❌ ERROR in callback: {str(e)}")
            print(f"🔍 Full error traceback:")
            traceback.print_exc()
            return create_placeholder_chart(f"Callback error: {str(e)}")
    
    # Callback for mental health vs other conditions comparison chart
    @app.callback(
        Output('comparison-chart', 'figure'),
        [Input('comparison-province-selector', 'value')]
    )
    def update_comparison_chart(selected_province):
        """Update comparison chart based on province selection (fixed to Rate per 100,000)"""
        print(f"🔄 Comparison callback triggered with province: {selected_province}")
        
        try:
            if not selected_province:
                selected_province = 'Canada'
                print(f"⚠️ No province selected, defaulting to: {selected_province}")
            
            if combined_df is None or combined_df.empty:
                print("⚠️ Combined DataFrame is empty, showing placeholder")
                return create_placeholder_chart("Comparison data not available - please check data files")
            
            # Always use "Rate per 100,000" as the metric
            result = create_mental_health_vs_other_chart(selected_province, 'Rate per 100,000', combined_df)
            print("✅ Comparison callback completed successfully")
            return result
            
        except Exception as e:
            print(f"❌ ERROR in comparison callback: {str(e)}")
            print(f"🔍 Full error traceback:")
            traceback.print_exc()
            return create_placeholder_chart(f"Comparison callback error: {str(e)}")
    
    # Callback for provincial contribution pie chart
    @app.callback(
        Output('provincial-pie-chart', 'figure'),
        [Input('pie-year-selector', 'value')]
    )
    def update_pie_chart(selected_year):
        """Update pie chart based on year selection (fixed to Rate per 100,000)"""
        print(f"🔄 Pie chart callback triggered with year: {selected_year}")
        
        try:
            if not selected_year:
                selected_year = '2023-24'
                print(f"⚠️ No year selected, defaulting to: {selected_year}")
            
            if table3_df.empty:
                print("⚠️ Table 3 DataFrame is empty, showing placeholder")
                return create_placeholder_chart("Provincial data not available - please check data files")
            
            # Always use "Rate per 100,000" as the metric
            result = create_provincial_contribution_pie_chart(selected_year, 'Rate per 100,000', table3_df)
            print("✅ Pie chart callback completed successfully")
            return result
            
        except Exception as e:
            print(f"❌ ERROR in pie chart callback: {str(e)}")
            print(f"🔍 Full error traceback:")
            traceback.print_exc()
            return create_placeholder_chart(f"Pie chart callback error: {str(e)}")