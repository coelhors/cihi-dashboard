"""
Chart helper functions for CIHI Mental Health Dashboard
"""

import plotly.express as px
import plotly.graph_objects as go
from utils.config import COLORS

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
        import traceback
        print(f"🔍 Full error traceback:")
        traceback.print_exc()
        return create_placeholder_chart(f"Error creating chart: {str(e)}")