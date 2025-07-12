# Question 11 Explanation: Manufacturing Quality Control Through Regression Analysis

## Background Context
In manufacturing, quality control is critical for maintaining product standards and customer satisfaction. This study examines whether assembly line speed affects the detection of defective parts during visual inspection. Understanding this relationship helps optimize production processes for both efficiency and quality.

## The Problem
**Research Question**: Does assembly line speed affect the number of defective parts found during inspection?

**Data Collected**:
| Line Speed (ft/min) | Defective Parts Found |
|---------------------|----------------------|
| 20 | 21 |
| 20 | 19 |
| 40 | 15 |
| 30 | 16 |
| 60 | 14 |
| 40 | 17 |

**Analysis Goals**:
1. Visualize the relationship through scatter plot
2. Develop regression equation
3. Calculate coefficient of determination
4. Interpret business implications

## Part 1: Scatter Plot Analysis and Model Formulation

### Visual Analysis

**Creating the Scatter Plot**:
- **X-axis**: Line Speed (feet per minute)
- **Y-axis**: Number of Defective Parts Found
- **Pattern Observed**: Clear downward trend

**Key Observations from the Plot**:
1. **Negative Slope**: As line speed increases, defective parts found decreases
2. **Linear Relationship**: Points roughly follow a straight line
3. **Strong Association**: Clear pattern visible despite some scatter

### Theoretical Model Formulation

**Population Model**: y = β₀ + β₁x + ε

Where:
- **y** = Number of defective parts found (dependent variable)
- **x** = Line speed in ft/min (independent variable)
- **β₀** = True intercept (defective parts when speed = 0)
- **β₁** = True slope (change in defective parts per unit speed increase)
- **ε** = Random error term

**Sample Model to be Estimated**: ŷ = b₀ + b₁x

Where b₀ and b₁ are sample estimates of the population parameters.

## Part 2: Regression Equation Development

### Required Calculations

**Summary Statistics**:
- n = 6 observations
- Σx = 210
- Σy = 102  
- Σ(x·y) = 3,400
- Σ(x²) = 8,500

### Calculate Slope (b₁)

**Formula**: 
```
b₁ = [n·Σ(xi·yi) - Σxi·Σyi] / [n·Σ(xi²) - (Σxi)²]
```

**Calculation**:
```
b₁ = [6×3,400 - 210×102] / [6×8,500 - (210)²]
   = [20,400 - 21,420] / [51,000 - 44,100]
   = -1,020 / 6,900
   = -0.1478
```

### Calculate Intercept (b₀)

**Means**:
- x̄ = 210/6 = 35
- ȳ = 102/6 = 17

**Formula**: b₀ = ȳ - b₁·x̄

**Calculation**:
```
b₀ = 17 - (-0.1478×35) = 17 + 5.173 = 22.1739
```

### Final Regression Equation
**ŷ = 22.17 - 0.148x**

### Business Interpretation

**Intercept (22.17)**:
- When line speed = 0 (theoretical), 22.17 defective parts would be found
- Represents baseline defect detection capability

**Slope (-0.148)**:
- For each 1 ft/min increase in line speed, defective parts found decreases by 0.148
- **Critical Insight**: Faster production reduces defect detection ability

## Part 3: Coefficient of Determination Analysis

### Theoretical Framework

**R² Definition**: Proportion of total variation in y explained by the regression model

**Formula**: R² = Σ(ŷᵢ - ȳ)² / Σ(yᵢ - ȳ)²

### Step-by-Step Calculation

#### Calculate Predicted Values and Variations

| Obs | x | y | ŷᵢ | (ŷᵢ - ȳ)² | (yᵢ - ȳ)² |
|-----|---|---|----|-----------|-----------| 
| 1 | 20 | 21 | 19.22 | 4.92 | 16.0 |
| 2 | 20 | 19 | 19.22 | 4.92 | 4.0 |
| 3 | 40 | 15 | 16.26 | 0.55 | 4.0 |
| 4 | 30 | 16 | 17.74 | 0.55 | 1.0 |
| 5 | 60 | 14 | 13.30 | 13.66 | 9.0 |
| 6 | 40 | 17 | 16.26 | 0.55 | 0.0 |

**Totals**:
- Σ(ŷᵢ - ȳ)² = 25.13 (Explained variation)
- Σ(yᵢ - ȳ)² = 34.0 (Total variation)

#### Calculate R²
```
R² = 25.13 / 34.0 = 0.7391 = 73.91%
```

### Interpretation of R²

**Meaning**: The regression model explains **73.91%** of the variation in defective parts found.

**Quality Assessment**:
- **Excellent**: R² > 0.70 ✓
- **Strong Predictive Power**: Model captures most of the relationship
- **Remaining 26.09%**: Due to other factors not in the model

## Difference Between R² and Correlation Coefficient

### Correlation Coefficient (r)
- **Range**: -1 to +1
- **Measures**: Strength and direction of linear relationship
- **Value**: r = √R² = √0.7391 = -0.860 (negative due to negative slope)
- **Interpretation**: Strong negative linear association

### Coefficient of Determination (R²)
- **Range**: 0 to 1
- **Measures**: Proportion of variance explained
- **Value**: R² = 0.7391 = 73.91%
- **Interpretation**: Explanatory power of the model

### Key Differences

| Aspect | Correlation (r) | R² |
|--------|----------------|----| 
| Purpose | Measures association | Measures explanation |
| Range | -1 to +1 | 0 to 1 |
| Units | Unitless | Percentage |
| Interpretation | Strength & direction | Explanatory power |
| Business Use | Relationship assessment | Model evaluation |

## Comprehensive Business Analysis

### Quality Control Implications

#### Critical Findings
1. **Speed-Quality Trade-off**: Faster production reduces inspection effectiveness
2. **Quantified Relationship**: Each 10 ft/min increase reduces detection by ~1.5 parts
3. **Strong Predictability**: Model can reliably predict inspection performance

#### Operational Decisions

**Production Speed Optimization**:
- **Conservative Speed**: 20-30 ft/min for maximum defect detection
- **Balanced Approach**: 40 ft/min balances speed and quality
- **High Speed Risk**: 60+ ft/min significantly reduces quality control

### Strategic Recommendations

#### Immediate Actions
1. **Speed Limits**: Establish maximum line speeds based on quality requirements
2. **Inspector Training**: Enhance skills for high-speed inspection
3. **Technology Investment**: Consider automated defect detection systems
4. **Quality Monitoring**: Implement continuous quality tracking

#### Long-term Improvements
1. **Process Redesign**: Optimize workflow for both speed and quality
2. **Multiple Inspections**: Add inspection points for high-speed production
3. **Statistical Control**: Use control charts for ongoing monitoring
4. **Technology Integration**: Implement vision systems or AI-based detection

### Model Limitations and Considerations

#### Statistical Assumptions
1. **Linearity**: Assumes constant rate of change (may not hold at extremes)
2. **Independence**: Each observation assumed independent
3. **Homoscedasticity**: Constant variance across speed levels
4. **Normality**: Residuals should be normally distributed

#### Business Limitations
1. **Sample Size**: Only 6 observations limit statistical power
2. **Speed Range**: Limited to 20-60 ft/min range
3. **Single Factor**: Only considers speed, not other factors
4. **Inspector Variation**: Doesn't account for individual differences

### Advanced Analysis Recommendations

#### Statistical Enhancements
1. **Larger Sample**: Collect more data for robust analysis
2. **Residual Analysis**: Check model assumptions
3. **Non-linear Models**: Explore polynomial relationships
4. **Multiple Regression**: Include other relevant factors

#### Operational Enhancements
1. **Factor Analysis**: Include lighting, product complexity, inspector experience
2. **Time Series**: Study performance changes over time
3. **Comparative Studies**: Analyze different product lines
4. **Cost-Benefit Analysis**: Balance speed gains vs quality costs

This analysis demonstrates how regression analysis can optimize manufacturing processes by quantifying trade-offs between efficiency and quality, providing data-driven insights for operational decision-making.
