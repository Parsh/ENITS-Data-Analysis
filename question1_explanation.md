# Question 1 Explanation: Confidence Intervals and Outlier Detection

## Background Context
TechCo Inc. is facing cybersecurity challenges as employees work remotely due to COVID-19. The Head of Cyber Risk Management needs to analyze remote login data to detect unusual patterns that might indicate security threats.

## The Problem
We have hourly remote login data for one day from the Research & Development department:
- 8:00-9:00: 24 logins
- 9:00-10:00: 21 logins  
- 10:00-11:00: 25 logins
- 11:00-12:00: 29 logins
- 12:00-13:00: 30 logins
- 14:00-15:00: 22 logins
- 16:00-17:00: 27 logins
- 17:00-18:00: 26 logins

## Part 1: Confidence Interval and Outlier Detection

### Key Concepts

**Confidence Interval**: A range of values that we're confident contains the true population mean. A 95% confidence interval means if we repeated this study 100 times, 95 of those intervals would contain the true mean.

**Outliers**: Data points that are significantly different from the rest of the data. They might indicate errors in data collection or genuinely unusual events (like security breaches).

### Mathematical Foundation

**Sample Mean (x̄)**:
```
x̄ = (1/n) × Σxi = (24+21+25+29+30+22+27+26)/8 = 25.50
```

**Sample Standard Deviation (s)**:
```
s = √[(1/(n-1)) × Σ(xi - x̄)²]
s = √[(1/7) × ((24-25.5)² + (21-25.5)² + ... + (26-25.5)²)]
s = 3.16
```

**95% Confidence Interval Formula**:
```
x̄ ± t(α/2)[n-1] × (s/√n)
```

Where:
- t(0.025)[7] = 2.36 (given t-value for 95% confidence with 7 degrees of freedom)
- n = 8 (sample size)

**Calculation**:
```
25.50 ± 2.36 × (3.16/√8) = 25.50 ± 2.36 × 1.118 = 25.50 ± 2.64
Confidence Interval: [22.86, 28.16]
```

### Interpretation
All data points (21, 22, 24, 25, 26, 27, 29, 30) fall within the confidence interval [22.86, 28.16], so **there are no outliers** in this dataset.

## Part 2: Normality Check Using Standardized Data

### Key Concepts

**Standardization (Z-scores)**: Converting data to have mean = 0 and standard deviation = 1. This helps compare data points regardless of original scale.

**Z-score Formula**: z = (x - x̄)/s

**Histogram**: A visual representation showing the frequency distribution of data.

### Standardized Values Calculation

| Original Value | Z-score | Calculation |
|----------------|---------|-------------|
| 24 | -0.47 | (24-25.5)/3.16 |
| 21 | -1.42 | (21-25.5)/3.16 |
| 25 | -0.16 | (25-25.5)/3.16 |
| 29 | 1.11 | (29-25.5)/3.16 |
| 30 | 1.42 | (30-25.5)/3.16 |
| 22 | -1.11 | (22-25.5)/3.16 |
| 27 | 0.47 | (27-25.5)/3.16 |
| 26 | 0.16 | (26-25.5)/3.16 |

### Histogram Analysis

**Bins Used**: Following the rule "Lower Level ≤ Value < Upper Level"
- [-2, -1): 2 values (21, 22)
- [-1, 0): 2 values (24, 25)
- [0, 1): 2 values (26, 27)
- [1, 2): 2 values (29, 30)

### Normality Assessment
The data shows a relatively uniform distribution across bins, which suggests it's **approximately normally distributed** for practical purposes, though with only 8 data points, perfect normality assessment is limited.

## Part 3: Why Check Normality?

### Importance of Normality Assumption

1. **Statistical Test Validity**: Most statistical tests (t-tests, ANOVA, regression) assume normal distribution
2. **Confidence Interval Accuracy**: The confidence interval calculation we used assumes normality
3. **Outlier Detection**: Many outlier detection methods rely on normal distribution assumptions
4. **Parameter Estimation**: Maximum likelihood estimators work best under normality
5. **Predictive Modeling**: Many models assume normally distributed errors

### Practical Implications
- If data isn't normal, we might need non-parametric tests
- Outlier detection methods might be less reliable
- Confidence intervals might not have the claimed coverage probability
- Transformation of data might be necessary

## Business Context
For TechCo's cybersecurity analysis:
- Normal patterns help establish baselines for "typical" login behavior
- Deviations from normal patterns could indicate security threats
- Understanding the distribution helps in setting appropriate alert thresholds
- This analysis provides a foundation for more sophisticated anomaly detection systems
