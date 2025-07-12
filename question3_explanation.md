# Question 3 Explanation: Queuing Theory and Server Capacity Analysis

## Background Context
A large cybersecurity firm manages a central server that stores sensitive client information. Security analysts from six regional offices need to access this database for investigations. The current system allows only 3 simultaneous users, and when at capacity, additional users are denied access with no waiting queue. Management needs to understand system performance and plan for future growth.

## The Problem
**Current System Parameters**:
- **Arrival rate (λ)**: 42 login attempts per hour (follows Poisson distribution)
- **Service rate per server (μ)**: 20 logins per hour  
- **Number of servers (k)**: 3
- **System type**: No waiting queue (blocked calls are lost)

## Key Concepts in Queuing Theory

### Queuing System Notation: M/G/k
- **M**: Markovian (Poisson) arrivals - random arrival times
- **G**: General service time distribution  
- **k**: Number of parallel servers

### Important Metrics
- **ρ = λ/μ**: Traffic intensity (utilization rate per server)
- **P_j**: Probability that exactly j servers are busy
- **P_k**: Blocking probability (all servers busy)
- **L**: Average number of servers in use

## Part 1: Probability Calculations for Each Number of Busy Servers

### Mathematical Foundation

For an M/G/k system with no waiting queue, the probability of exactly j servers being busy is:

```
P_j = [(λ/μ)^j / j!] / [Σ(λ/μ)^i / i!] for i=0 to k
```

### Step-by-Step Calculation

**Given**: λ = 42, μ = 20, so λ/μ = 42/20 = 2.1

**Step 1**: Calculate numerators for each state

| j | (λ/μ)^j | j! | (λ/μ)^j / j! |
|---|---------|----|-----------   |
| 0 | 2.1^0 = 1.0000 | 1 | 1.0000 |
| 1 | 2.1^1 = 2.1000 | 1 | 2.1000 |
| 2 | 2.1^2 = 4.4100 | 2 | 2.2050 |
| 3 | 2.1^3 = 9.2610 | 6 | 1.5435 |

**Sum** = 6.8485

**Step 2**: Calculate probabilities

| j | P_j | Interpretation |
|---|-----|----------------|
| 0 | 1.0000/6.8485 = **0.1460** | 14.60% of time no servers busy |
| 1 | 2.1000/6.8485 = **0.3066** | 30.66% of time 1 server busy |
| 2 | 2.2050/6.8485 = **0.3220** | 32.20% of time 2 servers busy |
| 3 | 1.5435/6.8485 = **0.2254** | 22.54% of time all 3 servers busy |

## Part 2: Probability of Being Denied Access

### Key Concept
**Blocking Probability**: This occurs when all servers are busy and a new user tries to access the system.

**Answer**: P₃ = **0.2254** or **22.54%**

### Business Interpretation
- Nearly 1 in 4 users (22.54%) will be denied access
- This represents significant inefficiency and user frustration
- Lost productivity and potential security delays

## Part 3: Average Number of Access Lines in Use

### Mathematical Formula
```
L = (λ/μ) × (1 - P_k)
```

Where:
- λ/μ = average demand per server
- (1 - P_k) = probability that not all servers are busy

### Calculation
```
L = (42/20) × (1 - 0.2254) = 2.1 × 0.7746 = 1.6267
```

**Answer**: On average, **1.63 servers** are in use at any given time.

### Interpretation
- System utilization: 1.63/3 = 54.3%
- Despite blocking 22.54% of users, servers are only moderately utilized
- This suggests the blocking is due to the "no queue" policy, not server overload

## Part 4: Future Planning Analysis

### New Requirements
- **Increased arrival rate**: λ = 50 login attempts per hour
- **Constraint**: Blocking probability should not exceed current level (22.54%)
- **Question**: How many servers needed?

### Analysis for k = 4 Servers

**Step 1**: Calculate probabilities with λ = 50, μ = 20, k = 4
λ/μ = 50/20 = 2.5

| j | (λ/μ)^j / j! | P_j |
|---|-------------|-----|
| 0 | 1.0000 | 0.0921 |
| 1 | 2.5000 | 0.2303 |
| 2 | 3.1250 | 0.2878 |
| 3 | 2.6042 | 0.2399 |
| 4 | 1.6276 | 0.1499 |

**Sum** = 10.8568

**Step 2**: Check blocking probability
P₄ = 0.1499 = **14.99%**

**Step 3**: Compare with current system
14.99% < 22.54% ✓

**Answer**: **4 servers** are sufficient to handle 50 requests/hour while maintaining better performance than the current system.

## Practical Business Insights

### Current System Problems
1. **High blocking rate**: 22.54% of users denied access
2. **Low server utilization**: Only 54.3% of capacity used
3. **No queue system**: Users must retry, causing frustration

### Recommendations
1. **Immediate**: Add 1 server (total of 4) to handle growth
2. **Long-term**: Consider implementing a queue system
3. **Monitoring**: Track actual arrival patterns vs. Poisson assumption
4. **Capacity planning**: Regular analysis as client base grows

### Queuing Theory Applications in Cybersecurity
1. **Incident Response**: Managing multiple security alerts
2. **Access Control**: Balancing security and accessibility
3. **Network Traffic**: Understanding bandwidth limitations
4. **Help Desk**: Sizing support teams for security inquiries

### Key Takeaways
- Queuing theory helps optimize resource allocation
- Simple probability models can guide important business decisions
- Balance between service quality and resource costs
- Mathematical analysis provides objective basis for capacity planning
