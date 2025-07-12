# Question 2 Explanation: Time Series Regression and Autocorrelation Testing

## Background Context
John Durbin and Bill Watson are cybersecurity managers at TechnoCorp Inc. They're analyzing unsuccessful remote login attempts over 10 weeks to understand patterns and potential security threats. This type of analysis helps identify if attacks are random or follow predictable patterns.

## The Problem
We have weekly data on unsuccessful remote logins (in thousands):

| Week | Unsuccessful Logins ('000) |
|------|---------------------------|
| 1    | 933                      |
| 2    | 826                      |
| 3    | 748                      |
| 4    | 908                      |
| 5    | 983                      |
| 6    | 1009                     |
| 7    | 1101                     |
| 8    | 1149                     |
| 9    | 1207                     |
| 10   | 1255                     |

A linear regression analysis was performed, resulting in the equation:
**ŷ = 739.40 + 49.55 × t**

## Part 1: Calculate Residuals and Squared Residuals

### Key Concepts

**Residuals (e)**: The difference between actual observed values and predicted values from the regression model. They represent the "error" or unexplained variation.

**Formula**: e_t = y_t - ŷ_t

**Why Important**: Residuals help us:
- Assess model fit quality
- Check regression assumptions
- Identify outliers or patterns the model missed

### Calculations

For each week, we calculate:
1. **Predicted value (ŷ)**: Using the regression equation
2. **Residual (e)**: Actual - Predicted
3. **Squared residual (e²)**: For later statistical tests

| Week (t) | Actual (y) | Predicted (ŷ) | Residual (e) | Squared Residual (e²) |
|----------|------------|----------------|--------------|----------------------|
| 1 | 933 | 739.40 + 49.55×1 = 788.95 | 144.05 | 20,751.71 |
| 2 | 826 | 739.40 + 49.55×2 = 838.49 | -12.49 | 156.02 |
| 3 | 748 | 739.40 + 49.55×3 = 888.04 | -140.04 | 19,610.18 |
| 4 | 908 | 739.40 + 49.55×4 = 937.58 | -29.58 | 875.08 |
| 5 | 983 | 739.40 + 49.55×5 = 987.13 | -4.13 | 17.03 |
| 6 | 1009 | 739.40 + 49.55×6 = 1036.67 | -27.67 | 765.78 |
| 7 | 1101 | 739.40 + 49.55×7 = 1086.22 | 14.78 | 218.50 |
| 8 | 1149 | 739.40 + 49.55×8 = 1135.76 | 13.24 | 175.20 |
| 9 | 1207 | 739.40 + 49.55×9 = 1185.31 | 21.69 | 470.50 |
| 10 | 1255 | 739.40 + 49.55×10 = 1234.85 | 20.15 | 405.84 |

**Total of Squared Residuals**: Σe² = 43,445.85

## Part 2: Calculate Standardized Residuals

### Key Concepts

**Standardized Residuals**: Residuals divided by their standard deviation. This helps:
- Compare residuals on a common scale
- Identify unusually large residuals (potential outliers)
- Check if residuals follow a normal distribution

**Formula**: e^z_t = e_t / √[(1/(n-1)) × Σe²]

### Calculation

**Step 1**: Calculate standard deviation of residuals
```
√[(1/(n-1)) × Σe²] = √[(1/9) × 43,445.85] = √4,827.32 = 69.48
```

**Step 2**: Standardize each residual

| Week (t) | Residual (e) | Standardized Residual (e^z) |
|----------|--------------|----------------------------|
| 1 | 144.05 | 144.05/69.48 = 2.07 |
| 2 | -12.49 | -12.49/69.48 = -0.18 |
| 3 | -140.04 | -140.04/69.48 = -2.02 |
| 4 | -29.58 | -29.58/69.48 = -0.43 |
| 5 | -4.13 | -4.13/69.48 = -0.06 |
| 6 | -27.67 | -27.67/69.48 = -0.40 |
| 7 | 14.78 | 14.78/69.48 = 0.21 |
| 8 | 13.24 | 13.24/69.48 = 0.19 |
| 9 | 21.69 | 21.69/69.48 = 0.31 |
| 10 | 20.15 | 20.15/69.48 = 0.29 |

**Interpretation**: Values beyond ±2 might be outliers. Here, weeks 1 (+2.07) and 3 (-2.02) are close to this threshold.

## Part 3: Durbin-Watson Test for Autocorrelation

### Key Concepts

**Autocorrelation**: When current values are correlated with previous values. In time series:
- **Positive autocorrelation**: High values tend to follow high values
- **Negative autocorrelation**: High values tend to follow low values
- **No autocorrelation**: Values are independent of previous values

**Why Important**: 
- Violates regression assumptions if present
- Affects reliability of statistical tests
- Common in time series data

**Durbin-Watson Statistic**: 
```
d = Σ(e_t - e_(t-1))² / Σe_t²
```

### Calculation

**Step 1**: Calculate differences between consecutive residuals and square them

| Week | (e_t - e_(t-1))² |
|------|------------------|
| 2 | (-12.49 - 144.05)² = 24,506.48 |
| 3 | (-140.04 - (-12.49))² = 16,267.84 |
| 4 | (-29.58 - (-140.04))² = 12,200.21 |
| 5 | (-4.13 - (-29.58))² = 647.93 |
| 6 | (-27.67 - (-4.13))² = 554.39 |
| 7 | (14.78 - (-27.67))² = 1,802.39 |
| 8 | (13.24 - 14.78)² = 2.39 |
| 9 | (21.69 - 13.24)² = 71.48 |
| 10 | (20.15 - 21.69)² = 2.39 |

**Sum**: Σ(e_t - e_(t-1))² = 56,055.50

**Step 2**: Calculate Durbin-Watson statistic
```
d = 56,055.50 / 43,445.85 = 1.29
```

### Hypothesis Testing

**Test for Positive Autocorrelation**:
- H₀: No positive autocorrelation
- H₁: Positive autocorrelation exists

**Critical Values**: d_L = 0.879, d_U = 1.320

**Decision Rule**:
- If d < d_L: Reject H₀ (positive autocorrelation exists)
- If d > d_U: Do not reject H₀ (no positive autocorrelation)
- If d_L ≤ d ≤ d_U: Test is inconclusive

**Result**: Since 0.879 ≤ 1.29 ≤ 1.320, the **test is inconclusive** for positive autocorrelation.

**Test for Negative Autocorrelation**:
- H₀: No negative autocorrelation
- H₁: Negative autocorrelation exists

**Decision Rule**: Use (4-d) and compare with d_U
- (4-d) = 4-1.29 = 2.71
- Since 2.71 > 1.32, we **do not reject H₀**

**Conclusion**: No evidence of negative autocorrelation.

## Business Implications

### For Cybersecurity Analysis:
1. **Pattern Recognition**: The inconclusive autocorrelation test suggests unsuccessful login attempts don't follow a strong predictable pattern
2. **Attack Independence**: This could indicate that attacks are largely independent events rather than coordinated campaigns
3. **Forecasting Reliability**: The lack of strong autocorrelation makes simple trend forecasting more reliable
4. **Resource Planning**: Security teams can plan resources based on the general upward trend without worrying about strong cyclical patterns

### Statistical Implications:
1. **Model Validity**: While we can't definitively rule out positive autocorrelation, there's no strong evidence it exists
2. **Assumption Checking**: This analysis is crucial for validating regression model assumptions
3. **Further Analysis**: If autocorrelation were present, we'd need more sophisticated time series models (ARIMA, etc.)
