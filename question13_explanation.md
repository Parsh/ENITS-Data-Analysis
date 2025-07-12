# Question 13 Explanation: Time Series Analysis with Durbin-Watson Test and Normality Assessment

## Background Context
Smart Data Company has experienced cyber attacks over eight months. The analysis involves testing for autocorrelation in time series regression residuals and assessing the normality of standardized residuals. This is crucial for validating regression model assumptions and ensuring reliable statistical inference.

## The Problem
**Data**: Monthly cyber attacks over 8 months

| Month | Attacks |
|-------|---------|
| January | 242 |
| February | 265 |
| March | 283 |
| April | 312 |
| May | 312 |
| June | 340 |
| July | 335 |
| August | 323 |

**Given Information**:
- Time series regression equation: ŷₜ = 243.21 + 12.95×t
- Durbin-Watson critical values: dₗ₍₀.₀₅₎ = 0.763, dᵤ₍₀.₀₅₎ = 1.332
- Standardized residuals provided for normality testing

## Key Concepts in Time Series Regression Analysis

### Autocorrelation in Time Series
**Definition**: Correlation between current values and past values in the same series.

**Types**:
- **Positive autocorrelation**: High values tend to follow high values
- **Negative autocorrelation**: High values tend to follow low values
- **No autocorrelation**: Values are independent over time

**Why It Matters**:
- Violates regression assumption of independent errors
- Affects standard errors and confidence intervals
- Can lead to spurious statistical significance

### Durbin-Watson Test
**Purpose**: Tests for first-order autocorrelation in regression residuals

**Test Statistic**: 
```
d = Σ(eₜ - eₜ₋₁)² / Σeₜ²
```

**Interpretation**:
- d ≈ 2: No autocorrelation
- d < 2: Positive autocorrelation
- d > 2: Negative autocorrelation

## Durbin-Watson Test Calculation and Analysis

### Step 1: Calculate Residuals and Predicted Values

| Month | t | Attacks | Predicted | Error (eₑ) |
|-------|---|---------|-----------|------------|
| Jan | 1 | 242 | 256.16 | -14.16 |
| Feb | 2 | 265 | 269.11 | -4.11 |
| Mar | 3 | 283 | 282.06 | 0.94 |
| Apr | 4 | 312 | 295.01 | 16.99 |
| May | 5 | 312 | 307.96 | 4.04 |
| Jun | 6 | 340 | 320.91 | 19.09 |
| Jul | 7 | 335 | 333.86 | 1.14 |
| Aug | 8 | 323 | 346.81 | -23.81 |

### Step 2: Calculate Durbin-Watson Components

**Numerator: Σ(eₜ - eₜ₋₁)²**

| Month | (eₜ - eₜ₋₁) | (eₜ - eₜ₋₁)² |
|-------|-------------|-------------|
| Feb | -4.11 - (-14.16) = 10.05 | 101.00 |
| Mar | 0.94 - (-4.11) = 5.05 | 25.50 |
| Apr | 16.99 - 0.94 = 16.05 | 257.60 |
| May | 4.04 - 16.99 = -12.95 | 167.70 |
| Jun | 19.09 - 4.04 = 15.05 | 226.50 |
| Jul | 1.14 - 19.09 = -17.95 | 322.20 |
| Aug | -23.81 - 1.14 = -24.95 | 622.50 |

**Sum**: Σ(eₜ - eₜ₋₁)² = 1,723.02

**Denominator: Σeₜ²**

| Month | eₜ² |
|-------|-----|
| Jan | 200.51 |
| Feb | 16.89 |
| Mar | 0.88 |
| Apr | 288.66 |
| May | 16.32 |
| Jun | 364.43 |
| Jul | 1.30 |
| Aug | 566.92 |

**Sum**: Σeₜ² = 1,455.91

### Step 3: Calculate Durbin-Watson Statistic
```
d = 1,723.02 / 1,455.91 = 1.18
```

### Step 4: Hypothesis Testing

#### Test for Positive Autocorrelation
**Hypotheses**:
- H₀: No positive autocorrelation
- H₁: Positive autocorrelation exists

**Decision Rule**:
- If d < dₗ: Reject H₀ (positive autocorrelation)
- If d > dᵤ: Do not reject H₀ (no positive autocorrelation)  
- If dₗ ≤ d ≤ dᵤ: Test inconclusive

**Analysis**: 0.763 ≤ 1.18 ≤ 1.332
**Conclusion**: **Test is inconclusive** for positive autocorrelation

#### Test for Negative Autocorrelation
**Hypotheses**:
- H₀: No negative autocorrelation
- H₁: Negative autocorrelation exists

**Decision Rule**: Compare (4-d) with dᵤ
- If (4-d) > dᵤ: Do not reject H₀
- If (4-d) < dₗ: Reject H₀

**Analysis**: 
- (4-d) = 4 - 1.18 = 2.82
- Since 2.82 > 1.332, **do not reject H₀**

**Conclusion**: **No evidence of negative autocorrelation**

## Normality Assessment Using Histogram

### Standardized Residuals Analysis

**Given Standardized Residuals**:
| Observation | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|-------------|---|---|---|---|---|---|---|---|
| Stand. Residual | -0.98 | -0.29 | 0.06 | 1.18 | 0.28 | 1.32 | 0.08 | -1.65 |

### Histogram Construction

**Following the rule**: Lower Level ≤ Stand.Residual < Upper Level

| Bin | Interval | Count | Values |
|-----|----------|-------|---------|
| 1 | -2 ≤ value < -1 | 1 | -1.65 |
| 2 | -1 ≤ value < 0 | 2 | -0.98, -0.29 |
| 3 | 0 ≤ value < 1 | 3 | 0.06, 0.28, 0.08 |
| 4 | 1 ≤ value < 2 | 2 | 1.18, 1.32 |

### Normality Assessment

**Distribution Characteristics**:
- **Shape**: Relatively symmetric
- **Range**: All values within ±2 standard deviations
- **Frequency**: Reasonable distribution across bins

**Conclusion**: The error terms are **approximately normally distributed**.

## Comprehensive Analysis and Implications

### Model Validation Results

#### Autocorrelation Assessment
1. **Positive autocorrelation**: Inconclusive (needs further investigation)
2. **Negative autocorrelation**: No evidence
3. **Overall**: Cannot definitively rule out some degree of positive autocorrelation

#### Normality Assessment
✓ **Residuals are approximately normal**: Supports model validity

### Business Interpretation

#### What the Results Mean
1. **Model Reliability**: Basic normality assumption satisfied
2. **Temporal Patterns**: Possible (but not definitive) evidence of attack clustering
3. **Forecasting**: Model can be used with caution for predictions
4. **Further Analysis**: May need more sophisticated time series methods

#### Cybersecurity Implications
1. **Attack Patterns**: Potential clustering suggests coordinated attack campaigns
2. **Response Planning**: Consider that attacks may occur in waves
3. **Resource Allocation**: Plan for potential burst periods
4. **Monitoring**: Implement systems sensitive to attack sequences

### Statistical Methodology Insights

#### Model Assumptions Status
| Assumption | Status | Evidence |
|------------|--------|----------|
| Linearity | ✓ Assumed satisfied | Regression equation provided |
| Independence | ⚠️ Questionable | Inconclusive autocorrelation test |
| Normality | ✓ Satisfied | Histogram analysis confirms |
| Homoscedasticity | ? Not tested | Would need residual plot analysis |

#### Recommendations for Model Improvement

**Immediate Actions**:
1. **Collect more data**: Increase sample size for better test power
2. **Residual analysis**: Plot residuals vs time for visual inspection
3. **Additional tests**: Consider Ljung-Box test for higher-order autocorrelation

**Advanced Modeling**:
1. **ARIMA models**: If autocorrelation confirmed
2. **Seasonal decomposition**: Look for monthly/quarterly patterns
3. **Intervention analysis**: Include external factors (holidays, events)
4. **Machine learning**: Consider more flexible models

### Practical Decision Making

#### Current Model Usage
**Appropriate for**:
- Short-term forecasting (1-2 months)
- General trend analysis
- Budget planning
- Initial risk assessment

**Use with caution for**:
- Long-term predictions
- Precise confidence intervals
- Detailed statistical inference
- Critical security decisions

#### Enhanced Analysis Recommendations

**Data Collection**:
1. **Longer time series**: Collect 2+ years of data
2. **Higher frequency**: Weekly or daily observations
3. **Additional variables**: Include external factors
4. **Attack categorization**: Separate different attack types

**Advanced Testing**:
1. **Structural breaks**: Test for changes in trend/pattern
2. **Non-linear relationships**: Explore polynomial or exponential trends
3. **Multivariate analysis**: Include leading indicators
4. **Cross-validation**: Test model performance on held-out data

## Conclusion

The analysis reveals:
1. **Normality assumption satisfied**: Model residuals are approximately normal
2. **Autocorrelation status unclear**: Cannot definitively confirm or reject temporal dependence
3. **Model usability**: Acceptable for basic analysis with noted limitations
4. **Future research needs**: More data and sophisticated methods needed for robust time series modeling

This demonstrates the importance of assumption testing in statistical analysis and the iterative nature of model development in data analysis.
