"""
Clinical Patterns page layout and callbacks - Updated with horizontal controls
"""

from dash import html, dcc, callback, Input, Output
import traceback
from utils.config import COLORS, STYLE_CARD
from utils.chart_helpers import create_placeholder_chart, create_clinical_diagnostic_heatmap

def create_layout(table13_df=None):
    """Create Clinical Patterns page layout with horizontal controls"""
    return html.Div([
        html.H2("🏥 Clinical Patterns", style={'color': COLORS['success'], 'marginBottom': '30px'}),
        
        html.P("Understand diagnostic patterns and clinical service utilization across different mental health conditions.", 
               style={'fontSize': '18px', 'marginBottom': '30px'}),
        
        # Visual Element 8: Clinical Heat Map
        html.Div([
            html.H3("Clinical Diagnostic Patterns"),
            html.P("Interactive heat map showing how different mental health diagnoses affect various age groups and genders."),
            
            # Controls - Arranged horizontally with reduced widths
            html.Div([
                # Sex Selection - Left column (reduced width)
                html.Div([
                    html.Label("Select Sex:", style={'fontWeight': 'bold', 'marginBottom': '10px', 'display': 'block'}),
                    dcc.RadioItems(
                        id='clinical-sex-selector',
                        options=[
                            {'label': 'Female', 'value': 'Female'},
                            {'label': 'Male', 'value': 'Male'},
                            {'label': 'Both Combined', 'value': 'Total'}
                        ],
                        value='Female',
                        inline=False,
                        style={'marginBottom': '10px'}
                    )
                ], style={
                    'width': '22%', 
                    'display': 'inline-block', 
                    'verticalAlign': 'top',
                    'marginRight': '2%',
                    'padding': '10px',
                    'backgroundColor': '#f8f9fa',
                    'borderRadius': '5px',
                    'border': '1px solid #dee2e6'
                }),
                
                # Year Selection - Middle column (reduced width)
                html.Div([
                    html.Label("Select Year:", style={'fontWeight': 'bold', 'marginBottom': '10px', 'display': 'block'}),
                    dcc.RadioItems(
                        id='clinical-year-selector',
                        options=[
                            {'label': '2023-24', 'value': '2023-24'},
                            {'label': '2022-23', 'value': '2022-23'},
                            {'label': '2021-22', 'value': '2021-22'}
                        ],
                        value='2023-24',
                        inline=False,
                        style={'marginBottom': '10px'}
                    )
                ], style={
                    'width': '22%', 
                    'display': 'inline-block', 
                    'verticalAlign': 'top',
                    'marginRight': '2%',
                    'padding': '10px',
                    'backgroundColor': '#f8f9fa',
                    'borderRadius': '5px',
                    'border': '1px solid #dee2e6'
                }),
                
                # Diagnosis Selection - Right column (much smaller width)
                html.Div([
                    html.Label("Select Diagnosis Categories:", style={'fontWeight': 'bold', 'marginBottom': '10px', 'display': 'block'}),
                    dcc.Checklist(
                        id='clinical-diagnosis-filter',
                        options=[
                            {'label': 'Neurocognitive disorders', 'value': 'Neurocognitive disorders'},
                            {'label': 'Substance-related disorders', 'value': 'Substance-related disorders'},
                            {'label': 'Schizophrenic and psychotic disorders', 'value': 'Schizophrenic and psychotic disorders'},
                            {'label': 'Mood disorders', 'value': 'Mood disorders'},
                            {'label': 'Anxiety disorders', 'value': 'Anxiety disorders'},
                            {'label': 'Personality disorders', 'value': 'Personality disorders'}
                        ],
                        value=['Neurocognitive disorders', 'Substance-related disorders', 'Schizophrenic and psychotic disorders', 'Mood disorders', 'Anxiety disorders', 'Personality disorders'],
                        inline=False,
                        style={'fontSize': '12px'}  # Smaller font for better fit
                    )
                ], style={
                    'width': '32%', 
                    'display': 'inline-block', 
                    'verticalAlign': 'top',
                    'padding': '8px',
                    'backgroundColor': '#f8f9fa',
                    'borderRadius': '5px',
                    'border': '1px solid #dee2e6'
                })
                
            ], style={
                'marginBottom': '30px',
                'display': 'flex',
                'flexWrap': 'wrap',
                'gap': '2%'
            }),  # Added flexbox properties for better horizontal layout
            
            # Heatmap visualization
            dcc.Graph(
                id='clinical-heatmap',
                figure=create_clinical_diagnostic_heatmap('2023-24', 'Female', ['Neurocognitive disorders', 'Substance-related disorders', 'Schizophrenic and psychotic disorders', 'Mood disorders', 'Anxiety disorders', 'Personality disorders'], table13_df) if table13_df is not None and not table13_df.empty else create_placeholder_chart("Clinical Diagnostic Heat Map", height=600)
            )
        ], style=STYLE_CARD)
    ])

def register_callbacks(app, table13_df=None):
    """Register callbacks for Clinical Patterns page"""
    
    @app.callback(
        Output('clinical-heatmap', 'figure'),
        [Input('clinical-year-selector', 'value'),
         Input('clinical-sex-selector', 'value'),
         Input('clinical-diagnosis-filter', 'value')]
    )
    def update_clinical_heatmap(selected_year, selected_sex, selected_diagnoses):
        """Update clinical heatmap based on selections"""
        print(f"🔄 Clinical heatmap callback triggered with year: {selected_year}, sex: {selected_sex}, diagnoses: {len(selected_diagnoses) if selected_diagnoses else 0}")
        
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
            
            if table13_df is None or table13_df.empty:
                print("⚠️ Table 13 DataFrame is empty, showing placeholder")
                return create_placeholder_chart("Clinical diagnostic data not available - please check data files")
            
            result = create_clinical_diagnostic_heatmap(selected_year, selected_sex, selected_diagnoses, table13_df)
            print("✅ Clinical heatmap callback completed successfully")
            return result
            
        except Exception as e:
            print(f"❌ ERROR in clinical heatmap callback: {str(e)}")
            print(f"🔍 Full error traceback:")
            traceback.print_exc()
            return create_placeholder_chart(f"Clinical heatmap callback error: {str(e)}")