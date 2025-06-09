[![🗂️ home](https://img.shields.io/badge/home-eee?style=flat)](http://not2much.github.io/se4ai)
[![🗂️ src](https://img.shields.io/badge/src-bbbbbb?style=flat)](/src/)
[![🔱 fork](https://img.shields.io/badge/fork-888888?style=flat&logo=github&logoColor=white)](https://github.com/not2much/se4ai/fork)
<small>&nbsp;[©2025](#)</small><br>
[![🧭 rules](https://img.shields.io/badge/guide-ff6f6f?style=flat)](rules)
[![📂 egs](https://img.shields.io/badge/egs-ff9999?style=flat)](egs)
[![💡 why](https://img.shields.io/badge/motivation-ffcccc?style=flat)](motives) &nbsp;&nbsp;
[![🐚 sh](https://img.shields.io/badge/sh-f1c40f?style=flat)](sh)
[![🐍 python](https://img.shields.io/badge/python-f39c12?style=flat)](python)
[![🛠 se](https://img.shields.io/badge/se-e67e22?style=flat)](se) &nbsp;&nbsp;
[![📐 math](https://img.shields.io/badge/maths-7fdb7f?style=flat)](maths)
[![🧠 ai](https://img.shields.io/badge/ai-2ecc71?style=flat)](a)
[![📦 apps](https://img.shields.io/badge/apps-27ae60?style=flat)](apps) &nbsp;&nbsp;

# Artificial Intelligence (AI) Concepts:

## Descriptive statistics:
* Example: `Num` (calculates mean, standard deviation, min, max)
* Notes: AI often uses descriptive statistics to summarize and describe the main
  features of a dataset, providing insights into the data's characteristics before
  applying more complex models.

## Similarity measures:
* Example: `xdist(data, row1, row2)`
* Notes: Functions that quantify how alike two data points are. In AI, these are
  crucial for tasks like clustering, recommendation systems, and nearest-neighbor algorithms.

## Feature scaling:
* Example: `norm(num,v)`
* Notes: A data preprocessing step that standardizes the range of independent
  features. This is essential for many AI algorithms (like k-nearest neighbors or SVMs)
  that are sensitive to the magnitude of feature values.

## Clustering algorithms (K-means++):
* Example: `def kpp(data, k=None, rows=None):`
* Notes: Unsupervised learning algorithms that group similar data points together
  into clusters. K-means++ is an initialization strategy for K-means that aims to
  select initial centroids that are far apart, leading to better clustering results.

## Initialization strategies for optimization:
* Example: `kpp(data)`
* Notes: Techniques used to set the starting points or parameters for an optimization
  algorithm. A good initialization can significantly impact the speed and quality
  of convergence for iterative optimization processes.

## Naïve Bayes classification:
* Example: `def pdf(col,v, prior=0):` and `def like(data, row, nall=2, nh=100):`
* Notes: A probabilistic supervised learning algorithm based on Bayes' theorem,
  with a "naïve" assumption of independence between features. It's often used
  for text classification and spam filtering due to its simplicity and efficiency.

## Handling of missing values ("?"):
* Example: `if v != "?":`
* Notes: Strategies for dealing with absent or unspecified data points in a dataset.
  Common methods include imputation (filling in missing values) or simply ignoring
  records with missing values, as seen here.

## Active learning strategies (exploration vs. exploitation):
* Example: `the.Acq` option (`xploit` or `xplore` or `adapt`)
* Notes: A machine learning approach where the algorithm can interactively query
  a user or other information source to obtain the desired outputs at new data points.
  It's useful when labeled data is scarce or expensive to obtain.

## Uncertainty sampling:
* Example: Implicit in `_acquire` logic via `q`
* Notes: An active learning strategy where the algorithm selects the data points
  about which it is most "uncertain" (e.g., those closest to a decision boundary)
  to be labeled next, aiming to maximize information gain.

## Decision tree learning:
* Example: `def tree(data, Klass=Num, Y=None, how=None):`
* Notes: A supervised learning method used for classification and regression.
  It builds a tree-like model of decisions, where each internal node represents
  a "test" on an attribute, each branch represents the outcome of the test, and
  each leaf node represents a class label or a predicted value.

## Information gain:
* Example: Implicit in `cuts` function which selects splits that minimize `div`
* Notes: In decision tree learning, information gain is a metric used to select the
  best attribute for splitting data at each node. It measures the reduction in entropy
  (or impurity) achieved by splitting the dataset based on that attribute.

## Pruning (decision trees):
* Example: `if the.leaf <= lhs.n <= len(xys) - the.leaf:`
* Notes: A technique used in decision tree learning to reduce the complexity of the
  tree by removing branches that have low predictive power or are likely to
  overfit the training data. `the.leaf` sets a minimum size for a leaf node.

## Feature importance:
* Example: Implicitly determined by the `cuts` function
* Notes: A concept that ranks features based on their utility in predicting the
  target variable. In decision trees, features that are chosen for splits higher up
  in the tree (because they yield significant information gain) are considered more important.

## Non-parametric statistics:
* Example: `bootstrap(vals1, vals2)` and `cliffs(vals1,vals2)`
* Notes: Statistical methods that do not rely on assumptions about the probability
  distribution of the population (e.g., that data is normally distributed). They
  are often used when data is skewed or when sample sizes are small.

## A/B testing:
* Example: `eg__stats`
* Notes: A randomized controlled experiment involving two variants (A and B) to
  determine which one performs better. In AI, it's used to compare different
  models, algorithms, or feature sets.

## Statistical ranking (Scott-Knott test):
* Example: `def scottKnott(rxs, eps=0, reverse=False):`
* Notes: A non-parametric statistical method for grouping treatments (e.g., different
  algorithms) into statistically distinct ranks. Treatments within the same rank
  are not significantly different from each other, but are different from those in other ranks.

## Comparison of distributions:
* Example: `scottKnott`
* Notes: Analyzing whether two or more sets of data come from the same underlying
  probability distribution or if there are statistically significant differences between them.

## Model-assisted sampling:
* Example: `acquired(data)`
* Notes: A sampling strategy where a statistical model is used to improve the
  efficiency or accuracy of sampling, often by guiding the selection of samples
  that are expected to provide the most information.

## Predictive modeling:
* Example: `leaf(t,z).ys.mu`
* Notes: The process of creating a model (e.g., a decision tree) that can forecast
  future outcomes or predict unknown values based on historical data.

## Search space exploration:
* Example: `fmap` and `landscape`
* Notes: The process of systematically examining potential solutions within the
  set of all possible solutions (the search space) to find an optimal or
  near-optimal solution.

## Multi-objective optimization:
* Example: The program aims to optimize 'Throughput+' and 'Latency-'.
* Notes: An optimization problem involving more than one objective function
  to be simultaneously optimized. Often, these objectives conflict, requiring
  trade-offs to find a set of Pareto optimal solutions.

## Heuristic search:
* Example: The `acquires` function uses heuristics like `_guess`
* Notes: Search algorithms that employ a heuristic function to guide the search process,
  aiming to find a good solution in a reasonable amount of time, though not always
  guaranteeing the optimal solution.

## Optimization landscapes:
* Example: `def landscapes(data):`
* Notes: A conceptual representation of the search space of an optimization problem,
  where "peaks" represent good solutions (e.g., low `ydist`) and "valleys" represent
  poor solutions. Algorithms navigate this landscape to find optimal points.

## Hyperparameters:
* Example: `the.Few`, `the.leaf`, `the.p`, `the.k`, `the.m`
* Notes: Parameters whose values are set before the learning process begins, and that
  control the learning process itself (e.g., learning rate, regularization strength,
  tree depth). They are distinct from model parameters learned during training.
