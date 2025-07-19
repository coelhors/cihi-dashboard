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
- **Provincial Overview** - Interactive provincial hospitalization trends line chart
- **Demographics** - Age and gender analysis (placeholder)
- **Health Equity** - Urban/rural and income disparities (placeholder)
- **Clinical Patterns** - Diagnostic pattern analysis (placeholder)

### 📈 Interactive Visualizations
- **Provincial Trends Chart** - Multi-province comparison with metric toggle
- **Province Selection** - Multi-select dropdown for comparing 2-4 provinces
- **Metric Toggle** - Switch between rates per 100,000 and absolute case numbers
- **Real-time Updates** - Chart updates based on user selections

## 📁 Project Structure

```
cihi-mental-health-dashboard/
├── 📄 app.py                          # Main Dash application (multi-page with working provincial chart)
├── 📄 requirements.txt                # Python dependencies (dash, plotly, pandas)
├── 📄 README.md                       # Project documentation (this file)
├── 📄 dashboard_overview.md           # Detailed visualization specifications
├── 📄 .gitignore                      # Git ignore rules
│
├── 📂 assets/                         # Static files and styling
│   └── 📄 style.css                  # Basic CSS styling for dashboard
├── 📂 data/                           # Raw data files (JSON format)
│   └── 📄 table_03.json              # Provincial hospitalization data (2018-2024)
├── 📂 components/                     # Dashboard visualization components - empty
├── 📂 utils/                          # Helper functions and data processing - empty
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