"""
Chart helper functions for CIHI Mental Health Dashboard
"""

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
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
def create_urban_rural_disparity_chart(display_mode, show_ci, highlight_gap, show_percentage, table11_df):
    """Create urban vs rural disparity line chart"""
    print(f"🔄 Creating urban/rural chart - mode: {display_mode}, CI: {show_ci}, gap: {highlight_gap}, %: {show_percentage}")
    
    try:
        if table11_df.empty:
            print("❌ Table 11 DataFrame is empty")
            return create_placeholder_chart("Urban vs Rural Analysis - Data not available")
        
        print(f"✅ Table 11 has {len(table11_df)} records")
        
        if display_mode == "Absolute Rates":
            # Create dual-line chart
            fig = go.Figure()
            
            # Get data for each residence type
            urban_data = table11_df[table11_df['Residence_Type'] == 'Urban'].sort_values('Year')
            rural_data = table11_df[table11_df['Residence_Type'] == 'Rural/remote'].sort_values('Year')
            
            # Add Urban line
            fig.add_trace(go.Scatter(
                x=urban_data['Year'],
                y=urban_data['Rate'],
                mode='lines+markers',
                name='Urban',
                line=dict(color='#2196F3', width=3),
                marker=dict(size=8),
                hovertemplate='<b>Urban</b><br>Year: %{x}<br>Rate: %{y:.0f} per 100k<br>95% CI: [%{customdata[0]:.0f}-%{customdata[1]:.0f}]<extra></extra>',
                customdata=urban_data[['CI_Lower', 'CI_Upper']].values
            ))
            
            # Add Rural line
            fig.add_trace(go.Scatter(
                x=rural_data['Year'],
                y=rural_data['Rate'],
                mode='lines+markers',
                name='Rural/Remote',
                line=dict(color='#F44336', width=3),
                marker=dict(size=8),
                hovertemplate='<b>Rural/Remote</b><br>Year: %{x}<br>Rate: %{y:.0f} per 100k<br>95% CI: [%{customdata[0]:.0f}-%{customdata[1]:.0f}]<extra></extra>',
                customdata=rural_data[['CI_Lower', 'CI_Upper']].values
            ))
            
            # Add gap fill if requested
            if highlight_gap:
                fig.add_trace(go.Scatter(
                    x=urban_data['Year'].tolist() + rural_data['Year'].tolist()[::-1],
                    y=urban_data['Rate'].tolist() + rural_data['Rate'].tolist()[::-1],
                    fill='toself',
                    fillcolor='rgba(244, 67, 54, 0.2)',
                    line=dict(color='rgba(255,255,255,0)'),
                    name='Rural-Urban Gap',
                    showlegend=True,
                    hoverinfo='skip'
                ))
            
            # Add confidence intervals if requested
            if show_ci:
                # Urban CI
                fig.add_trace(go.Scatter(
                    x=urban_data['Year'].tolist() + urban_data['Year'].tolist()[::-1],
                    y=urban_data['CI_Upper'].tolist() + urban_data['CI_Lower'].tolist()[::-1],
                    fill='toself',
                    fillcolor='rgba(33, 150, 243, 0.2)',
                    line=dict(color='rgba(255,255,255,0)'),
                    name='Urban 95% CI',
                    showlegend=False,
                    hoverinfo='skip'
                ))
                
                # Rural CI
                fig.add_trace(go.Scatter(
                    x=rural_data['Year'].tolist() + rural_data['Year'].tolist()[::-1],
                    y=rural_data['CI_Upper'].tolist() + rural_data['CI_Lower'].tolist()[::-1],
                    fill='toself',
                    fillcolor='rgba(244, 67, 54, 0.2)',
                    line=dict(color='rgba(255,255,255,0)'),
                    name='Rural 95% CI',
                    showlegend=False,
                    hoverinfo='skip'
                ))
            
            title = 'Urban vs Rural Mental Health Hospitalization Rates'
            y_title = 'Rate per 100,000 population'
            
        elif display_mode == "Ratio View (Rural:Urban)":
            # Calculate ratios
            urban_data = table11_df[table11_df['Residence_Type'] == 'Urban'].sort_values('Year')
            rural_data = table11_df[table11_df['Residence_Type'] == 'Rural/remote'].sort_values('Year')
            
            # Merge data to calculate ratios
            merged = pd.merge(urban_data[['Year', 'Rate']], rural_data[['Year', 'Rate']], on='Year', suffixes=['_Urban', '_Rural'])
            merged['Ratio'] = merged['Rate_Rural'] / merged['Rate_Urban']
            
            fig = go.Figure()
            
            fig.add_trace(go.Scatter(
                x=merged['Year'],
                y=merged['Ratio'],
                mode='lines+markers',
                name='Rural:Urban Ratio',
                line=dict(color='#9C27B0', width=3),
                marker=dict(size=8),
                hovertemplate='<b>Rural:Urban Ratio</b><br>Year: %{x}<br>Ratio: %{y:.2f}<br><extra></extra>'
            ))
            
            # Add reference line at 1.0
            fig.add_hline(y=1, line_dash="dash", line_color="gray", line_width=2)
            
            title = 'Rural to Urban Hospitalization Rate Ratio'
            y_title = 'Rural:Urban Ratio'
            
        else:  # Percentage Above Urban
            # Calculate percentage differences
            urban_data = table11_df[table11_df['Residence_Type'] == 'Urban'].sort_values('Year')
            rural_data = table11_df[table11_df['Residence_Type'] == 'Rural/remote'].sort_values('Year')
            
            merged = pd.merge(urban_data[['Year', 'Rate']], rural_data[['Year', 'Rate']], on='Year', suffixes=['_Urban', '_Rural'])
            merged['Percentage_Diff'] = ((merged['Rate_Rural'] - merged['Rate_Urban']) / merged['Rate_Urban']) * 100
            
            fig = go.Figure()
            
            fig.add_trace(go.Scatter(
                x=merged['Year'],
                y=merged['Percentage_Diff'],
                mode='lines+markers',
                name='Rural Excess (%)',
                line=dict(color='#FF5722', width=3),
                marker=dict(size=8),
                hovertemplate='<b>Rural Excess</b><br>Year: %{x}<br>Percentage: %{y:.1f}%<br><extra></extra>'
            ))
            
            # Add reference line at 0%
            fig.add_hline(y=0, line_dash="dash", line_color="gray", line_width=2)
            
            title = 'Rural Mental Health Hospitalization Excess (% Above Urban)'
            y_title = 'Percentage Above Urban Rate'
        
        # Update layout
        fig.update_layout(
            title=title,
            xaxis_title='Fiscal Year',
            yaxis_title=y_title,
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
            margin=dict(r=150),
            height=500
        )
        
        # Add grid lines
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
        
        print("✅ Urban/rural chart created successfully")
        return fig
        
    except Exception as e:
        print(f"❌ ERROR creating urban/rural chart: {str(e)}")
        import traceback
        print(f"🔍 Full error traceback:")
        traceback.print_exc()
        return create_placeholder_chart(f"Error creating chart: {str(e)}")

def create_income_gradient_chart(display_mode, show_ci, show_ratio, show_shading, table12_df):
    """Create income gradient multi-line chart"""
    print(f"🔄 Creating income gradient chart - mode: {display_mode}, CI: {show_ci}, ratio: {show_ratio}, shading: {show_shading}")
    
    try:
        if table12_df.empty:
            print("❌ Table 12 DataFrame is empty")
            return create_placeholder_chart("Income Gradient Analysis - Data not available")
        
        print(f"✅ Table 12 has {len(table12_df)} records")
        
        # Color mapping for income quintiles (red to green gradient)
        quintile_colors = {
            'Q1': '#E74C3C',  # Red (highest rates, lowest income)
            'Q2': '#FF8C00',  # Orange
            'Q3': '#FFD700',  # Yellow/Gold
            'Q4': '#90EE90',  # Light Green
            'Q5': '#228B22'   # Green (lowest rates, highest income)
        }
        
        if display_mode == "Absolute Rates":
            # Create multi-line chart
            fig = go.Figure()
            
            for quintile in ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']:
                quintile_data = table12_df[table12_df['Income_Quintile'] == quintile].sort_values('Year')
                
                if not quintile_data.empty:
                    # Determine line width - make Q1 and Q5 thicker to emphasize endpoints
                    line_width = 4 if quintile in ['Q1', 'Q5'] else 3
                    
                    fig.add_trace(go.Scatter(
                        x=quintile_data['Year'],
                        y=quintile_data['Rate'],
                        mode='lines+markers',
                        name=f'{quintile} ({"Lowest" if quintile=="Q1" else "Highest" if quintile=="Q5" else "Middle"} Income)',
                        line=dict(color=quintile_colors[quintile], width=line_width),
                        marker=dict(size=8),
                        hovertemplate=f'<b>Income {quintile}</b><br>Year: %{{x}}<br>Rate: %{{y:.0f}} per 100k<br>95% CI: [%{{customdata[0]:.0f}}-%{{customdata[1]:.0f}}]<extra></extra>',
                        customdata=quintile_data[['CI_Lower', 'CI_Upper']].values
                    ))
                    
                    # Add confidence intervals if requested
                    if show_ci:
                        fig.add_trace(go.Scatter(
                            x=quintile_data['Year'].tolist() + quintile_data['Year'].tolist()[::-1],
                            y=quintile_data['CI_Upper'].tolist() + quintile_data['CI_Lower'].tolist()[::-1],
                            fill='toself',
                            fillcolor=f'rgba({int(quintile_colors[quintile][1:3], 16)}, {int(quintile_colors[quintile][3:5], 16)}, {int(quintile_colors[quintile][5:7], 16)}, 0.2)',
                            line=dict(color='rgba(255,255,255,0)'),
                            name=f'{quintile} 95% CI',
                            showlegend=False,
                            hoverinfo='skip'
                        ))
            
            # Add gradient shading between Q1 and Q5 if requested
            if show_shading:
                q1_data = table12_df[table12_df['Income_Quintile'] == 'Q1'].sort_values('Year')
                q5_data = table12_df[table12_df['Income_Quintile'] == 'Q5'].sort_values('Year')
                
                if not q1_data.empty and not q5_data.empty:
                    fig.add_trace(go.Scatter(
                        x=q5_data['Year'].tolist() + q1_data['Year'].tolist()[::-1],
                        y=q5_data['Rate'].tolist() + q1_data['Rate'].tolist()[::-1],
                        fill='toself',
                        fillcolor='rgba(231, 76, 60, 0.15)',
                        line=dict(color='rgba(255,255,255,0)'),
                        name='Income Inequality Gap',
                        showlegend=True,
                        hoverinfo='skip'
                    ))
            
            title = 'Mental Health Hospitalizations by Income Quintile (Canada)'
            y_title = 'Rate per 100,000 population'
            
        elif display_mode == "Relative to Q5":
            # Calculate ratios relative to Q5 (highest income)
            fig = go.Figure()
            
            q5_data = table12_df[table12_df['Income_Quintile'] == 'Q5'].set_index('Year')['Rate']
            
            for quintile in ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']:
                quintile_data = table12_df[table12_df['Income_Quintile'] == quintile].sort_values('Year')
                
                if not quintile_data.empty:
                    # Calculate ratio to Q5
                    quintile_rates = quintile_data.set_index('Year')['Rate']
                    ratios = quintile_rates / q5_data
                    ratio_df = ratios.reset_index()
                    ratio_df.columns = ['Year', 'Ratio']
                    
                    line_width = 4 if quintile in ['Q1', 'Q5'] else 3
                    
                    fig.add_trace(go.Scatter(
                        x=ratio_df['Year'],
                        y=ratio_df['Ratio'],
                        mode='lines+markers',
                        name=f'{quintile} ({"Lowest" if quintile=="Q1" else "Highest" if quintile=="Q5" else "Middle"} Income)',
                        line=dict(color=quintile_colors[quintile], width=line_width),
                        marker=dict(size=8),
                        hovertemplate=f'<b>Income {quintile}</b><br>Year: %{{x}}<br>Ratio to Q5: %{{y:.2f}}x<extra></extra>'
                    ))
            
            # Add reference line at 1.0 (Q5 baseline)
            fig.add_hline(y=1, line_dash="dash", line_color="gray", line_width=2)
            
            title = 'Income Quintile Rates Relative to Q5 (Highest Income)'
            y_title = 'Ratio to Q5 (Highest Income Quintile)'
            
        else:  # Percentage Above National Average
            # Calculate percentage differences from national average
            # First calculate national average across all quintiles (weighted)
            national_avg = table12_df.groupby('Year')['Rate'].mean().reset_index()
            national_avg.columns = ['Year', 'National_Avg']
            
            fig = go.Figure()
            
            for quintile in ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']:
                quintile_data = table12_df[table12_df['Income_Quintile'] == quintile].sort_values('Year')
                
                if not quintile_data.empty:
                    # Merge with national average
                    merged = pd.merge(quintile_data, national_avg, on='Year')
                    merged['Percentage_Diff'] = ((merged['Rate'] - merged['National_Avg']) / merged['National_Avg']) * 100
                    
                    line_width = 4 if quintile in ['Q1', 'Q5'] else 3
                    
                    fig.add_trace(go.Scatter(
                        x=merged['Year'],
                        y=merged['Percentage_Diff'],
                        mode='lines+markers',
                        name=f'{quintile} ({"Lowest" if quintile=="Q1" else "Highest" if quintile=="Q5" else "Middle"} Income)',
                        line=dict(color=quintile_colors[quintile], width=line_width),
                        marker=dict(size=8),
                        hovertemplate=f'<b>Income {quintile}</b><br>Year: %{{x}}<br>% Above/Below Avg: %{{y:.1f}}%<extra></extra>'
                    ))
            
            # Add reference line at 0% (national average)
            fig.add_hline(y=0, line_dash="dash", line_color="gray", line_width=2)
            
            title = 'Income Quintile Rates as % Above/Below National Average'
            y_title = 'Percentage Above/Below National Average'
        
        # Add ratio annotations if requested
        if show_ratio and display_mode == "Absolute Rates":
            # Calculate Q1:Q5 ratios for each year
            q1_data = table12_df[table12_df['Income_Quintile'] == 'Q1'].set_index('Year')['Rate']
            q5_data = table12_df[table12_df['Income_Quintile'] == 'Q5'].set_index('Year')['Rate']
            
            # Add annotation for latest year
            latest_year = q1_data.index[-1]
            latest_ratio = q1_data[latest_year] / q5_data[latest_year]
            
            fig.add_annotation(
                x=latest_year,
                y=q1_data[latest_year],
                text=f"Q1 is {latest_ratio:.1f}x higher than Q5",
                showarrow=True,
                arrowhead=2,
                arrowcolor=quintile_colors['Q1'],
                bgcolor="white",
                bordercolor=quintile_colors['Q1'],
                borderwidth=2
            )
        
        # Update layout
        fig.update_layout(
            title=title,
            xaxis_title='Fiscal Year',
            yaxis_title=y_title,
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
            margin=dict(r=200),
            height=600
        )
        
        # Add grid lines
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
        
        print("✅ Income gradient chart created successfully")
        return fig
        
    except Exception as e:
        print(f"❌ ERROR creating income gradient chart: {str(e)}")
        import traceback
        print(f"🔍 Full error traceback:")
        traceback.print_exc()
        return create_placeholder_chart(f"Error creating chart: {str(e)}")