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
- **Health Equity** - Urban/rural and income disparities (placeholder)
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
- **Gender Differences** - Side-by-side comparison of female (pink) vs male (blue) rates
- **Streamlined Controls** - Simplified interface focusing on essential features

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
│   └── 📄 table_10.json              # Age and gender demographics data (2018-2024)
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
│       ├── 📄 health_equity.py       # Health equity analysis page (placeholder)
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

## 🛠️ Technical Stack

- **Backend**: Python 3.8+
- **Web Framework**: Dash (Plotly)
- **Data Visualization**: Plotly Express & Graph Objects
- **Data Processing**: Pandas, NumPy
- **Styling**: CSS3, Dash Bootstrap Components
- **Version Control**: Git & GitHub



---

*Last updated: July 2025*