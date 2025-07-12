# Question 2 Explanation: Time Series Regression and Autocorrelation Testing

## Background Context
John Durbin and Bill Watson are cybersecurity managers at TechnoCorp Inc. facing a critical challenge: understanding the nature of cyber attacks targeting their systems. They're analyzing unsuccessful remote login attempts over 10 weeks to determine whether these security incidents are:

- **Random attacks**: Independent, opportunistic attempts by different attackers
- **Coordinated campaigns**: Systematic attacks that might escalate or follow patterns
- **Persistent threats**: Advanced attackers who adjust their tactics based on previous attempts

**Why This Matters**: Understanding attack patterns helps determine:
- Resource allocation for cybersecurity teams
- Whether current defenses are effective
- If attackers are learning from failed attempts
- How to predict and prepare for future attack volumes

**The Statistical Challenge**: Traditional analysis might miss subtle patterns in the data. Time series regression helps identify trends, while autocorrelation testing reveals whether attack attempts influence each other over time.

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

A linear regression analysis was performed to find the best-fitting line through our data points.

## Reading the Regression Equation from the Output Table

### Quick Recognition Method

Looking at the regression output table provided in the exam:

```
SUMMARY OUTPUT
Regression Statistics
Multiple R            0.999
R Square             0.998
Adjusted R Square    0.998
Standard Error       6.9
Observations         10

ANOVA                df    SS        MS        F    Significance F
Regression           1     20225.51  20225.51  420.7  0.00
Residual             8     384.46    48.06
Total                9     20609.97

                Coefficients  Standard Error  t Stat  P-value  Lower 95%  Upper 95%
Intercept       739.40        57.00          12.97   0.00     623.31     855.49
Week            49.55         2.42           20.51   0.00     30.84      68.26
```

### How to Quickly Identify the Regression Equation:

**Step 1**: Look at the "Coefficients" column in the bottom table
- **Intercept**: 739.40 (this is your 'a' value)
- **Week**: 49.55 (this is your 'b' value, the slope)

**Step 2**: Plug into the standard form ŷ = a + b × t
- **ŷ = 739.40 + 49.55 × t**

**That's it!** No complex calculations needed during an exam.

### What Each Row Means:
- **Intercept row**: Shows the y-intercept (739.40) - where the line crosses the y-axis
- **Week row**: Shows the slope (49.55) - how much y increases for each unit increase in week

### Quick Check:
- **Multiple R = 0.999**: Very strong relationship (close to 1.0)
- **R Square = 0.998**: 99.8% of variation is explained by the model
- **Both p-values = 0.00**: Both coefficients are statistically significant
**ŷ = 739.40 + 49.55 × t**

### Interpreting the Regression Equation

**ŷ = 739.40 + 49.55 × t**

**What each component means**:
- **739.40** (y-intercept): The baseline level of unsuccessful logins when t = 0 (theoretical week 0)
  - This represents the "starting point" before the time period began
  - In cybersecurity terms: the baseline threat level before the observed trend started
  
- **49.55** (slope): The rate of increase per week
  - Each week, unsuccessful login attempts increase by approximately 49,550
  - This represents the trend: attacks are escalating by about 49.55 thousand attempts per week
  - **This is concerning!** It suggests a sustained increase in cyber threats

**Practical Examples**:
- **Week 1 prediction**: ŷ = 739.40 + 49.55 × 1 = 788.95 thousand
- **Week 5 prediction**: ŷ = 739.40 + 49.55 × 5 = 987.15 thousand  
- **Week 10 prediction**: ŷ = 739.40 + 49.55 × 10 = 1,234.90 thousand

**Forecasting Future Weeks**:
- **Week 11**: ŷ = 739.40 + 49.55 × 11 = 1,284.45 thousand
- **Week 12**: ŷ = 739.40 + 49.55 × 12 = 1,334.00 thousand

**Business Implications**:
- **Linear growth**: Attacks are increasing at a steady, predictable rate
- **Significant escalation**: Nearly 50,000 additional attempts per week
- **Resource planning**: Security teams need to plan for continuous capacity increases
- **Trend analysis**: The consistent upward trend suggests systematic factors driving increased attacks

## Part 1: Calculate Residuals and Squared Residuals

### Key Concepts

**Residuals (e)**: The difference between what actually happened and what our model predicted would happen. Think of residuals as "prediction errors" or "surprises."

**Formula**: e_t = y_t - ŷ_t
- e_t = residual for time period t
- y_t = actual observed value
- ŷ_t = predicted value from regression model

**What Residuals Tell Us**:
- **Small residuals**: Model predictions are accurate
- **Large residuals**: Model missed something important
- **Pattern in residuals**: Model is missing a systematic trend or relationship
- **Random residuals**: Model has captured the main patterns well

**Real-World Interpretation**:
- **Positive residual**: More attacks occurred than predicted (concerning!)
- **Negative residual**: Fewer attacks than predicted (good news)
- **Large positive residuals**: Potential security breaches or new attack methods
- **Large negative residuals**: Successful defense improvements or attacker deterrence

**Why Residuals Matter in Cybersecurity**:
1. **Anomaly Detection**: Unusually large residuals might indicate new types of attacks
2. **Model Validation**: Consistent patterns in residuals suggest our model needs improvement
3. **Forecasting Accuracy**: Small, random residuals mean we can trust future predictions
4. **Resource Planning**: Understanding prediction errors helps allocate security resources

### Calculations

For each week, we calculate:
1. **Predicted value (ŷ)**: Using the regression equation ŷ = 739.40 + 49.55 × t
2. **Residual (e)**: Actual - Predicted (how far off our prediction was)
3. **Squared residual (e²)**: Used in statistical tests (eliminates negative signs)

**Step-by-Step Example for Week 1**:
- **Predicted**: ŷ₁ = 739.40 + 49.55 × 1 = 788.95 thousand unsuccessful logins
- **Actual**: y₁ = 933 thousand unsuccessful logins  
- **Residual**: e₁ = 933 - 788.95 = 144.05 thousand (model underestimated by 144,050 attempts!)
- **Squared Residual**: e₁² = (144.05)² = 20,751.71

**Complete Analysis Table**:

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

**Key Insights from the Residuals**:
- **Week 1**: Largest positive residual (+144.05) - significant underestimate, possible new attack vector
- **Week 3**: Largest negative residual (-140.04) - model overestimated, perhaps defenses improved
- **Later weeks (7-10)**: Small positive residuals suggest model is tracking well with slight underestimates
- **Overall pattern**: Model captures the general trend but misses some weekly variations

## Part 2: Calculate Standardized Residuals

### Key Concepts

**Standardized Residuals**: Converting residuals to a common scale that makes them easier to interpret and compare. Think of it as "how many standard deviations away from normal is this residual?"

**Why Standardize?**:
- **Comparison**: Makes all residuals comparable regardless of their original scale
- **Outlier Detection**: Values beyond ±2 are considered potentially unusual
- **Normal Distribution Check**: Standardized residuals should follow a standard normal distribution if our model assumptions are correct

**Formula**: e^z_t = e_t / s_e
- e^z_t = standardized residual for time t
- e_t = original residual  
- s_e = standard deviation of all residuals

**Interpretation Guide**:
- **|e^z| < 1**: Normal variation (about 68% of data should fall here)
- **1 ≤ |e^z| < 2**: Somewhat unusual but not necessarily problematic
- **|e^z| ≥ 2**: Potentially significant outlier requiring investigation
- **|e^z| ≥ 3**: Definitely an outlier - urgent investigation needed

**Cybersecurity Context**:
- **High positive standardized residual**: Unexpectedly high attack volume
- **High negative standardized residual**: Unexpectedly low attack volume  
- **Multiple outliers**: Model may be missing important patterns

### Calculation

**Step 1**: Calculate standard deviation of residuals
```
s_e = √[(1/(n-1)) × Σe²] = √[(1/(10-1)) × 43,445.85] = √[43,445.85/9] = √4,827.32 = 69.48
```

**Why divide by (n-1)?** This gives us the sample standard deviation, which provides an unbiased estimate of the population standard deviation.

**Step 2**: Standardize each residual by dividing by the standard deviation

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

**Detailed Analysis**:
- **Week 1 (+2.07)**: Just above the +2 threshold - this represents a significant spike in unsuccessful logins that our model didn't predict. Possible causes:
  - New attack campaign launched
  - Security vulnerability discovered by attackers
  - Seasonal/event-driven increase in attacks
  
- **Week 3 (-2.02)**: Just above the -2 threshold - model significantly overestimated attacks. Possible causes:
  - Successful implementation of new security measures
  - Attackers shifted focus to other targets
  - Temporary disruption of attack infrastructure

- **Other weeks**: All fall within ±1 standard deviation, indicating normal prediction accuracy

**Security Implications**: The two near-outliers (weeks 1 and 3) suggest discrete events affecting attack patterns rather than random variation.

## Part 3: Durbin-Watson Test for Autocorrelation

### Key Concepts

**Autocorrelation**: A statistical relationship where current values are influenced by previous values. In simple terms: "Does what happened last week affect what happens this week?"

**Types of Autocorrelation**:
- **Positive autocorrelation**: 
  - High values tend to follow high values
  - Low values tend to follow low values
  - Creates "clustering" or "momentum" in the data
  - Example: If attacks are high one week, they're likely high the next week
  
- **Negative autocorrelation**: 
  - High values tend to follow low values
  - Low values tend to follow high values
  - Creates an "alternating" or "oscillating" pattern
  - Example: High attacks one week, low attacks the next week
  
- **No autocorrelation**: 
  - Current values are independent of previous values
  - Each week's attacks are unrelated to previous weeks
  - Random pattern with no predictable sequence

**Why Autocorrelation Matters**:
1. **Regression Assumptions**: Linear regression assumes residuals are independent (no autocorrelation)
2. **Forecasting**: If autocorrelation exists, we can use past values to predict future values more accurately  
3. **Model Selection**: Strong autocorrelation suggests we need time series models instead of simple regression
4. **Statistical Tests**: Autocorrelation makes standard regression tests unreliable

**Cybersecurity Implications**:
- **Positive autocorrelation**: Suggests coordinated, persistent attack campaigns
- **Negative autocorrelation**: Might indicate reactive security measures or attacker adaptation
- **No autocorrelation**: Suggests independent, opportunistic attacks

**Durbin-Watson Statistic**: A specific test designed to detect autocorrelation in regression residuals.
```
d = Σ(e_t - e_(t-1))² / Σe_t²
```

**How it works**: Compares differences between consecutive residuals to the overall variability of residuals. If consecutive residuals are similar (positive autocorrelation), the numerator will be small relative to the denominator.

### Calculation

**Step 1**: Calculate differences between consecutive residuals and square them

**Understanding the Process**: We're looking at how much each residual differs from the previous residual. Large differences suggest independence (no autocorrelation), while small differences suggest autocorrelation.

**Example Calculation for Week 2**:
- e₁ = 144.05 (Week 1 residual)
- e₂ = -12.49 (Week 2 residual)  
- Difference: e₂ - e₁ = -12.49 - 144.05 = -156.54
- Squared difference: (-156.54)² = 24,506.48

**Complete Table**:

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
d = Σ(e_t - e_(t-1))² / Σe_t² = 56,055.50 / 43,445.85 = 1.29
```

**Understanding the Result**:
- **Numerator (56,055.50)**: Sum of squared differences between consecutive residuals
- **Denominator (43,445.85)**: Sum of squared residuals  
- **Ratio (1.29)**: This is our test statistic

**What the d-statistic tells us**:
- **d ≈ 0**: Strong positive autocorrelation (consecutive residuals are very similar)
- **d ≈ 2**: No autocorrelation (consecutive residuals are independent)  
- **d ≈ 4**: Strong negative autocorrelation (consecutive residuals alternate high/low)

### Hypothesis Testing

**Test for Positive Autocorrelation**:
- **H₀ (Null Hypothesis)**: No positive autocorrelation exists (residuals are independent)
- **H₁ (Alternative Hypothesis)**: Positive autocorrelation exists (current residuals are positively related to previous residuals)

**Critical Values**: d_L = 0.879 (lower bound), d_U = 1.320 (upper bound)
*These values come from statistical tables based on sample size (n=10) and number of predictors (k=1)*

**Decision Rule for Positive Autocorrelation**:
- **If d < d_L (d < 0.879)**: Reject H₀ → **Positive autocorrelation exists**
- **If d > d_U (d > 1.320)**: Do not reject H₀ → **No positive autocorrelation**  
- **If d_L ≤ d ≤ d_U (0.879 ≤ d ≤ 1.320)**: **Test is inconclusive**

**Our Result**: d = 1.29
Since 0.879 ≤ 1.29 ≤ 1.320, the **test is inconclusive** for positive autocorrelation.

**What "Inconclusive" Means**:
- We cannot definitively say whether positive autocorrelation exists or not
- The data falls in the "gray area" between the two conclusions
- We need more data or different tests to make a definitive determination
- For practical purposes, we proceed cautiously assuming autocorrelation might exist

**Test for Negative Autocorrelation**:
- **H₀ (Null Hypothesis)**: No negative autocorrelation exists
- **H₁ (Alternative Hypothesis)**: Negative autocorrelation exists (high residuals tend to follow low residuals and vice versa)

**Decision Rule**: Use (4-d) and compare with d_U
- **Calculation**: (4-d) = 4-1.29 = 2.71
- **Comparison**: Since 2.71 > 1.32 (d_U), we **do not reject H₀**

**Interpretation**: No evidence of negative autocorrelation exists.

**Why Use (4-d)?** The Durbin-Watson statistic is symmetric around 2. Values near 4 indicate negative autocorrelation just as values near 0 indicate positive autocorrelation. By calculating (4-d), we transform our test to check the "high end" of the scale.

**Overall Conclusion**: 
- **No negative autocorrelation detected** (definitive)
- **Positive autocorrelation inconclusive** (but not ruled out)
- **Most likely scenario**: Little to no autocorrelation, but we can't be completely certain

## Business Implications

### For Cybersecurity Analysis:

**Pattern Recognition and Threat Assessment**:
1. **Independence of Attacks**: The inconclusive autocorrelation test suggests unsuccessful login attempts don't follow a strong predictable pattern from week to week
2. **Attack Nature**: This pattern indicates attacks are likely:
   - **Opportunistic rather than coordinated**: Different attackers acting independently
   - **Not part of sustained campaigns**: No evidence of persistent, escalating threats
   - **Responsive to external factors**: Weekly variations might be due to news events, vulnerability disclosures, or seasonal factors

**Operational Implications**:
1. **Resource Planning**: 
   - Security teams can plan resources based on the general upward trend (49.55k more attempts per week)
   - No need for complex cyclical staffing patterns
   - Focus on baseline capacity with surge capabilities
   
2. **Alert Systems**:
   - Simple trend-based forecasting is appropriate
   - Threshold alerts can be set based on the regression model ± 2 standard deviations
   - No need for sophisticated autocorrelation-based prediction models
   
3. **Investigation Priorities**:
   - Focus on the outlier weeks (Week 1 high, Week 3 low) for detailed forensic analysis
   - Week 1's high attacks might reveal new attack vectors or vulnerabilities
   - Week 3's low attacks might indicate successful countermeasures to replicate

**Strategic Planning**:
1. **Threat Intelligence**: The lack of strong patterns suggests:
   - Multiple independent threat actors rather than organized groups
   - General increase in cybersecurity threats industry-wide
   - Need for broad defensive measures rather than targeted responses
   
2. **Budget Allocation**:
   - Predictable linear growth allows for systematic capacity planning
   - Investment in scalable, automated defense systems is justified
   - Focus on prevention and detection rather than incident response surge capacity

### Statistical Implications:

**Model Validation and Assumptions**:
1. **Regression Model Validity**: 
   - While we can't definitively rule out positive autocorrelation, there's no strong evidence it exists
   - Our linear regression model (ŷ = 739.40 + 49.55 × t) appears reasonably valid
   - Standard errors and confidence intervals are likely reliable
   
2. **Assumption Checking Importance**: 
   - This Durbin-Watson analysis is crucial for validating regression model assumptions
   - Autocorrelation would violate the independence assumption of linear regression
   - Without this test, our statistical inferences could be misleading
   
3. **Practical Statistical Decision-Making**:
   - The inconclusive result means we should be somewhat cautious about our conclusions
   - We can proceed with the regression model but should:
     - Monitor future data for autocorrelation patterns
     - Consider using robust standard errors
     - Validate predictions carefully

**Future Analysis Recommendations**:
1. **Extended Data Collection**: 
   - Collect more weeks of data to get a more definitive autocorrelation test result
   - More data points would move us out of the "inconclusive" zone
   
2. **Advanced Modeling Options**: 
   - If strong autocorrelation were present, consider ARIMA (AutoRegressive Integrated Moving Average) models
   - Time series models that explicitly account for autocorrelation structure
   - Seasonal decomposition if longer-term patterns emerge
   
3. **Alternative Tests**:
   - Ljung-Box test for higher-order autocorrelation
   - Breusch-Godfrey test as an alternative to Durbin-Watson
   - Visual inspection using autocorrelation function (ACF) plots

**Key Takeaway**: This rigorous statistical analysis provides confidence that our simple regression approach is appropriate for this cybersecurity forecasting problem, while highlighting areas for continued monitoring and potential model refinement.
