[![🏠 home](https://img.shields.io/badge/home-cccccc?style=flat)](/README)
[![🗂️ src](https://img.shields.io/badge/src-aaaaaa?style=flat)](/src/)
[![© 2025](https://img.shields.io/badge/©︎_2025-cccccc?style=flat)](#)
[![🔱 fork](https://img.shields.io/badge/fork-grey?style=flat&logo=github&logoColor=white)](https://github.com/not2much/se4ai/fork)<br>
[![🧭 rules](https://img.shields.io/badge/guide-88c0d0?style=flat)](rules)
[![📂 egs](https://img.shields.io/badge/egs-81a1c1?style=flat)](egs)
[![💡 why](https://img.shields.io/badge/motivation-eee85c?style=flat)](motives)
[![📐 math](https://img.shields.io/badge/maths-8faadc?style=flat)](maths)
[![🐍 python](https://img.shields.io/badge/python-a4c639?style=flat)](python)
[![🛠 se](https://img.shields.io/badge/se-f36f6f?style=flat)](se)
[![🧠 ai](https://img.shields.io/badge/ai-c17dc6?style=flat)](a)
[![📦 apps](https://img.shields.io/badge/apps-faa857?style=flat)](apps)

# Not 2 Much Maths

Core idea. y=f(x). x chearp to find that y.

used a lot (any pre-rocessor that clusters data or does feature selection).

# Maths Concepts:


## Arithmetic operations
(addition, subtraction, multiplication, division, exponentiation):
* Example: `num.mu += inc * (d / num.n)`
* Notes: These are fundamental mathematical operations. In programming, they are
  directly translated using operators like `+`, `-`, `*`, `/`, `**` (for exponentiation).
  Understanding their order of operations is crucial for correct calculations.

## Absolute value:
* Example: `abs(lt - gt)`
* Notes: The absolute value of a number is its distance from zero, always non-negative.
  It's used when the magnitude of a difference is important, regardless of its sign.


## Real numbers:
* Example: `p=math.pi` in `eg__o` output `{:name alan, :age 41, :p 3.14}`
* Notes: Real numbers include all rational (integers, fractions) and irrational numbers
  (like pi, square root of 2). In Python, they are typically represented as `float` types.

## Mean (average):
* Example: `num.mu=0` and `num.mu += inc * (d / num.n)`
* Notes: The mean is a measure of central tendency, calculated as the sum of all values
  divided by the count of values. It represents the "typical" value in a dataset.

## Summation:
* Example: `sum(p*math.log(p,2) for n in i.has.values() if (p:=n/i.n) > 0)`
* Notes: Summation is the operation of adding a sequence of numbers. In Python,
  the built-in `sum()` function is commonly used, often with generator expressions
  or list comprehensions for complex sums.

## Probability:
* Example: `p:=n/i.n`
* Notes: Probability quantifies the likelihood of an event occurring. It is a value
  between 0 and 1, where 0 indicates impossibility and 1 indicates certainty.
  In `bing1.py`, it's often calculated as `count_of_event / total_count`.

## Logarithms:
* Example: `math.log(p,2)`
* Notes: A logarithm is the inverse operation to exponentiation. `log_b(x)` asks
  "to what power must `b` be raised to get `x`?". Here, `math.log(p,2)` calculates
  the logarithm base 2, often used in information theory (e.g., entropy).

## Entropy:
* Example: `_ent = lambda: -sum(p*math.log(p,2) for n in i.has.values() if (p:=n/i.n) > 0)`
* Notes: In information theory, entropy measures the impurity or uncertainty in a set
  of data. For a discrete probability distribution, it's calculated as the negative
  sum of `p * log2(p)` for each probability `p`. Higher entropy means more diversity/uncertainty.

## Square root:
* Example: `** .5`
* Notes: The square root of a number `x` is a number `y` such that `y*y = x`. In Python,
  it can be calculated using `math.sqrt()` or by raising to the power of 0.5 (`** 0.5`).
  It's fundamental for calculating standard deviation.

## Gaussian distribution (normal distribution):
* Example: `random.gauss(10,2)`
* Notes: Also known as the bell curve, it's a symmetric probability distribution
  that is very common in nature and statistics. It's characterized by its mean (center)
  and standard deviation (spread). `random.gauss` generates numbers following this distribution.

## Random number generation:
* Example: `random.seed(the.rseed)`
* Notes: The process of generating a sequence of numbers that appear random.
  `random.seed()` initializes the random number generator, ensuring reproducibility
  of results for debugging and comparisons.

## Minkowski distance:
* Example: `def minkowski(src):`
* Notes: A generalization of Euclidean and Manhattan distances. For two points
  $(x_1, ..., x_n)$ and $(y_1, ..., y_n)$, and a parameter `p`, the Minkowski
  distance is $( \sum_{i=1}^{n} |x_i - y_i|^p )^{1/p}$. When `p=1`, it's Manhattan
  distance; when `p=2`, it's Euclidean distance. `the.p` controls this parameter.

## Normalization (Min-Max scaling):
* Example: `(v-num.lo) / (num.hi-num.lo + 1/big)`
* Notes: A data preprocessing technique that rescales numerical features to a
  standard range (typically 0 to 1). This is crucial for distance-based algorithms
  to prevent features with larger ranges from dominating the distance calculations.

## Geometric projection:
* Example: `return (A*A + C*C - B*B) / (C + 1/big)`
* Notes: This involves projecting a point onto a line or plane. In `bing1.py`,
  it's used to project data points onto a line defined by two "extreme" points
  (a and b) in the data landscape. This helps in ordering points relative to these extremes.

## Hypothesis testing:
* Example: `bootstrap(vals1, vals2)`
* Notes: A statistical method used to determine if there is enough evidence in a
  sample data to infer that a certain condition is true for the entire population.
  It typically involves a null hypothesis and an alternative hypothesis, and
  calculating a p-value to decide whether to reject the null hypothesis.

## Significance level:
* Example: `(1- the.Boots)`
* Notes: In hypothesis testing, the significance level (alpha, often 0.05 or 0.01)
  is the probability of rejecting the null hypothesis when it is actually true
  (Type I error). `the.Boots` (bootstrap samples) is related to the confidence level,
  so `1 - the.Boots` would be the Type I error rate or significance threshold.

## Effect size:
* Example: `abs(lt - gt)/n < the.Cliffs`
* Notes: Effect size measures the magnitude of the difference between two groups
  or the strength of a relationship between two variables. Unlike statistical
  significance, which tells you if an effect exists, effect size tells you how
  large the effect is. Cliffs Delta (used here) is a non-parametric effect size measure.


