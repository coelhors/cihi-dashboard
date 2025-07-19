"""
Clinical Patterns page layout and callbacks
"""

from dash import html, dcc, callback, Input, Output
import traceback
from utils.config import COLORS, STYLE_CARD
from utils.chart_helpers import create_placeholder_chart, create_clinical_diagnostic_heatmap

def create_layout(table13_df=None):
    """Create Clinical Patterns page layout"""
    return html.Div([
        html.H2("🏥 Clinical Patterns", style={'color': COLORS['success'], 'marginBottom': '30px'}),
        
        html.P("Understand diagnostic patterns and clinical service utilization across different mental health conditions.", 
               style={'fontSize': '18px', 'marginBottom': '30px'}),
        
        # Visual Element 8: Clinical Heat Map
        html.Div([
            html.H3("Clinical Diagnostic Patterns"),
            html.P("Interactive heat map showing how different mental health diagnoses affect various age groups and genders."),
            
            # Controls
            html.Div([
                html.Div([
                    html.Label("Select Sex:", style={'fontWeight': 'bold', 'marginBottom': '5px'}),
                    dcc.RadioItems(
                        id='clinical-sex-selector',
                        options=[
                            {'label': 'Female', 'value': 'Female'},
                            {'label': 'Male', 'value': 'Male'},
                            {'label': 'Both Combined', 'value': 'Total'}
                        ],
                        value='Female',
                        inline=True
                    )
                ], style={'width': '30%', 'display': 'inline-block', 'marginRight': '5%'}),
                
                html.Div([
                    html.Label("Select Year:", style={'fontWeight': 'bold', 'marginBottom': '5px'}),
                    dcc.Dropdown(
                        id='clinical-year-selector',
                        options=[
                            {'label': '2023-24', 'value': '2023-24'},
                            {'label': '2022-23', 'value': '2022-23'},
                            {'label': '2021-22', 'value': '2021-22'}
                        ],
                        value='2023-24',
                        clearable=False,
                        placeholder="Select year"
                    )
                ], style={'width': '25%', 'display': 'inline-block', 'marginRight': '5%'}),
                
                html.Div([
                    html.Label("Color Scale:", style={'fontWeight': 'bold', 'marginBottom': '5px'}),
                    dcc.Dropdown(
                        id='clinical-color-scale',
                        options=[
                            {'label': 'Linear Scale', 'value': 'Linear Scale'},
                            {'label': 'Log Scale', 'value': 'Log Scale'},
                            {'label': 'Percentile Ranking', 'value': 'Percentile Ranking'},
                            {'label': 'Z-Score Normalization', 'value': 'Z-Score Normalization'}
                        ],
                        value='Linear Scale',
                        clearable=False,
                        placeholder="Select scale"
                    )
                ], style={'width': '35%', 'display': 'inline-block'})
                
            ], style={'marginBottom': '20px'}),
            
            # Diagnosis filter
            html.Div([
                html.Label("Select Diagnosis Categories:", style={'fontWeight': 'bold', 'marginBottom': '5px'}),
                dcc.Checklist(
                    id='clinical-diagnosis-filter',
                    options=[
                        {'label': 'Neurocognitive disorders', 'value': 'Neurocognitive disorders'},
                        {'label': 'Substance-related disorders', 'value': 'Substance-related disorders'},
                        {'label': 'Schizophrenic and psychotic disorders', 'value': 'Schizophrenic and psychotic disorders'},
                        {'label': 'Mood disorders', 'value': 'Mood disorders'},
                        {'label': 'Anxiety disorders', 'value': 'Anxiety disorders'},
                        {'label': 'Personality disorders', 'value': 'Personality disorders'},
                        {'label': 'Other disorders', 'value': 'Other disorders'}
                    ],
                    value=['Mood disorders', 'Anxiety disorders', 'Substance-related disorders', 'Personality disorders', 'Other disorders'],
                    inline=True,
                    style={'marginBottom': '20px'}
                )
            ]),
            
            dcc.Graph(
                id='clinical-heatmap',
                figure=create_clinical_diagnostic_heatmap('2023-24', 'Female', ['Mood disorders', 'Anxiety disorders', 'Substance-related disorders', 'Personality disorders', 'Other disorders'], 'Linear Scale', table13_df) if table13_df is not None and not table13_df.empty else create_placeholder_chart("Clinical Diagnostic Heat Map", height=600)
            )
        ], style=STYLE_CARD),
        
        # Clinical insights section
        html.Div([
            html.H4("Clinical Pattern Insights"),
            html.Ul([
                html.Li("Eating disorders (in Other disorders) peak dramatically in adolescent females"),
                html.Li("Substance-related disorders more common in young adults, especially males"),
                html.Li("Mood disorders show consistent gender differences across all age groups"),
                html.Li("Different conditions emerge at different developmental stages"),
                html.Li("Gender toggle reveals striking male-female differences in diagnostic patterns")
            ])
        ], style=STYLE_CARD)
    ])

def register_callbacks(app, table13_df=None):
    """Register callbacks for Clinical Patterns page"""
    
    @app.callback(
        Output('clinical-heatmap', 'figure'),
        [Input('clinical-year-selector', 'value'),
         Input('clinical-sex-selector', 'value'),
         Input('clinical-diagnosis-filter', 'value'),
         Input('clinical-color-scale', 'value')]
    )
    def update_clinical_heatmap(selected_year, selected_sex, selected_diagnoses, color_scale):
        """Update clinical heatmap based on selections"""
        print(f"🔄 Clinical heatmap callback triggered with year: {selected_year}, sex: {selected_sex}, diagnoses: {len(selected_diagnoses) if selected_diagnoses else 0}, scale: {color_scale}")
        
        try:
            if not selected_year:
                selected_year = '2023-24'
                print(f"⚠️ No year selected, defaulting to: {selected_year}")
            
            if not selected_sex:
                selected_sex = 'Female'
                print(f"⚠️ No sex selected, defaulting to: {selected_sex}")
            
            if not selected_diagnoses:
                selected_diagnoses = ['Mood disorders', 'Anxiety disorders', 'Substance-related disorders']
                print(f"⚠️ No diagnoses selected, defaulting to: {selected_diagnoses}")
            
            if not color_scale:
                color_scale = 'Linear Scale'
                print(f"⚠️ No color scale selected, defaulting to: {color_scale}")
            
            if table13_df is None or table13_df.empty:
                print("⚠️ Table 13 DataFrame is empty, showing placeholder")
                return create_placeholder_chart("Clinical diagnostic data not available - please check data files")
            
            result = create_clinical_diagnostic_heatmap(selected_year, selected_sex, selected_diagnoses, color_scale, table13_df)
            print("✅ Clinical heatmap callback completed successfully")
            return result
            
        except Exception as e:
            print(f"❌ ERROR in clinical heatmap callback: {str(e)}")
            print(f"🔍 Full error traceback:")
            traceback.print_exc()
            return create_placeholder_chart(f"Clinical heatmap callback error: {str(e)}")