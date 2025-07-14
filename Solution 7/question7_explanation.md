# Question 7 Explanation: Queuing Analysis for City Cab Dispatcher System

## Background Context
City Cab Inc. operates a taxi dispatch system with shared phone lines. When both dispatchers are busy, callers receive a busy signal and must either call back later or use a competitor. This is a classic queuing problem where the company needs to balance service quality (minimize busy signals) with operational costs (number of dispatchers).

## The Problem
**Current System Parameters**:
- **Arrival rate (λ)**: 40 calls per hour (Poisson distribution)
- **Service rate per dispatcher (μ)**: 30 calls per hour
- **Current dispatchers**: 2
- **No waiting queue**: Busy calls are lost (blocked)

**Key Questions**: Determine system performance metrics and optimal dispatcher count.

## Key Concepts in Queuing Theory for Service Systems

### System Type: M/M/k/k (Erlang Loss Model)
- **First M**: Markovian (Poisson) arrivals
- **Second M**: Markovian (exponential) service times  
- **k**: Number of servers
- **k**: System capacity (no waiting queue)

### Traffic Intensity
**ρ = λ/μ = 40/30 = 1.33**
This represents the average number of busy dispatchers if there were infinite capacity.

## Part 1: Probability Both Dispatchers Idle

### Mathematical Framework
For an M/M/k/k system, the probability of exactly i busy servers is:

```
Pi = [(λ/μ)^i / i!] / [Σ(λ/μ)^j / j!] for j=0 to k
```

### Calculation for k = 2 Dispatchers

**Step 1**: Calculate numerators for each state

| State (i) | (λ/μ)^i | i! | (λ/μ)^i / i! |
|-----------|---------|----|-----------   |
| 0 | 1.33^0 = 1.0000 | 1 | 1.0000 |
| 1 | 1.33^1 = 1.3333 | 1 | 1.3333 |
| 2 | 1.33^2 = 1.7778 | 2 | 0.8889 |

**Sum** = 3.2222

**Step 2**: Calculate probability both idle
```
P₀ = 1.0000 / 3.2222 = 0.3104
```

**Answer**: **31.04%** of the time both dispatchers are idle.

### Business Interpretation
- Nearly one-third of the time, the system has excess capacity
- This suggests potential for either handling more calls or reducing staff during low-demand periods
- High idle time indicates the system isn't fully utilized

## Part 2: Probability Both Dispatchers Busy

### Calculation
```
P₂ = 0.8889 / 3.2222 = 0.2758
```

**Answer**: **27.58%** of the time both dispatchers are busy.

### Business Interpretation
- More than 1 in 4 times, new callers receive busy signals
- This represents significant customer service issues
- Lost calls likely translate to lost business revenue

## Part 3: Busy Signal Probability for Different Numbers of Dispatchers

### Key Concept
**Blocking Probability** = Probability that all servers are busy = P_k

### For k = 3 Dispatchers

**Calculation**:
| State (i) | (λ/μ)^i / i! |
|-----------|-------------|
| 0 | 1.0000 |
| 1 | 1.3333 |
| 2 | 0.8889 |
| 3 | 0.3951 |

**Sum** = 3.6173

```
P₃ = 0.3951 / 3.6173 = 0.1092
```

**Answer for 3 dispatchers**: **10.92%** busy signal rate

### For k = 4 Dispatchers

**Calculation**:
| State (i) | (λ/μ)^i / i! |
|-----------|-------------|
| 0 | 1.0000 |
| 1 | 1.3333 |
| 2 | 0.8889 |
| 3 | 0.3951 |
| 4 | 0.1317 |

**Sum** = 3.7490

```
P₄ = 0.1317 / 3.7490 = 0.0351
```

**Answer for 4 dispatchers**: **3.51%** busy signal rate

### Summary of Busy Signal Rates

| Number of Dispatchers | Busy Signal Probability |
|-----------------------|------------------------|
| 2 (current) | 27.58% |
| 3 | 10.92% |
| 4 | 3.51% |

## Part 4: Meeting Service Goal

### Management Constraint
**Goal**: No more than 12% of callers should receive busy signals

### Analysis
From our calculations:
- **2 dispatchers**: 27.58% > 12% ❌
- **3 dispatchers**: 10.92% < 12% ✓
- **4 dispatchers**: 3.51% < 12% ✓

**Answer**: **3 dispatchers** minimum to meet the 12% goal.

### Cost-Benefit Consideration
While 4 dispatchers provide even better service (3.51% vs 10.92%), the marginal improvement might not justify the additional cost. The decision between 3 and 4 dispatchers should consider:
- Cost of additional dispatcher
- Value of improved customer satisfaction
- Competitive positioning requirements

## Comprehensive Business Analysis

### Performance Comparison

| Metric | 2 Dispatchers | 3 Dispatchers | 4 Dispatchers |
|--------|---------------|---------------|---------------|
| Busy Signal Rate | 27.58% | 10.92% | 3.51% |
| Service Level | Poor | Good | Excellent |
| Customer Satisfaction | Low | Moderate | High |
| Staffing Cost | Low | Medium | High |

### Revenue Impact Analysis

**Lost Call Calculation**:
- Current system: 40 calls/hour × 27.58% = **11.03 lost calls/hour**
- With 3 dispatchers: 40 calls/hour × 10.92% = **4.37 lost calls/hour**
- Improvement: 11.03 - 4.37 = **6.66 additional calls served/hour**

**Business Case for Additional Dispatcher**:
If average revenue per call is R, then additional revenue = 6.66R per hour
This additional revenue should exceed the cost of the third dispatcher.

### Strategic Recommendations

#### Immediate Actions
1. **Add 1 dispatcher** to meet service goal (3 total)
2. **Monitor call patterns** for peak/off-peak variations
3. **Track lost call impact** on revenue and customer retention

#### Advanced Considerations
1. **Time-varying demand**: Different staffing for different times of day
2. **Call-back system**: Allow customers to request call-backs during busy periods
3. **Predictive staffing**: Use forecasting to optimize dispatcher schedules
4. **Technology solutions**: Automated dispatch systems, mobile apps

### Queuing Theory Applications

#### Other Business Applications
1. **Customer Service Centers**: Sizing support teams
2. **Emergency Services**: Ambulance/fire department capacity planning
3. **Manufacturing**: Machine capacity and bottleneck analysis
4. **IT Systems**: Server capacity and response time optimization

#### Key Insights
- **Trade-offs**: Service quality vs operational costs
- **Non-linear improvements**: Each additional server provides diminishing returns
- **Mathematical precision**: Queuing theory provides exact calculations for decision-making
- **Strategic value**: Quantitative analysis supports business decisions

### Limitations and Assumptions
1. **Poisson arrivals**: Assumes random, independent call timing
2. **Exponential service**: Assumes constant average service rate
3. **No abandonment**: Model assumes lost calls don't retry immediately
4. **Steady state**: Assumes system reaches equilibrium
5. **Homogeneous service**: All dispatchers have same capability

This analysis demonstrates how mathematical modeling can optimize service operations while balancing customer satisfaction and operational efficiency.
