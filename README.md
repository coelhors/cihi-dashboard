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
- **Modern Sidebar** - Professional gradient design with enhanced navigation styling
- **Provincial Overview** - Interactive provincial trends and comparison charts
- **Demographics** - Age and gender analysis with interactive year selection
- **Health Equity** - Urban/rural disparity and income gradient analysis
- **Clinical Patterns** - Diagnostic pattern analysis with interactive heat map
- **Intuitive Navigation** - Large icons (18px), improved spacing, and clear active states

### 📈 Interactive Visualizations

This dashboard features 8 comprehensive interactive visualizations across 4 pages, providing deep insights into Canadian youth mental health trends and disparities.

#### **Visual Element 1: Provincial Hospitalization Trends**
- **Multi-province comparison** with line chart visualization
- **Province Selection** - Multi-select checklist for easy province comparison (2-4 provinces recommended)
- **Fixed Metric** - Rate per 100,000 population (most appropriate for cross-provincial comparison)
- **Default Selection** - Alberta (configurable)
- **Real-time Updates** - Chart updates based on province selections
- **Enhanced UX** - All provinces visible at once, no dropdown required

#### **Visual Element 2: Mental Health vs Other Conditions**
- **Stacked area chart** comparing mental health and other medical conditions
- **Province Selection** - Radio items for single province selection (default: Canada)
- **Fixed Metric** - Rate per 100,000 population for consistent comparison
- **Visual Layers** - Mental health (red), other conditions (blue), total line (gray)
- **Interactive Tooltips** - Show detailed breakdown with percentages
- **Data Integration** - Combines Table 3 and Table 4 datasets
- **Simplified Interface** - Clean single-control design for teaching demonstrations

#### **Visual Element 3: Provincial Contribution Analysis**
- **Interactive pie chart** showing each province's share of total hospitalizations
- **Year Selection** - Radio items to explore contributions across 2018-2024 (enhanced visibility)
- **Fixed Metric** - Rate per 100,000 population for meaningful cross-provincial comparison
- **Visual Emphasis** - Alberta slice highlighted with pull-out effect
- **Rich Tooltips** - Province details with cases, rates, and percentages
- **Colorblind-friendly** - Distinct colors for all provinces/territories
- **Compact Control** - Optimized 25% width for efficient space utilization
- **Simplified Interface** - Clean single-control design consistent with other visualizations

#### **Visual Element 4: Age and Gender Demographics**
- **Interactive grouped bar chart** showing hospitalization rates by age and gender
- **Year Selection** - Radio items to explore patterns across 2018-2024 (enhanced from dropdown)
- **Display Modes** - Switch between absolute rates and female-to-male ratios
- **Age Progression** - Clear visualization of increasing rates from childhood to adolescence
- **Gender Differences** - Side-by-side comparison of female (green) vs male (blue) rates
- **Non-stereotypical Colors** - Green for females, blue for males
- **Enhanced Layout** - Horizontal control arrangement with styled background boxes

#### **Visual Element 5: Urban vs Rural Health Equity**
- **Static dual-line disparity chart** showing persistent rural disadvantage in mental health
- **Purple Gap Visualization** - Highlighted purple area between lines showing equity disparity
- **Clean Interface** - Streamlined presentation focusing on core equity insights
- **Equity Insights** - Rural youth consistently 20-30% higher hospitalization rates
- **Temporal Analysis** - Shows disparity persistence even through COVID disruption

#### **Visual Element 6: Income Gradient Analysis**
- **Multi-line chart** showing mental health hospitalization rates across income quintiles (Q1-Q5)
- **Color Gradient** - Red (Q1, lowest income, highest rates) to green (Q5, highest income, lowest rates)
- **Descriptive Legend** - Clear income level descriptions (Q1 Lowest Income, Q2 Lower-Middle Income, etc.)
- **Static Display** - Clean presentation focusing on absolute rates for clear teaching demonstration
- **Emphasized Lines** - Q1 and Q5 lines are thicker to highlight income inequality endpoints
- **Socioeconomic Insights** - Clear visualization of income inequality in mental health outcomes
- **Teaching Focus** - Shows persistent income gradient with Q1 consistently higher rates than Q5

#### **Visual Element 7: Income Quintile Contributions**
- **Interactive donut chart** showing how different income quintiles contribute to mental health hospitalization burden
- **Year Selection** - Radio items to explore contributions across 2018-2024 (enhanced from dropdown)
- **Professional Design** - Clean donut chart with 40% center hole showing fiscal year
- **Rate-Based Analysis** - Shows proportional contributions based on rates per 100,000 population
- **Expressive Labels** - Clear income hierarchy from Q1 (Lowest Income) to Q5 (Highest Income)
- **Consistent Design** - Same red-to-green color gradient as Visual Element 6
- **Health Equity Focus** - Visualizes disproportionate burden on lower-income populations
- **Enhanced Control** - Styled 25% width control box with professional appearance

#### **Visual Element 8: Clinical Diagnostic Patterns**
- **Interactive heat map** showing mental health hospitalization rates by diagnosis, age group, and gender
- **Horizontal Control Layout** - Sex, Year, and Diagnosis controls arranged side-by-side for better space utilization
- **Sex Selection** - Radio buttons to toggle between Female, Male, and Both Combined
- **Year Selection** - Radio buttons to explore patterns across 2021-2024 fiscal years
- **Diagnosis Filter** - Multi-select checklist for 6 core diagnostic categories
- **Linear Color Scale** - Blue-to-red gradient showing rate intensity with text annotations
- **Clinical Focus** - Excludes Other disorders for cleaner focus on main diagnostic categories
- **Optimized Layout** - Compact horizontal arrangement (22%, 22%, 32% width distribution)
- **Professional UI** - Styled control boxes with consistent visual design

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
│   ├── 📄 table_12.json              # Income quintile data (2018-2024)
│   ├── 📄 table_13-2021-2022.json    # Clinical diagnostic patterns data (2021-2022)
│   ├── 📄 table_13-2022-2023.json    # Clinical diagnostic patterns data (2022-2023)
│   └── 📄 table_13-2023-2024.json    # Clinical diagnostic patterns data (2023-2024)
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
│       ├── 📄 health_equity.py       # Urban/rural and income disparity analysis (3 working visualizations)
│       └── 📄 clinical_patterns.py   # Clinical diagnostic patterns analysis (1 working visualization)
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
7. **User interface optimization** for teaching and demonstration purposes
8. **Professional data presentation** with enhanced readability and accessibility
9. **Modern navigation design** with intuitive sidebar and clear visual hierarchy

## 🛠️ Technical Stack

- **Backend**: Python 3.8+
- **Web Framework**: Dash (Plotly)
- **Data Visualization**: Plotly Express & Graph Objects
- **Data Processing**: Pandas, NumPy
- **Styling**: CSS3, Dash Bootstrap Components
- **Version Control**: Git & GitHub

## 🎨 Design Philosophy

### **Modern Professional Interface**
- **Enhanced Sidebar Design** - Modern gradient background with professional styling and improved visual hierarchy
- **Simplified Controls** - Reduced cognitive load with streamlined options
- **Radio Items Standardization** - Consistent use of radio items for single selection across all pages
- **Horizontal Layouts** - Better space utilization and professional appearance
- **Fixed Metrics** - Rate per 100,000 as standard for meaningful comparisons
- **Visual Consistency** - Styled control boxes with unified design language
- **Alberta Emphasis** - Strategic highlighting for local teaching context

### **Enhanced User Experience**
- **Modern Navigation** - Professional sidebar with gradient background, larger icons (18px), and improved spacing
- **Active State Clarity** - White backgrounds with gold borders for active navigation items
- **Checklist over Dropdowns** - All options visible for better province selection
- **Radio Items for Single Selection** - Clear single-choice interactions across Demographics and Health Equity
- **Compact Control Arrangements** - Optimized width distributions (22%, 25%, 32%, 45%)
- **Professional Styling** - Background boxes, borders, and consistent spacing throughout
- **Teaching Demo Ready** - Clean interfaces ideal for classroom presentations
- **Larger Legends** - 14px font size across all charts for better readability

### **Visual Enhancements**
- **Professional Sidebar** - 280px width with modern gradient background and enhanced navigation styling
- **Purple Gap Highlighting** - Improved color choice for urban/rural disparity visualization
- **Descriptive Income Labels** - Clear income level descriptions in legends and labels
- **Donut Chart Implementation** - Professional proportional visualization for income contributions
- **Consistent Color Schemes** - Red-to-green gradient maintained across income-related visualizations
- **Enhanced Readability** - Larger legends, improved text sizing, and better navigation contrast
- **Clean Navigation** - Distraction-free sidebar design with focus on functionality

---

*Last updated: July 2025*