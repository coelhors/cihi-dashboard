# CIHI Mental Health Dashboard

An interactive web dashboard analyzing the Canadian youth mental health crisis using data from the Canadian Institute for Health Information (CIHI). This is a personal project exploring youth mental health trends and disparities across Canada.

## 🎯 Project Purpose

This dashboard enables users to:
- **Explore trends** in youth mental health hospitalizations across Canada (2018-2024)
- **Identify disparities** by geography, income, and demographics
- **Understand clinical patterns** across different mental health conditions
- **Develop actionable recommendations** for policy and intervention strategies

The interactive visualizations guide users through a comprehensive analysis, from broad provincial trends to specific clinical diagnostic patterns, ultimately empowering evidence-based decision making in youth mental health.

## 📊 Current Features

### 🏠 Multi-Page Navigation
- **Provincial Overview** - Interactive provincial trends and comparison charts
- **Demographics** - Age and gender analysis with interactive year selection
- **Health Equity** - Urban/rural disparity and income gradient analysis
- **Clinical Patterns** - Diagnostic pattern analysis (placeholder)

### 📈 Interactive Visualizations

#### **Visual Element 1: Provincial Hospitalization Trends**
- **Multi-province comparison** with line chart visualization
- **Province Selection** - Multi-select dropdown for comparing 2-4 provinces
- **Metric Toggle** - Switch between rates per 100,000 and absolute case numbers
- **Default Selection** - Alberta (configurable)
- **Real-time Updates** - Chart updates based on user selections

#### **Visual Element 2: Mental Health vs Other Conditions**
- **Stacked area chart** comparing mental health and other medical conditions
- **Province Selection** - Single-select dropdown (default: Canada)
- **Metric Toggle** - Switch between rates per 100,000 and absolute numbers
- **Visual Layers** - Mental health (red), other conditions (blue), total line (gray)
- **Interactive Tooltips** - Show detailed breakdown with percentages
- **Data Integration** - Combines Table 3 and Table 4 datasets

#### **Visual Element 3: Provincial Contribution Analysis**
- **Interactive pie chart** showing each province's share of total hospitalizations
- **Year Selection** - Dropdown to explore contributions across 2018-2024
- **Metric Toggle** - Switch between absolute cases and rates per 100,000
- **Visual Emphasis** - Alberta slice highlighted with pull-out effect
- **Rich Tooltips** - Province details with cases, rates, and percentages
- **Colorblind-friendly** - Distinct colors for all provinces/territories

#### **Visual Element 4: Age and Gender Demographics**
- **Interactive grouped bar chart** showing hospitalization rates by age and gender
- **Year Selection** - Dropdown to explore patterns across 2018-2024
- **Display Modes** - Switch between absolute rates and female-to-male ratios
- **Age Progression** - Clear visualization of increasing rates from childhood to adolescence
- **Gender Differences** - Side-by-side comparison of female (green) vs male (blue) rates
- **Non-stereotypical Colors** - Green for females, blue for males

#### **Visual Element 5: Urban vs Rural Health Equity**
- **Static dual-line disparity chart** showing persistent rural disadvantage in mental health
- **Gap Visualization** - Highlighted area between lines showing equity disparity
- **Clean Interface** - Streamlined presentation focusing on core equity insights
- **Equity Insights** - Rural youth consistently 20-30% higher hospitalization rates
- **Temporal Analysis** - Shows disparity persistence even through COVID disruption

#### **Visual Element 6: Income Gradient Analysis**
- **Multi-line chart** showing mental health hospitalization rates across income quintiles (Q1-Q5)
- **Color Gradient** - Red (Q1, lowest income, highest rates) to green (Q5, highest income, lowest rates)
- **Static Display** - Clean presentation focusing on absolute rates for clear teaching demonstration
- **Emphasized Lines** - Q1 and Q5 lines are thicker to highlight income inequality endpoints
- **Socioeconomic Insights** - Clear visualization of income inequality in mental health outcomes
- **Teaching Focus** - Shows persistent income gradient with Q1 consistently higher rates than Q5

## 📁 Project Structure

```
cihi-dashboard/
├── 📄 app.py                          # Main application entry point (modular, clean)
├── 📄 requirements.txt                # Python dependencies (dash, plotly, pandas)
├── 📄 README.md                       # Project documentation (this file)
├── 📄 dashboard_overview.md           # Detailed visualization specifications
├── 📄 .gitignore                      # Git ignore rules
│
├── 📂 assets/                         # Static files and styling
│   └── 📄 style.css                  # Basic CSS styling for dashboard
├── 📂 data/                           # Raw data files (JSON format)
│   ├── 📄 table_03.json              # Provincial mental health hospitalization data (2018-2024)
│   ├── 📄 table_04.json              # Provincial other conditions hospitalization data (2018-2024)
│   ├── 📄 table_10.json              # Age and gender demographics data (2018-2024)
│   ├── 📄 table_11.json              # Urban vs rural residence data (2018-2024)
│   └── 📄 table_12.json              # Income quintile data (2018-2024)
├── 📂 utils/                          # Utility functions and configuration
│   ├── 📄 __init__.py                # Package initialization
│   ├── 📄 config.py                  # Colors, styles, constants, and configuration
│   ├── 📄 data_loader.py             # Data loading, processing, and merging functions
│   └── 📄 chart_helpers.py           # Chart creation and visualization functions
├── 📂 components/                     # UI components and page layouts
│   ├── 📄 __init__.py                # Package initialization
│   ├── 📄 sidebar.py                 # Navigation sidebar component
│   └── 📂 pages/                     # Individual page modules
│       ├── 📄 __init__.py            # Package initialization
│       ├── 📄 provincial_overview.py # Provincial trends and comparison charts (3 working visualizations)
│       ├── 📄 demographics.py        # Age and gender demographics analysis (1 working visualization)
│       ├── 📄 health_equity.py       # Urban/rural and income disparity analysis (2 working visualizations)
│       └── 📄 clinical_patterns.py   # Clinical patterns page (placeholder)
└── 📂 docs/                           # Documentation and methodology - empty
```

## 📚 Data Source

**Canadian Institute for Health Information (CIHI)**  
*Care for Children and Youth With Mental Disorders (2018-2024)*

**Dataset Download**: [CIHI Mental Health Data Tables](https://www.cihi.ca/sites/default/files/document/care-children-youth-with-mental-disorders-data-tables-en.xlsx)

## 🎓 Educational Value

This dashboard demonstrates:
1. **Data visualization** best practices for health analytics
2. **Interactive design** principles for exploratory data analysis
3. **Health equity analysis** methods and interpretation
4. **Evidence-based insights** for public health decision making
5. **Full-stack development** with Python and modern web technologies
6. **Socioeconomic health disparities** visualization and analysis

## 🛠️ Technical Stack

- **Backend**: Python 3.8+
- **Web Framework**: Dash (Plotly)
- **Data Visualization**: Plotly Express & Graph Objects
- **Data Processing**: Pandas, NumPy
- **Styling**: CSS3, Dash Bootstrap Components
- **Version Control**: Git & GitHub

## 📈 Implementation Status

**Current Progress: 6/8 Visualizations Complete (75%)**

### ✅ **Completed Visualizations**
- **Provincial Overview Page**: 3 visualizations
  - Provincial Hospitalization Trends
  - Mental Health vs Other Conditions
  - Provincial Contribution Analysis
- **Demographics Page**: 1 visualization
  - Age and Gender Patterns
- **Health Equity Page**: 2 visualizations
  - Urban vs Rural Disparities
  - Income Gradient Analysis

### ⏳ **Remaining Visualizations**
- **Health Equity Page**: 1 remaining
  - Income Quintile Contributions (pie chart)
- **Clinical Patterns Page**: 1 remaining
  - Clinical Diagnostic Heat Map

---

*Last updated: July 2025*