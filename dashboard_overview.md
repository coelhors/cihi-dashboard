# Mental Health Dashboard - Visual Element Choices

## Dashboard Overview
**Topic**: Canadian Youth Mental Health Crisis Data Analysis  
**Data Source**: CIHI Mental Health Tables (2018-2024)  
**Teaching Demo Duration**: 30 minutes  
**Implementation**: Python/Plotly/Dash  

---

## Visual Element 1: Provincial Hospitalization Trends

### **Data Source**
- **Table**: Table 3 - Children and youth hospitalized for mental disorders, by province/territory, 2018–2019 to 2023–2024
- **Metrics**: N (number of cases) and Rate per 100,000 population
- **Geographic Coverage**: All 13 provinces/territories
- **Time Period**: 6 fiscal years (2018-19 to 2023-24)

### **Visualization Choice: Interactive Line Chart with Province Selection**

#### **Chart Specifications**
- **Chart Type**: `plotly.express.line`
- **X-axis**: Fiscal years ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24"]
- **Y-axis**: Rate per 100,000 population (range: ~200-1,400, auto-scaling)
- **Color**: Different provinces/territories (distinct colors for each selected line)
- **Line Style**: Solid lines with markers at data points

#### **Interactive Controls**
1. **Province Selector**:
   - **Type**: Multi-select dropdown (`dcc.Dropdown` with `multi=True`)
   - **Options**: All 13 provinces/territories + "Canada" total
   - **Default Selection**: ["Canada", "Ontario", "Alberta"] 
   - **Purpose**: Allow comparison of 2-4 provinces simultaneously

2. **Metric Toggle**:
   - **Type**: Radio buttons (`dcc.RadioItems`)
   - **Options**: ["Rate per 100,000", "Number of Cases (N)"]
   - **Default**: "Rate per 100,000"
   - **Purpose**: Switch between population-adjusted rates and absolute numbers

#### **Visual Features**
- **Hover Tooltip**: 
  - Template: "{Province}<br>Year: {year}<br>Rate: {rate} per 100k<br>Cases: {N}<br>Change from previous year: {change}%"
- **Legend**: Interactive legend allowing users to click to show/hide specific provinces
- **Grid Lines**: Light gray horizontal grid lines for easier reading
- **Annotations**: Option to highlight COVID period (2020-21 to 2021-22) with background shading

#### **Teaching Purpose**
- **Primary Insight**: Show COVID impact on mental health hospitalizations across Canada
- **Secondary Insights**: 
  - Provincial variation in hospitalization rates
  - Recovery patterns post-COVID
  - Identification of high-burden provinces/territories
- **Student Discovery**: Let students explore which provinces were most affected by COVID and which have highest baseline rates

---

## Visual Element 2: Mental Health vs Other Conditions Hospitalization Comparison

### **Data Source**
- **Tables**: 
  - Table 3 - Children and youth hospitalized for mental disorders, by province/territory, 2018–2019 to 2023–2024
  - Table 4 - Children and youth hospitalized for other conditions, by province/territory, 2018–2019 to 2023–2024
- **Metrics**: N (number of cases) and Rate per 100,000 population for both mental health and other conditions
- **Geographic Coverage**: All 13 provinces/territories
- **Time Period**: 6 fiscal years (2018-19 to 2023-24)

### **Visualization Choice: Modified Stacked Area Chart**

#### **Chart Specifications**
- **Chart Type**: `plotly.express.area` or `plotly.graph_objects.Figure` with area traces
- **X-axis**: Fiscal years ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24"]
- **Y-axis**: Hospitalization values (auto-scaling based on metric selection)
- **Areas**: Three components:
  1. **Mental Health Hospitalizations** (bottom layer - red color)
  2. **Other Conditions Hospitalizations** (middle layer - blue color)
  3. **Total Hospitalizations** (top boundary line - sum of both)

#### **Interactive Controls**
1. **Province Selector**:
   - **Type**: Single-select dropdown (`dcc.Dropdown`)
   - **Options**: All 13 provinces/territories + "Canada" total
   - **Default Selection**: "Canada"
   - **Purpose**: Show one province at a time for clear comparison

2. **Metric Toggle**:
   - **Type**: Radio buttons (`dcc.RadioItems`)
   - **Options**: ["Rate per 100,000", "Number of Cases (N)"]
   - **Default**: "Rate per 100,000"
   - **Purpose**: Switch between population-adjusted rates and absolute numbers

#### **Visual Features**
- **Fill Areas**: Semi-transparent stacked areas showing mental health vs other conditions
- **Hover Tooltip**: 
  - Template: "{Province}<br>Year: {year}<br>Mental Health: {mh_value}<br>Other Conditions: {other_value}<br>Total: {total_value}<br>MH as % of Total: {mh_percentage}%"
- **Legend**: Interactive legend to highlight different hospitalization types
- **Colors**: 
  - Mental Health: Red/Orange tones
  - Other Conditions: Blue tones
  - Total boundary: Dark gray line

#### **Teaching Purpose**
- **Primary Insight**: Show relative burden of mental health vs other conditions hospitalizations
- **Secondary Insights**: 
  - Mental health represents ~1/4 to 1/10 of total youth hospitalizations
  - Both condition types showed COVID impact but different recovery patterns
  - Provincial variation in mental health hospitalization ratios
- **Student Discovery**: Let students explore how mental health burden compares to other conditions and varies by province

---

## Visual Element 3: Provincial Contribution to Mental Health Hospitalizations

### **Data Source**
- **Table**: Table 3 - Children and youth hospitalized for mental disorders, by province/territory, 2018–2019 to 2023–2024
- **Metrics**: N (number of cases) and Rate per 100,000 population
- **Geographic Coverage**: 12 provinces/territories (excluding "Canada" total)
- **Time Period**: User-selected fiscal year from 6 available years

### **Visualization Choice: Provincial Contribution Pie Chart**

#### **Chart Specifications**
- **Chart Type**: `plotly.express.pie`
- **Values**: Mental health hospitalizations for selected fiscal year
- **Labels**: Province/territory names
- **Size**: Proportional to each province's contribution to national total

#### **Interactive Controls**
1. **Fiscal Year Selector**:
   - **Type**: Dropdown (`dcc.Dropdown`)
   - **Options**: ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24"]
   - **Default Selection**: "2023-24" (most recent year)
   - **Purpose**: Allow exploration of how provincial contributions changed over time

2. **Metric Choice**:
   - **Type**: Radio buttons (`dcc.RadioItems`)
   - **Options**: ["Number of Cases (N)", "Rate per 100,000"]
   - **Default**: "Number of Cases (N)"
   - **Purpose**: Show absolute contribution vs per-capita burden

#### **Visual Features**
- **Slice Colors**: Distinct color for each province using colorblind-friendly palette
- **Hover Tooltip**: 
  - Template: "{Province}<br>Year: {year}<br>Cases: {value}<br>Percentage of Canada: {percentage}%<br>Rate per 100k: {rate}"
- **Slice Labels**: Show province abbreviations and percentages on larger slices
- **Pull-out Effect**: Optional highlighting of largest contributors (Ontario, Quebec)
- **Legend**: Province names with color coding, positioned to the side

#### **Teaching Purpose**
- **Primary Insight**: Visualize which provinces contribute most to Canada's youth mental health hospitalization burden
- **Secondary Insights**: 
  - Population size vs per-capita burden comparison
  - Changes in provincial contributions over time
  - Identification of provinces with disproportionate burden relative to population
- **Student Discovery**: Let students explore how COVID years affected different provinces' contributions and whether large provinces dominate due to population or higher rates

---

## Visual Element 4: Age and Gender Patterns in Mental Health Hospitalizations

### **Data Source**
- **Table**: Table 10 - Children and youth hospitalized for mental disorders, by age group and sex, Canada, 2018–2019 to 2023–2024
- **Metrics**: Rate per 100,000 population with 95% confidence intervals
- **Geographic Coverage**: Canada (national aggregate)
- **Demographics**: 4 age groups × 2 sexes × 6 fiscal years
- **Age Groups**: 5-9, 10-14, 15-17, 18-24 years

### **Visualization Choice: Grouped Bar Chart with Animation**

#### **Chart Specifications**
- **Chart Type**: `plotly.express.bar` with grouped bars and animation
- **X-axis**: Age groups ["5-9", "10-14", "15-17", "18-24"]
- **Y-axis**: Rate per 100,000 population (range: 0-1,300, auto-scaling)
- **Color**: Sex categories (Female=pink/red, Male=blue)
- **Animation**: Fiscal year progression (2018-19 to 2023-24)
- **Grouping**: Side-by-side bars for Female/Male within each age group

#### **Interactive Controls**
1. **Year Animation Slider**:
   - **Type**: Slider with play/pause button (`dcc.Slider` with animation)
   - **Range**: 2018-19 to 2023-24
   - **Default**: Start at 2018-19
   - **Features**: Auto-play option and manual year selection

2. **Confidence Intervals Toggle**:
   - **Type**: Checkbox (`dcc.Checklist`)
   - **Options**: ["Show Confidence Intervals"]
   - **Default**: Unchecked (for cleaner initial view)
   - **Purpose**: Add error bars showing 95% CI from Table 10

3. **Display Options**:
   - **Type**: Radio buttons (`dcc.RadioItems`)
   - **Options**: ["Absolute Rates", "Gender Ratio (F:M)", "Both Sexes Combined"]
   - **Default**: "Absolute Rates"
   - **Purpose**: Different analytical perspectives

#### **Visual Features**
- **Bar Styling**: Grouped bars with slight transparency, distinct colors for gender
- **Error Bars**: Optional 95% confidence intervals as specified in Table 10
- **Hover Tooltip**: 
  - Template: "Age {age}<br>Sex: {sex}<br>Year: {year}<br>Rate: {rate} per 100k<br>95% CI: [{ci_lower}-{ci_upper}]<br>Gender Ratio: {ratio}"
- **Animation Speed**: 1-second transitions between years
- **Annotations**: Optional year display and key insights (e.g., "COVID Impact Year")

#### **Teaching Purpose**
- **Primary Insight**: Demonstrate dramatic age progression in mental health hospitalization rates
- **Secondary Insights**: 
  - Gender differences across age groups (females consistently higher)
  - COVID impact varied significantly by age and gender
  - Adolescent females (15-17) represent highest-risk group
  - Young adults (18-24) maintain high rates
- **Student Discovery**: Let students animate through years to see COVID impact patterns and explore how gender gaps change with age

---

## Visual Element 5: Urban vs Rural/Remote Mental Health Hospitalization Disparity

### **Data Source**
- **Table**: Table 11 - Children and youth hospitalized for mental disorders, by urban versus rural/remote residence, Canada, 2018–2019 to 2023–2024
- **Metrics**: Rate per 100,000 population with 95% confidence intervals
- **Geographic Coverage**: Canada (national aggregate)
- **Demographics**: Urban vs Rural/Remote residence classification
- **Time Period**: 6 fiscal years (2018-19 to 2023-24)

### **Visualization Choice: Dual-Line Chart with Gap Highlighting**

#### **Chart Specifications**
- **Chart Type**: `plotly.express.line` with filled area between lines
- **X-axis**: Fiscal years ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24"]
- **Y-axis**: Rate per 100,000 population (range: 300-600, auto-scaling)
- **Lines**: Two lines with distinct colors:
  - **Urban**: Blue line (lower values)
  - **Rural/Remote**: Red line (higher values)
- **Gap Fill**: Colored area between lines highlighting the disparity

#### **Interactive Controls**
1. **Confidence Intervals Toggle**:
   - **Type**: Checkbox (`dcc.Checklist`)
   - **Options**: ["Show Confidence Intervals"]
   - **Default**: Unchecked (for cleaner initial view)
   - **Purpose**: Add error bands showing 95% CI from Table 11

2. **Gap Analysis Toggle**:
   - **Type**: Checkbox (`dcc.Checklist`)
   - **Options**: ["Highlight Disparity Gap", "Show Percentage Difference"]
   - **Default**: Both checked
   - **Purpose**: Emphasize the equity gap and quantify the difference

3. **Display Mode**:
   - **Type**: Radio buttons (`dcc.RadioItems`)
   - **Options**: ["Absolute Rates", "Ratio View (Rural:Urban)", "Percentage Above Urban"]
   - **Default**: "Absolute Rates"
   - **Purpose**: Different analytical perspectives on the disparity

#### **Visual Features**
- **Line Styling**: Solid lines with markers, different colors for urban vs rural
- **Gap Fill**: Semi-transparent colored area between lines (light red/orange)
- **Annotations**: Text boxes showing "Rural rate is X% higher" for each year
- **Error Bands**: Optional confidence interval bands around each line
- **Hover Tooltip**: 
  - Template: "Residence: {residence}<br>Year: {year}<br>Rate: {rate} per 100k<br>95% CI: [{ci_lower}-{ci_upper}]<br>Gap: {gap} per 100k<br>Rural advantage: {percentage}%"
- **Reference Lines**: Optional horizontal lines showing Canada averages

#### **Teaching Purpose**
- **Primary Insight**: Demonstrate persistent rural disadvantage in youth mental health hospitalizations
- **Secondary Insights**: 
  - Rural youth consistently have 20-30% higher hospitalization rates
  - Health equity gap persisted even through COVID disruption
  - Both populations showed similar COVID patterns but maintained disparity
  - Rural rates range 444-567 vs Urban rates 345-446 (highlighting concrete numbers)
- **Student Discovery**: Let students explore how the rural-urban gap changes over time and whether COVID affected both populations equally

---

## Visual Element 6: Income Gradient in Mental Health Hospitalizations

### **Data Source**
- **Table**: Table 12 - Children and youth hospitalized for mental disorders, by income quintile, Canada, 2018–2019 to 2023–2024
- **Metrics**: Rate per 100,000 population
- **Geographic Coverage**: Canada (national aggregate)
- **Demographics**: 5 income quintiles (Q1=lowest income to Q5=highest income)
- **Time Period**: 6 fiscal years (2018-19 to 2023-24)

### **Visualization Choice: Multi-Line Income Gradient Chart**

#### **Chart Specifications**
- **Chart Type**: `plotly.express.line` with multiple traces
- **X-axis**: Fiscal years ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24"]
- **Y-axis**: Rate per 100,000 population (range: 250-650, auto-scaling)
- **Lines**: Five lines, one for each income quintile:
  - **Q1 (Lowest)**: Red line (highest rates)
  - **Q2**: Orange line
  - **Q3**: Yellow line  
  - **Q4**: Light green line
  - **Q5 (Highest)**: Green line (lowest rates)
- **Color Gradient**: Clear progression from red (high rates) to green (low rates)

#### **Interactive Controls**
1. **Confidence Intervals Toggle**:
   - **Type**: Checkbox (`dcc.Checklist`)
   - **Options**: ["Show Confidence Intervals"]
   - **Default**: Unchecked (for cleaner initial view)
   - **Purpose**: Add error bands showing 95% CI from Table 12

2. **Inequality Metrics Display**:
   - **Type**: Checkbox (`dcc.Checklist`)
   - **Options**: ["Show Q1:Q5 Ratio", "Show Gradient Shading"]
   - **Default**: Both checked
   - **Purpose**: Quantify and visualize the socioeconomic gradient

3. **Display Mode**:
   - **Type**: Radio buttons (`dcc.RadioItems`)
   - **Options**: ["Absolute Rates", "Relative to Q5", "Percentage Above National Average"]
   - **Default**: "Absolute Rates"
   - **Purpose**: Different analytical perspectives on income inequality

#### **Visual Features**
- **Line Styling**: Solid lines with markers, color-coded by income level
- **Gradient Fill**: Optional semi-transparent areas between quintile lines
- **Ratio Annotations**: Text boxes showing "Q1 is X.X times higher than Q5" for each year
- **Error Bands**: Optional confidence interval bands around each line
- **Hover Tooltip**: 
  - Template: "Income Quintile: {quintile}<br>Year: {year}<br>Rate: {rate} per 100k<br>95% CI: [{ci_lower}-{ci_upper}]<br>Ratio to Q5: {ratio}<br>National Rank: {rank}/5"
- **Reference Lines**: Optional horizontal line showing national average

#### **Teaching Purpose**
- **Primary Insight**: Demonstrate persistent socioeconomic gradient in youth mental health hospitalizations
- **Secondary Insights**: 
  - Clear income hierarchy: Q1 consistently 1.6-2.0x higher than Q5
  - Gradient persisted through COVID disruption (all groups affected similarly but maintained relative positions)
  - Poverty is a strong predictor of mental health crises
  - 2023-24: Q1 (529) vs Q5 (296) = 1.8x difference
- **Student Discovery**: Let students explore how the income gradient changes over time and whether COVID affected all income groups equally

---

## Visual Element 7: Income Quintile Contribution to Mental Health Hospitalizations

### **Data Source**
- **Table**: Table 12 - Children and youth hospitalized for mental disorders, by income quintile, Canada, 2018–2019 to 2023–2024
- **Metrics**: Rate per 100,000 population (converted to estimated case numbers)
- **Geographic Coverage**: Canada (national aggregate)
- **Demographics**: 5 income quintiles with estimated population distributions
- **Time Period**: User-selected fiscal year from 6 available years

### **Visualization Choice: Income Quintile Contribution Pie Chart**

#### **Chart Specifications**
- **Chart Type**: `plotly.express.pie`
- **Values**: Estimated mental health hospitalizations by income quintile for selected fiscal year
- **Labels**: Income quintile names ["Q1 (Lowest Income)", "Q2", "Q3", "Q4", "Q5 (Highest Income)"]
- **Size**: Proportional to each quintile's estimated contribution to national total
- **Color**: Same gradient as Visual Element 6 (red to green)

#### **Interactive Controls**
1. **Fiscal Year Selector**:
   - **Type**: Dropdown (`dcc.Dropdown`)
   - **Options**: ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24"]
   - **Default Selection**: "2023-24" (most recent year)
   - **Purpose**: Allow exploration of how quintile contributions changed over time

2. **Display Mode**:
   - **Type**: Radio buttons (`dcc.RadioItems`)
   - **Options**: ["Estimated Case Numbers", "Rate per 100,000", "Per-Capita Burden"]
   - **Default**: "Estimated Case Numbers"
   - **Purpose**: Show absolute contribution vs rate-based burden

#### **Visual Features**
- **Slice Colors**: Income gradient coloring (red=Q1, green=Q5) consistent with Element 6
- **Hover Tooltip**: 
  - Template: "Income Quintile: {quintile}<br>Year: {year}<br>Estimated Cases: {cases}<br>Percentage of Total: {percentage}%<br>Rate per 100k: {rate}<br>Burden Index: {burden}"
- **Slice Labels**: Show quintile names and percentages on larger slices
- **Inequality Annotation**: Text showing "Q1 contributes X% despite being only 20% of population"
- **Legend**: Income quintile descriptions with color coding

#### **Teaching Purpose**
- **Primary Insight**: Visualize how lower-income populations contribute disproportionately to mental health hospitalization burden
- **Secondary Insights**: 
  - Q1 and Q2 likely contribute >40% of cases despite being only 40% of population
  - Higher-income quintiles (Q4, Q5) contribute less than their population share
  - Changes in contribution patterns during COVID years
  - Population vs per-capita burden comparison
- **Student Discovery**: Let students explore whether lower-income groups contribute more cases than expected based on population size alone

---

## Visual Element 8: Clinical Diagnostic Patterns by Age and Gender

### **Data Source**
- **Table**: Table 13 series - Children and youth hospitalized for mental disorders, by diagnosis, sex and age group, Canada, 2018–2019 to 2023–2024
- **Metrics**: Rate per 100,000 population with 95% confidence intervals
- **Geographic Coverage**: Canada (national aggregate)
- **Dimensions**: 
  - **Diagnosis Categories**: 7 main categories + 4 subcategories (Neurocognitive, Substance-related, Schizophrenic/psychotic, Mood, Anxiety, Personality, Other disorders, plus Trauma/stressor, Conduct, Eating, etc.)
  - **Age Groups**: 5-9, 10-14, 15-17, 18-24 years
  - **Sex**: Female, Male, Total
- **Time Period**: Focus on 2023-2024 (most recent year) with option to compare across years

### **Visualization Choice: Interactive Heat Map Matrix**

#### **Chart Specifications**
- **Chart Type**: `plotly.express.imshow` with custom annotations
- **X-axis**: Age groups ["5-9", "10-14", "15-17", "18-24"]
- **Y-axis**: Diagnosis categories (main categories + key subcategories)
- **Color Scale**: Rate per 100,000 population with custom colorscale:
  - **Low rates (0-20)**: Light blue
  - **Medium rates (20-100)**: Yellow to orange
  - **High rates (100+)**: Red to dark red
- **Cell Annotations**: Rate values displayed in cells when space allows

#### **Interactive Controls**
1. **Sex Selector**:
   - **Type**: Radio buttons (`dcc.RadioItems`)
   - **Options**: ["Female", "Male", "Both Combined", "Gender Comparison (F:M Ratio)"]
   - **Default**: "Female"
   - **Purpose**: Reveal dramatic gender differences across diagnostic categories

2. **Diagnosis Filter**:
   - **Type**: Multi-select checklist (`dcc.Checklist`)
   - **Options**: All diagnosis categories with option to select/deselect groups
   - **Default**: All main categories selected
   - **Purpose**: Focus analysis on specific clinical conditions of interest

3. **Color Scale Options**:
   - **Type**: Dropdown (`dcc.Dropdown`)
   - **Options**: ["Linear Scale", "Log Scale", "Percentile Ranking", "Z-Score Normalization"]
   - **Default**: "Linear Scale"
   - **Purpose**: Optimize visualization for different analytical perspectives

4. **Year Comparison** (Advanced):
   - **Type**: Dropdown (`dcc.Dropdown`)
   - **Options**: ["2023-24 Only", "Compare with 2018-19", "Show COVID Impact (2020-21)", "6-Year Average"]
   - **Default**: "2023-24 Only"
   - **Purpose**: Temporal analysis of diagnostic patterns

#### **Visual Features**
- **Cell Styling**: Clear borders, readable text annotations showing exact rates
- **Color Coding**: Intuitive progression from blue (low) to red (high) rates
- **Missing Data**: Gray cells for suppressed values or unavailable data
- **Hover Tooltip**: 
  - Template: "{diagnosis}<br>Age: {age}<br>Sex: {sex}<br>Rate: {rate} per 100k<br>95% CI: [{ci_lower}-{ci_upper}]<br>Risk Level: {risk_category}<br>Gender Ratio (F:M): {gender_ratio}"
- **Border Highlighting**: Thick borders around cells in 90th percentile (highest-risk combinations)
- **Legend**: Clear color scale with rate ranges and risk level descriptions

#### **Teaching Purpose**
- **Primary Insight**: Reveal complex patterns of how different mental health conditions affect different age groups and genders
- **Secondary Insights**: 
  - **Eating disorders**: Dramatic peak in 15-17 females (105 per 100k vs 13 males)
  - **Substance disorders**: Peak in 18-24 age group, higher male rates
  - **Mood disorders**: High across adolescent/young adult females (291 in 15-17, 170 in 18-24)
  - **Developmental progression**: How different conditions emerge across age groups
  - **Gender-specific vulnerabilities**: Clear diagnostic categories with strong gender differences
- **Student Discovery**: 
  - Let students explore gender toggle to discover striking male-female differences
  - Identify highest-risk age-diagnosis combinations (red cells)
  - Understand developmental psychiatry patterns
  - Recognize need for targeted, gender-informed interventions

#### **Advanced Features**
- **Click cells**: Drill down to detailed statistics and confidence intervals
- **Pattern detection**: Automatic highlighting of unusual patterns or outliers
- **Export functionality**: Save selected patterns or filtered views
- **Clinical notes**: Hover explanations for diagnostic categories and clinical significance

---

## Implementation Notes
- Use consistent color palette across all visualizations
- Ensure responsive design for different screen sizes
- Include data source citations and methodology notes
- Plan for smooth transitions between different views
- Consider linked interactions between charts (e.g., selecting a province in one chart highlights it in others)