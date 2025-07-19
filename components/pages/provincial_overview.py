"""
Provincial Overview page layout and callbacks
"""

from dash import dcc, html, callback, Input, Output
import traceback
from utils.config import COLORS, STYLE_CARD
from utils.chart_helpers import create_placeholder_chart, create_provincial_trends_chart, create_mental_health_vs_other_chart
from utils.data_loader import get_province_options, get_default_provinces

def create_layout(table3_df, combined_df=None):
    """Create Provincial Overview page layout"""
    return html.Div([
        html.H2("📊 Provincial Overview", style={'color': COLORS['primary'], 'marginBottom': '30px'}),
        
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
                        options=get_province_options(table3_df),
                        value=get_default_provinces(table3_df),
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
                figure=create_provincial_trends_chart(get_default_provinces(table3_df), 'Rate per 100,000', table3_df) if not table3_df.empty else create_placeholder_chart("Provincial Hospitalization Trends - Data not available")
            )
        ], style=STYLE_CARD),
        
        # Visual Element 2: Mental Health vs Other Conditions
        html.Div([
            html.H3("Mental Health vs Other Conditions"),
            html.P("Comparison of mental health hospitalizations with other medical conditions."),
            
            # Controls for comparison chart
            html.Div([
                html.Div([
                    html.Label("Select Province/Territory:", style={'fontWeight': 'bold', 'marginBottom': '5px'}),
                    dcc.Dropdown(
                        id='comparison-province-selector',
                        options=get_province_options(table3_df),
                        value='Canada' if not table3_df.empty and 'Canada' in table3_df['Province'].unique() else (get_default_provinces(table3_df)[0] if not table3_df.empty else 'none'),
                        clearable=False,
                        placeholder="Select a province"
                    )
                ], style={'width': '60%', 'display': 'inline-block', 'marginRight': '5%'}),
                
                html.Div([
                    html.Label("Metric:", style={'fontWeight': 'bold', 'marginBottom': '5px'}),
                    dcc.RadioItems(
                        id='comparison-metric-selector',
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
                id='comparison-chart',
                figure=create_mental_health_vs_other_chart('Canada', 'Rate per 100,000', combined_df) if combined_df is not None and not combined_df.empty else create_placeholder_chart("Mental Health vs Other Conditions Comparison - Data not available")
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

def register_callbacks(app, table3_df, combined_df=None):
    """Register callbacks for Provincial Overview page"""
    
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
                selected_provinces = get_default_provinces(table3_df)
                print(f"⚠️ No valid provinces selected, defaulting to: {selected_provinces}")
            
            if table3_df.empty:
                print("⚠️ TABLE3_DF is empty, showing placeholder")
                return create_placeholder_chart("Data not available - please check data/table_03.json file")
            
            result = create_provincial_trends_chart(selected_provinces, selected_metric, table3_df)
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
        [Input('comparison-province-selector', 'value'),
         Input('comparison-metric-selector', 'value')]
    )
    def update_comparison_chart(selected_province, selected_metric):
        """Update comparison chart based on selections"""
        print(f"🔄 Comparison callback triggered with province: {selected_province}, metric: {selected_metric}")
        
        try:
            if not selected_province or selected_province == 'none':
                selected_province = 'Canada' if not table3_df.empty and 'Canada' in table3_df['Province'].unique() else get_default_provinces(table3_df)[0]
                print(f"⚠️ No valid province selected, defaulting to: {selected_province}")
            
            if combined_df is None or combined_df.empty:
                print("⚠️ Combined DataFrame is empty, showing placeholder")
                return create_placeholder_chart("Comparison data not available - please check data files")
            
            result = create_mental_health_vs_other_chart(selected_province, selected_metric, combined_df)
            print("✅ Comparison callback completed successfully")
            return result
            
        except Exception as e:
            print(f"❌ ERROR in comparison callback: {str(e)}")
            print(f"🔍 Full error traceback:")
            traceback.print_exc()
            return create_placeholder_chart(f"Comparison callback error: {str(e)}")