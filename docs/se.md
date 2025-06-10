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

# Software Engineering (SE) Concepts:

## Data structures (e.g., records/structs):
* Example: `class o:`
* Notes: Ways of organizing and storing data efficiently. `class o` acts as a simple
  record or struct, bundling related data fields together.

## File I/O (reading files):
* Example: `doc(file)`
* Notes: Input/Output operations related to files, allowing programs to read data
  from external files or write data to them.

## Error handling principles:
* Example: `try...except Exception as _:`
* Notes: Strategies for designing robust software that can gracefully respond to
  unexpected inputs, system failures, or other runtime problems without crashing.

## Data parsing:
* Example: `def atom(x):`
* Notes: The process of converting data from one format (e.g., raw text from a file)
  into another more usable format (e.g., Python data types like int, float).

## CSV format:
* Example: `EXAMPLE="""Max_spout, hashing, Spliters, Counters, Throughput+, Latency-..."`
* Notes: Comma-Separated Values, a common plain-text file format for tabular data,
  where columns are delimited by commas and rows by newlines.

## Data schemas:
* Example: `Cols(names)`
* Notes: A formal description of the structure of data, including column names,
  data types, and relationships. It defines what data is expected and how it's organized.

## Feature types (numerical, symbolic):
* Example: `(Num if s[0].isupper() else Sym)`
* Notes: Classification of data attributes. Numerical features are quantitative (e.g., age, salary);
  symbolic (or categorical) features are qualitative (e.g., name, hashing 'on'/'off').

## Feature categorization (independent, dependent):
* Example: `if s[-1] != "X": (y if s[-1] in "+-" else x).append(all[-1])`
* Notes: Distinguishing between input features (independent variables, `x`) that predict
  or explain outcomes, and output/target features (dependent variables, `y`) that are being predicted.

## Data summarization:
* Example: `Num(inits=[],at=0, txt=" ", rank=0)` and `Sym( inits=[], at=0, txt=" ")`
* Notes: The process of condensing large datasets into smaller, more manageable
  summaries that highlight key characteristics (e.g., mean, standard deviation for numbers;
  counts, mode for symbols).

## Data encapsulation:
* Example: `def Data(inits):`
* Notes: The bundling of data (attributes) and the methods that operate on the data
  into a single unit (an object). It hides the internal implementation details from the user.

## Data loading:
* Example: `Data(csv(doc(file) if file else lines(EXAMPLE)))`
* Notes: The process of reading data from a source (like a file or a string) into
  a program's memory structure for processing.

## Incremental updates to data structures:
* Example: `add(data2,row)` and `sub(data2, row)`
* Notes: Modifying data structures by adding or removing individual elements
  while maintaining the integrity of the overall structure and its summary statistics efficiently.

## Data integrity checks:
* Example: `assert mids == mid(data2)`
* Notes: Procedures or assertions used to ensure that data remains consistent,
  accurate, and valid throughout its lifecycle within a system.

## Copying data structures (cloning):
* Example: `def clone(data, rows=[]):`
* Notes: Creating a duplicate of an existing data structure. A "deep clone" copies
  all nested components, while a "shallow clone" may share references to nested objects.

## Distance metrics:
* Example: `def minkowski(src):`
* Notes: Functions that quantify the "distance" or dissimilarity between two data points.
  The choice of metric depends on the data type and the problem.

## Sorting algorithms:
* Example: `return sorted(rows or data._rows, key=lambda row: ydist(data,row))`
* Notes: Algorithms used to arrange elements of a list or array in a specific order
  (e.g., ascending or descending). Python's `sorted()` function uses Timsort.

## Sampling techniques:
* Example: `shuffle(rows or data._rows)`
* Notes: Methods for selecting a subset of data points from a larger dataset.
  Used to reduce computation time or for statistical analysis (e.g., bootstrapping).

## Recursive algorithms:
* Example: `def nodes(data1, lvl=0, key=None):`
* Notes: Algorithms that solve a problem by calling themselves repeatedly with
  smaller instances of the same problem until a base case is reached.

## Tree data structures:
* Example: `data.kids = []`
* Notes: Hierarchical data structures consisting of nodes connected by edges.
  Trees are widely used for organizing data (e.g., file systems, decision trees).

## Integration of different modules/functions:
* Example: `acquired(data)` calls `acquires(data)` and `tree(clone(data, ...))`
* Notes: Combining distinct software components or functions to work together
  as a unified system, often through well-defined interfaces.

## Statistical testing frameworks:
* Example: `bootstrap(vals1, vals2)`
* Notes: Libraries or sets of functions that implement various statistical tests
  (e.g., hypothesis tests, non-parametric tests) to analyze data and draw conclusions.

## Ranking algorithms:
* Example: `scottKnott`
* Notes: Algorithms that assign a rank (order) to items based on certain criteria.
  The Scott-Knott test is a statistical ranking method for comparing multiple treatments.

## Iterative algorithms:
* Example: `while len(todo) > 2 and n < the.Stop:`
* Notes: Algorithms that repeat a sequence of steps until a certain condition is met.
  They are foundational for many optimization and search processes.

## Greedy algorithms:
* Example: The selection of `hi` (best guess) in `acquires` based on `_guess` score.
* Notes: Algorithms that make the locally optimal choice at each step with the hope
  that this choice will lead to a globally optimal solution. They are simple but
  don't always guarantee the best overall result.

## Configuration management:
* Example: `the = o(**{m[1]: atom(m[2]) ...})`
* Notes: The practice of systematically organizing, storing, and accessing program
  settings and options (e.g., from command-line arguments or configuration files).

## Command-line interfaces (CLI):
* Example: `def cli(d):`
* Notes: A text-based interface for interacting with a computer program, where
  users type commands and arguments rather than using graphical elements.

## Documentation strings:
* Example: The `"""..."""` at the top of `bing1.py`
* Notes: Multi-line string literals used in Python to explain the purpose and usage
  of modules, classes, methods, or functions. Accessed via `__doc__`.

## Test automation:
* Example: `def eg__all(_):`
* Notes: Using software to execute tests, compare actual outcomes with predicted
  outcomes, and report results. It helps ensure code quality and consistency.

## Code organization:
* Example: Logical grouping of functions and classes into sections.
* Notes: Structuring source code in a clear, modular, and maintainable way, often
  using functions, classes, and comments to enhance readability and collaboration.

## Performance testing/benchmarking:
* Example: `eg__compare`
* Notes: Evaluating the speed, responsiveness, and stability of a system or
  software under a particular workload. Benchmarking involves comparing performance
  against a standard or other systems.

## Experiment design:
* Example: `eg__compare` defines `repeats` and iterates over different `stop` values.
* Notes: The process of planning scientific or engineering experiments to collect
  data in a way that minimizes bias and allows for valid statistical analysis.

## Result aggregation:
* Example: `results[(name, stop)] = [Best(f) for _ in range(repeats)]`
* Notes: Collecting and combining data from multiple runs or sources into a single,
  consolidated view for analysis and reporting.

## Reporting (tabular output):
* Example: `def report(rows, head, decs=2):`
* Notes: Presenting data and analysis results in a structured and easy-to-understand
  format, often using tables, graphs, or summary statistics.

## Comparative analysis:
* Example: `eg__compare` uses `scottKnott` to statistically compare the `ydist` values.
* Notes: The process of evaluating the similarities and differences between
  multiple items, systems, or methods to draw conclusions about their relative
  strengths and weaknesses.

## Programming Paradigm:
* Notes: functional, object-oriebted

## Coding Styles
* Uncle Bob's rule:  short functions

## Dry not Wet

## Little Languages:
* Notes: aka domain specific languages. Make, regular expressions
