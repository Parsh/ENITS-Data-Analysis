# Question 12 Explanation: Non-Linear Regression and Logarithmic Transformation

## Background Context
PharmResearch Inc. operates a highly sensitive pharmaceutical production process vulnerable to cyber attacks. Jimmy Chow, the Cyber Data Analyst, needs to develop a regression model to predict the costs of production interruptions based on downtime duration. The relationship appears to be non-linear, requiring advanced mathematical modeling techniques.

## The Problem
**Objective**: Model the relationship between interruption time (x, in minutes) and costs (y, in thousand €)

**Advanced Model Proposed**: y = β₀ × x^β₁ × e^ε

This is a **power function model** with multiplicative error, which is more sophisticated than simple linear regression.

## Key Concepts in Non-Linear Regression

### Why Use Non-Linear Models?
1. **Real-world relationships**: Many business relationships are non-linear
2. **Cost functions**: Often exhibit exponential or power relationships
3. **Better fit**: Can capture curved patterns that linear models miss
4. **Economic theory**: Many economic relationships follow power laws

### Power Function Characteristics
- **y = β₀ × x^β₁**: Power function form
- **β₀**: Scale parameter (multiplicative constant)
- **β₁**: Shape parameter (elasticity)
- **Multiplicative error**: e^ε instead of additive ε

## Model Linearization Process

### Step 1: Apply Natural Logarithm
Starting with: **y = β₀ × x^β₁ × e^ε**

Take natural log of both sides:
```
ln(y) = ln(β₀ × x^β₁ × e^ε)
```

### Step 2: Use Logarithm Properties
```
ln(y) = ln(β₀) + ln(x^β₁) + ln(e^ε)
ln(y) = ln(β₀) + β₁×ln(x) + ε
```

### Step 3: Define New Variables
Let:
- **Y = ln(y)**: Transformed dependent variable
- **X = ln(x)**: Transformed independent variable  
- **α = ln(β₀)**: Transformed intercept
- **β₁**: Same slope parameter

**Linear Model**: Y = α + β₁×X + ε

### Critical Understanding
**What the transformation means**:
- Original model is multiplicative and non-linear
- Transformed model is additive and linear
- Can use standard linear regression on transformed variables
- Must transform back to get original scale predictions

## Data Analysis and Calculations

### Data Transformation

| y (cost) | x (time) | ln(y) | ln(x) | ln(x)×ln(y) | [ln(x)]² |
|----------|----------|-------|-------|-------------|----------|
| 28 | 2.3 | 3.33 | 0.83 | 2.78 | 0.69 |
| 29 | 2.4 | 3.37 | 0.88 | 2.95 | 0.77 |
| 26 | 2.2 | 3.26 | 0.79 | 2.57 | 0.62 |
| 30 | 2.5 | 3.40 | 0.92 | 3.12 | 0.84 |
| 31 | 2.6 | 3.43 | 0.96 | 3.28 | 0.91 |
| 27 | 2.3 | 3.30 | 0.83 | 2.75 | 0.69 |
| 29 | 2.4 | 3.37 | 0.88 | 2.95 | 0.77 |
| 30 | 2.4 | 3.40 | 0.88 | 2.98 | 0.77 |
| **Totals** | | **26.86** | **6.95** | **23.36** | **6.06** |

### Regression Calculations

**Using Linear Regression Formulas on Transformed Data**:

**Slope (β₁)**:
```
b₁ = [n×Σ(ln x × ln y) - Σ(ln x)×Σ(ln y)] / [n×Σ(ln x)² - (Σln x)²]
b₁ = 1.07
```

**Intercept (ln β₀)**:
```
Mean of ln(y) = 26.86/8 = 3.36
Mean of ln(x) = 6.95/8 = 0.87

ln(b₀) = 3.36 - 1.07×0.87 = 2.43
Therefore: b₀ = e^2.43 = 11.36
```

### Final Model

**In Logarithmic Form**: ln(y) = 2.43 + 1.07×ln(x)

**In Original Form**: **y = 11.36 × x^1.07**

## Model Interpretation

### Mathematical Interpretation

**Power Parameter (1.07)**:
- **Elasticity**: 1% increase in time leads to 1.07% increase in cost
- **Slightly increasing returns**: Each additional minute has slightly more impact
- **Near-linear**: Close to 1.0 suggests nearly proportional relationship

**Scale Parameter (11.36)**:
- **Base multiplier**: When x = 1 minute, cost = 11.36 thousand €
- **Units**: Thousand € per minute (approximately)

### Business Interpretation

**Cost Structure**:
- Costs increase slightly faster than proportionally with time
- Each additional minute of downtime becomes slightly more expensive
- Model captures the compounding nature of production disruptions

**Practical Examples**:
- 2 minutes: y = 11.36 × 2^1.07 = 24.0 thousand €
- 3 minutes: y = 11.36 × 3^1.07 = 36.4 thousand €
- 4 minutes: y = 11.36 × 4^1.07 = 49.1 thousand €

## Advanced Analysis Considerations

### Model Validation

**Goodness of Fit**:
- Calculate R² for transformed model
- Check residual patterns
- Compare with linear model performance

**Assumptions**:
1. **Log-normality**: ln(y) should be normally distributed
2. **Homoscedasticity**: Constant variance in transformed space
3. **Independence**: Observations independent
4. **Correct functional form**: Power function appropriate

### Advantages of Power Model

**Mathematical Benefits**:
1. **Flexibility**: Can capture various curved relationships
2. **Interpretability**: Elasticity has clear economic meaning
3. **Multiplicative errors**: Often more realistic than additive
4. **Scale invariance**: Relationships preserved under scaling

**Business Benefits**:
1. **Realistic**: Many cost functions follow power laws
2. **Predictive**: Better extrapolation than linear models
3. **Policy insights**: Elasticity guides decision making
4. **Risk assessment**: Better understanding of cost escalation

### Limitations and Cautions

**Statistical Limitations**:
1. **Transformation bias**: Predictions in original scale may be biased
2. **Complexity**: More difficult to interpret than linear models
3. **Assumption sensitivity**: Requires careful validation
4. **Sample size**: Needs adequate data for reliable estimation

**Business Limitations**:
1. **Extrapolation risk**: Power functions can grow very rapidly
2. **Domain restrictions**: May not apply to all time ranges
3. **Causation**: Still correlation, not necessarily causation
4. **Model selection**: Alternative non-linear forms might fit better

## Strategic Applications

### Risk Management

**Cost Prediction**:
- More accurate forecasting of incident costs
- Better understanding of escalation patterns
- Improved budget planning for contingencies

**Decision Support**:
- Investment decisions in prevention systems
- Response time optimization
- Resource allocation priorities

### Operational Improvements

**Response Planning**:
- Prioritize rapid response based on escalating costs
- Set maximum acceptable downtime thresholds
- Develop staged response protocols

**Prevention Investment**:
- Justify cybersecurity investments using cost models
- Compare prevention costs vs predicted incident costs
- ROI analysis for security measures

## Advanced Modeling Recommendations

### Model Enhancements
1. **Multiple variables**: Include incident type, time of day, etc.
2. **Piecewise models**: Different parameters for different time ranges
3. **Stochastic models**: Account for uncertainty in parameters
4. **Machine learning**: Explore neural networks for complex patterns

### Validation Approaches
1. **Cross-validation**: Test model on held-out data
2. **Sensitivity analysis**: Test robustness to outliers
3. **Alternative models**: Compare with exponential, polynomial forms
4. **Real-world testing**: Validate predictions against actual incidents

This analysis demonstrates how advanced mathematical modeling can provide deeper insights into business relationships, enabling more sophisticated risk management and decision-making in cybersecurity contexts.
