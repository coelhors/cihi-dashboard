"""
Chart helper functions for CIHI Mental Health Dashboard
"""

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
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
def create_income_quintile_contribution_pie(selected_year, table12_df):
    """Create simplified income quintile contribution pie chart"""
    print(f"🔄 Creating income quintile contribution pie chart for year: {selected_year}")
    
    try:
        if table12_df.empty:
            print("❌ Table 12 DataFrame is empty")
            return create_placeholder_chart("Income Quintile Contributions - Data not available")
        
        # Filter data for selected year
        filtered_df = table12_df[table12_df['Year'] == selected_year].copy()
        
        print(f"🔍 Filtered to {len(filtered_df)} quintiles for year {selected_year}")
        
        if filtered_df.empty:
            print("❌ No data after filtering")
            return create_placeholder_chart(f"No income quintile data available for {selected_year}")
        
        # Color mapping consistent with Visual Element 6
        quintile_colors = {
            'Q1': '#E74C3C',  # Red (highest rates)
            'Q2': '#FF8C00',  # Orange
            'Q3': '#FFD700',  # Yellow/Gold
            'Q4': '#90EE90',  # Light Green
            'Q5': '#228B22'   # Green (lowest rates)
        }
        
        # Create color list in correct order
        colors = [quintile_colors[q] for q in filtered_df['Income_Quintile']]
        
        # Always use Rate per 100,000 as values
        values = filtered_df['Rate']
        title_suffix = 'by Rate per 100,000'
        hover_template = (
            "<b>%{label}</b><br>"
            f"Year: {selected_year}<br>"
            "Rate per 100k: %{value:.0f}<br>"
            "Percentage: %{percent}"
            "<extra></extra>"
        )
        
        # Create quintile labels with more expressive names
        quintile_labels = []
        for q in filtered_df['Income_Quintile']:
            if q == 'Q1':
                quintile_labels.append('Q1 (Lowest Income)')
            elif q == 'Q2':
                quintile_labels.append('Q2 (Lower-Middle Income)')
            elif q == 'Q3':
                quintile_labels.append('Q3 (Middle Income)')
            elif q == 'Q4':
                quintile_labels.append('Q4 (Upper-Middle Income)')
            elif q == 'Q5':
                quintile_labels.append('Q5 (Highest Income)')
            else:
                quintile_labels.append(f'{q}')  # fallback
        
        # Create pie chart
        fig = px.pie(
            values=values,
            names=quintile_labels,
            title=f'Income Quintile Mental Health Hospitalization Contributions - {selected_year}<br><sub>{title_suffix}</sub>',
            color_discrete_sequence=colors
        )
        
        # Customize the pie chart
        fig.update_traces(
            textposition='inside',
            textinfo='percent+label',
            hovertemplate=hover_template
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
            margin=dict(r=200, l=50, t=100, b=50),
            showlegend=True,
            height=600,
            width=1000
        )
        
        print("✅ Income quintile contribution pie chart created successfully")
        return fig
        
    except Exception as e:
        print(f"❌ ERROR creating income quintile contribution pie chart: {str(e)}")
        import traceback
        print(f"🔍 Full error traceback:")
        traceback.print_exc()
def create_clinical_diagnostic_heatmap(selected_year, selected_sex, selected_diagnoses, color_scale, table13_df):
    """Create clinical diagnostic patterns heat map"""
    print(f"🔄 Creating clinical diagnostic heatmap for year: {selected_year}, sex: {selected_sex}, scale: {color_scale}")
    
    try:
        if table13_df.empty:
            print("❌ Table 13 DataFrame is empty")
            return create_placeholder_chart("Clinical Diagnostic Patterns - Data not available")
        
        # Filter data for selected year, sex, and diagnoses
        filtered_df = table13_df[
            (table13_df['Year'] == selected_year) & 
            (table13_df['Sex'] == selected_sex) &
            (table13_df['Diagnosis'].isin(selected_diagnoses)) &
            (table13_df['Age_Group'] != '5-24')  # Exclude total age group for cleaner heat map
        ].copy()
        
        print(f"🔍 Filtered to {len(filtered_df)} records")
        
        if filtered_df.empty:
            print("❌ No data after filtering")
            return create_placeholder_chart(f"No clinical data available for {selected_year}, {selected_sex}")
        
        # Create pivot table for heat map
        heatmap_data = filtered_df.pivot(index='Diagnosis', columns='Age_Group', values='Rate')
        
        # Ensure consistent column order
        age_order = ['5-9', '10-14', '15-17', '18-24']
        heatmap_data = heatmap_data.reindex(columns=age_order)
        
        # Apply color scale transformation if needed
        display_values = heatmap_data.copy()
        if color_scale == "Log Scale":
            # Add small value to avoid log(0)
            display_values = np.log(heatmap_data + 1)
            scale_title = "Log(Rate + 1)"
        elif color_scale == "Percentile Ranking":
            # Convert to percentile rankings
            display_values = heatmap_data.rank(pct=True) * 100
            scale_title = "Percentile Rank"
        elif color_scale == "Z-Score Normalization":
            # Standardize across all values
            flat_values = heatmap_data.values.flatten()
            flat_values = flat_values[~np.isnan(flat_values)]
            mean_val = np.mean(flat_values)
            std_val = np.std(flat_values)
            display_values = (heatmap_data - mean_val) / std_val
            scale_title = "Z-Score"
        else:  # Linear Scale
            scale_title = "Rate per 100,000"
        
        # Create custom color scale
        if color_scale == "Z-Score Normalization":
            colorscale = 'RdBu_r'  # Diverging scale for z-scores
        else:
            colorscale = [[0, '#E3F2FD'],    # Light blue (low)
                         [0.2, '#81D4FA'],   # Blue
                         [0.4, '#FFF59D'],   # Yellow
                         [0.6, '#FFB74D'],   # Orange
                         [0.8, '#FF7043'],   # Red-orange
                         [1.0, '#D32F2F']]   # Dark red (high)
        
        # Create heat map
        fig = go.Figure(data=go.Heatmap(
            z=display_values.values,
            x=display_values.columns,
            y=display_values.index,
            colorscale=colorscale,
            hovertemplate='<b>%{y}</b><br>' +
                         'Age Group: %{x}<br>' +
                         f'Sex: {selected_sex}<br>' +
                         'Rate: %{customdata:.0f} per 100k<br>' +
                         '<extra></extra>',
            customdata=heatmap_data.values,  # Use original values for hover
            colorbar=dict(
                title=scale_title,
                thickness=15,
                len=0.9
            )
        ))
        
        # Add text annotations with actual rates
        annotations = []
        for i, diagnosis in enumerate(display_values.index):
            for j, age_group in enumerate(display_values.columns):
                rate = heatmap_data.iloc[i, j]
                if not pd.isna(rate):
                    # Choose text color based on background intensity
                    text_color = 'white' if rate > 150 else 'black'
                    annotations.append(
                        dict(
                            x=age_group,
                            y=diagnosis,
                            text=f'{rate:.0f}',
                            showarrow=False,
                            font=dict(color=text_color, size=11, family="Arial Black")
                        )
                    )
        
        # Update layout
        fig.update_layout(
            title=f'Clinical Diagnostic Patterns by Age Group - {selected_sex}, {selected_year}<br><sub>Mental Health Hospitalization Rates per 100,000</sub>',
            xaxis_title='Age Group',
            yaxis_title='Diagnosis Category',
            font=dict(size=12),
            height=600,
            width=900,
            annotations=annotations,
            plot_bgcolor='white',
            paper_bgcolor='white'
        )
        
        # Style axes
        fig.update_xaxes(side='bottom')
        fig.update_yaxes(tickmode='linear')
        
        print("✅ Clinical diagnostic heatmap created successfully")
        return fig
        
    except Exception as e:
        print(f"❌ ERROR creating clinical diagnostic heatmap: {str(e)}")
        import traceback
        print(f"🔍 Full error traceback:")
        traceback.print_exc()
        return create_placeholder_chart(f"Error creating heatmap: {str(e)}")

def create_income_gradient_chart(table12_df):
    """Create simplified income gradient multi-line chart"""
    print(f"🔄 Creating simplified income gradient chart")
    
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
        
        # Create multi-line chart (always absolute rates)
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
                    hovertemplate=f'<b>Income {quintile}</b><br>Year: %{{x}}<br>Rate: %{{y:.0f}} per 100k<extra></extra>'
                ))
        
        # Update layout
        fig.update_layout(
            title='Mental Health Hospitalizations by Income Quintile (Canada)',
            xaxis_title='Fiscal Year',
            yaxis_title='Rate per 100,000 population',
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