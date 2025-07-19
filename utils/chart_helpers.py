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
def create_mental_health_vs_other_chart(selected_province, selected_metric, combined_df):
    """Create mental health vs other conditions stacked area chart"""
    print(f"🔄 Creating comparison chart for province: {selected_province}, metric: {selected_metric}")
    
    try:
        if combined_df.empty:
            print("❌ Combined DataFrame is empty")
            return create_placeholder_chart("Mental Health vs Other Conditions - Data not available")
        
        # Filter data for selected province
        filtered_df = combined_df[combined_df['Province'] == selected_province]
        print(f"🔍 Filtered to {len(filtered_df)} records for {selected_province}")
        
        if filtered_df.empty:
            print("❌ No data after filtering")
            return create_placeholder_chart(f"No data available for {selected_province}")
        
        # Determine which columns to use based on metric selection
        if selected_metric == 'Rate per 100,000':
            mh_col = 'MH_Rate'
            other_col = 'Other_Rate'
            total_col = 'Total_Rate'
            y_title = 'Rate per 100,000 population'
        else:
            mh_col = 'MH_N'
            other_col = 'Other_N'
            total_col = 'Total_N'
            y_title = 'Number of Cases'
        
        print(f"📊 Using columns: {mh_col}, {other_col}, {total_col}")
        
        # Create stacked area chart using plotly graph objects
        fig = go.Figure()
        
        # Add Mental Health area (bottom layer)
        fig.add_trace(go.Scatter(
            x=filtered_df['Year'],
            y=filtered_df[mh_col],
            fill='tonexty',
            mode='lines+markers',
            name='Mental Health',
            line=dict(color='#E74C3C', width=2),
            fillcolor='rgba(231, 76, 60, 0.3)',
            hovertemplate=f'<b>Mental Health</b><br>Year: %{{x}}<br>{y_title}: %{{y:,.0f}}<extra></extra>'
        ))
        
        # Add Other Conditions area (middle layer)
        fig.add_trace(go.Scatter(
            x=filtered_df['Year'],
            y=filtered_df[total_col],
            fill='tonexty',
            mode='lines+markers',
            name='Other Conditions',
            line=dict(color='#3498DB', width=2),
            fillcolor='rgba(52, 152, 219, 0.3)',
            hovertemplate=f'<b>Other Conditions</b><br>Year: %{{x}}<br>{y_title}: %{{customdata:,.0f}}<extra></extra>',
            customdata=filtered_df[other_col]
        ))
        
        # Add total boundary line
        fig.add_trace(go.Scatter(
            x=filtered_df['Year'],
            y=filtered_df[total_col],
            mode='lines',
            name='Total',
            line=dict(color='#2C3E50', width=3, dash='dash'),
            hovertemplate=f'<b>Total</b><br>Year: %{{x}}<br>{y_title}: %{{y:,.0f}}<br>MH as % of Total: %{{customdata:.1f}}%<extra></extra>',
            customdata=filtered_df['MH_Percentage']
        ))
        
        # Update layout
        fig.update_layout(
            title=f'Mental Health vs Other Conditions Hospitalizations - {selected_province} ({selected_metric})',
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
            margin=dict(r=150)
        )
        
        # Add grid lines
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
        
        print("✅ Comparison chart created successfully")
        return fig
        
    except Exception as e:
        print(f"❌ ERROR creating comparison chart: {str(e)}")
        import traceback
        print(f"🔍 Full error traceback:")
        traceback.print_exc()
def create_provincial_contribution_pie_chart(selected_year, selected_metric, table3_df):
    """Create provincial contribution pie chart"""
    print(f"🔄 Creating pie chart for year: {selected_year}, metric: {selected_metric}")
    
    try:
        if table3_df.empty:
            print("❌ Table 3 DataFrame is empty")
            return create_placeholder_chart("Provincial Contribution - Data not available")
        
        # Filter data for selected year and exclude Canada total
        filtered_df = table3_df[
            (table3_df['Year'] == selected_year) & 
            (table3_df['Province'] != 'Canada')
        ].copy()
        
        print(f"🔍 Filtered to {len(filtered_df)} provinces for year {selected_year}")
        
        if filtered_df.empty:
            print("❌ No data after filtering")
            return create_placeholder_chart(f"No provincial data available for {selected_year}")
        
        # Determine which column to use based on metric selection
        if selected_metric == 'Number of Cases (N)':
            value_col = 'N'
            title_suffix = 'by Number of Cases'
            hover_template = (
                "<b>%{label}</b><br>"
                "Year: " + selected_year + "<br>"
                "Cases: %{value:,.0f}<br>"
                "Percentage: %{percent}<br>"
                "Rate per 100k: %{customdata:.0f}"
                "<extra></extra>"
            )
        else:
            value_col = 'Rate'
            title_suffix = 'by Rate per 100,000'
            hover_template = (
                "<b>%{label}</b><br>"
                "Year: " + selected_year + "<br>"
                "Rate per 100k: %{value:.0f}<br>"
                "Percentage: %{percent}<br>"
                "Cases: %{customdata:,.0f}"
                "<extra></extra>"
            )
        
        print(f"📊 Using column: {value_col} for {title_suffix}")
        
        # Sort by value for better visual presentation
        filtered_df = filtered_df.sort_values(value_col, ascending=False)
        
        # Create pie chart
        fig = px.pie(
            filtered_df,
            values=value_col,
            names='Province',
            title=f'Provincial Mental Health Hospitalization Contributions - {selected_year}<br><sub>{title_suffix}</sub>',
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        
        # Customize the pie chart
        fig.update_traces(
            textposition='inside',
            textinfo='percent+label',
            hovertemplate=hover_template,
            customdata=filtered_df['Rate'] if selected_metric == 'Number of Cases (N)' else filtered_df['N'],
            pull=[0.1 if province == 'Alberta' else 0 for province in filtered_df['Province']]
        )
        
        # Update layout
        fig.update_layout(
            font=dict(size=12),
            legend=dict(
                orientation="v",
                yanchor="middle",
                y=0.5,
                xanchor="left",
                x=1.02
            ),
            margin=dict(r=150, l=50, t=80, b=50),
            showlegend=True,
            height=600,
            width=1000
        )
        
        print("✅ Pie chart created successfully")
        return fig
        
    except Exception as e:
        print(f"❌ ERROR creating pie chart: {str(e)}")
        import traceback
        print(f"🔍 Full error traceback:")
        traceback.print_exc()
def create_age_gender_chart(selected_year, display_option, show_ci, table10_df):
    """Create age and gender patterns bar chart"""
    print(f"🔄 Creating age/gender chart for year: {selected_year}, option: {display_option}, CI: {show_ci}")
    
    try:
        if table10_df.empty:
            print("❌ Table 10 DataFrame is empty")
            return create_placeholder_chart("Age and Gender Analysis - Data not available")
        
        # Filter data for selected year and exclude 'Total' sex category
        filtered_df = table10_df[
            (table10_df['Year'] == selected_year) & 
            (table10_df['Sex'] != 'Total')
        ].copy()
        
        print(f"🔍 Filtered to {len(filtered_df)} records for year {selected_year}")
        
        if filtered_df.empty:
            print("❌ No data after filtering")
            return create_placeholder_chart(f"No age/gender data available for {selected_year}")
        
        if display_option == "Absolute Rates":
            # Create grouped bar chart
            fig = px.bar(
                filtered_df,
                x='Age_Group',
                y='Rate',
                color='Sex',
                title=f'Mental Health Hospitalizations by Age and Gender - {selected_year}',
                labels={'Rate': 'Rate per 100,000 population', 'Age_Group': 'Age Group'},
                color_discrete_map={'Female': '#4CAF50', 'Male': '#2196F3'},  # Green for Female, Blue for Male
                barmode='group'
            )
            
            # Add error bars if requested
            if show_ci:
                # Add error bars manually
                for sex in ['Female', 'Male']:
                    sex_data = filtered_df[filtered_df['Sex'] == sex]
                    fig.add_bar(
                        x=sex_data['Age_Group'],
                        y=sex_data['Rate'],
                        error_y=dict(
                            type='data',
                            symmetric=False,
                            array=sex_data['CI_Upper'] - sex_data['Rate'],
                            arrayminus=sex_data['Rate'] - sex_data['CI_Lower'],
                            visible=True
                        ),
                        showlegend=False,
                        marker_color='rgba(0,0,0,0)',
                        hoverinfo='skip'
                    )
            
        elif display_option == "Gender Ratio (F:M)":
            # Calculate gender ratios
            female_data = filtered_df[filtered_df['Sex'] == 'Female'].set_index('Age_Group')['Rate']
            male_data = filtered_df[filtered_df['Sex'] == 'Male'].set_index('Age_Group')['Rate']
            ratio_data = (female_data / male_data).reset_index()
            ratio_data.columns = ['Age_Group', 'Ratio']
            
            fig = px.bar(
                ratio_data,
                x='Age_Group',
                y='Ratio',
                title=f'Female to Male Hospitalization Ratio by Age - {selected_year}',
                labels={'Ratio': 'Female:Male Ratio', 'Age_Group': 'Age Group'},
                color_discrete_sequence=['#9C27B0']
            )
            
            # Add horizontal line at ratio = 1
            fig.add_hline(y=1, line_dash="dash", line_color="#FF9800", line_width=3)
            
        else:  # Both Sexes Combined
            # Combine sexes using 'Total' category
            total_data = table10_df[
                (table10_df['Year'] == selected_year) & 
                (table10_df['Sex'] == 'Total')
            ].copy()
            
            fig = px.bar(
                total_data,
                x='Age_Group',
                y='Rate',
                title=f'Mental Health Hospitalizations by Age (Both Sexes) - {selected_year}',
                labels={'Rate': 'Rate per 100,000 population', 'Age_Group': 'Age Group'},
                color_discrete_sequence=['#607D8B']
            )
        
        # Update layout
        fig.update_layout(
            xaxis_title='Age Group',
            yaxis_title='Rate per 100,000 population',
            plot_bgcolor='white',
            paper_bgcolor='white',
            font=dict(size=12),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
            height=500
        )
        
        # Add grid lines
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
        
        # Custom hover template
        if display_option == "Absolute Rates":
            hover_template = (
                "<b>%{fullData.name}</b><br>"
                "Age Group: %{x}<br>"
                "Rate: %{y:,.0f} per 100k<br>"
                "<extra></extra>"
            )
            fig.update_traces(hovertemplate=hover_template)
        
        print("✅ Age/gender chart created successfully")
        return fig
        
    except Exception as e:
        print(f"❌ ERROR creating age/gender chart: {str(e)}")
        import traceback
        print(f"🔍 Full error traceback:")
        traceback.print_exc()
        return create_placeholder_chart(f"Error creating chart: {str(e)}")