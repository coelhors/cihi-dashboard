"""
CIHI Mental Health Dashboard
Simple starter application
"""

import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "CIHI Mental Health Dashboard"

# Simple layout
app.layout = html.Div([
    
    # Header
    html.H1("CIHI Mental Health Dashboard", 
            style={'textAlign': 'center', 'color': '#2E86AB', 'marginBottom': '30px'}),
    
    html.P("Interactive Analysis of Canadian Youth Mental Health Crisis Data", 
           style={'textAlign': 'center', 'fontSize': '18px', 'marginBottom': '40px'}),
    
    # Simple placeholder chart
    html.Div([
        html.H3("Sample Chart"),
        dcc.Graph(
            id='sample-chart',
            figure=px.bar(
                x=['2018-19', '2019-20', '2020-21', '2021-22', '2022-23', '2023-24'], 
                y=[100, 120, 180, 200, 190, 170],
                title="Sample Mental Health Data",
                labels={'x': 'Fiscal Year', 'y': 'Rate per 100,000'}
            )
        )
    ], style={'margin': '20px auto', 'maxWidth': '800px'}),
    
    # Footer
    html.Hr(),
    html.P("Data Source: CIHI - Care for Children and Youth With Mental Disorders", 
           style={'textAlign': 'center', 'color': '#666', 'fontSize': '14px'})
           
], style={'margin': '20px', 'fontFamily': 'Arial, sans-serif'})

# Run the app
if __name__ == '__main__':
    print("🚀 Starting CIHI Mental Health Dashboard...")
    print("📊 Dashboard available at: http://localhost:8050")
    app.run_server(debug=True)