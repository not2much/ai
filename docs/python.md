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

# Python 3 Concepts:

## Variables and Assignment:
* Example: `s,n = 0,0`
* Notes: Variables are names given to memory locations where data is stored.
  Assignment (`=`) is used to bind a value to a variable name.

## Literals (numbers, strings):
* Example: `name="alan"`
* Notes: Literals are fixed values in code, such as `41` (integer literal),
  `3.14` (float literal), or `"alan"` (string literal).

## F-string
* XXX

## Operators (arithmetic, assignment, comparison, logical):
* Example: `d = n - num.mu` (arithmetic subtraction and assignment)
* Notes: Symbols that perform operations on values and variables. Examples: `+`, `-`,
  `*`, `/` (arithmetic); `=`, `+=` (assignment); `==`, `!=`, `<`, `>` (comparison);
  `and`, `or`, `not` (logical).

## Data Types (int, float, str, bool, list, dict):
* Example: `int(v)`, `float('inf')`, `type(row[0]) is str`
* Notes: Python has several built-in data types. `int` for whole numbers,
  `float` for decimal numbers, `str` for text, `bool` for True/False,
  `list` for ordered collections, and `dict` for key-value pairs.

## Expressions:
* Example: `(b + r*q) / abs(b*q - r + 1/big)`
* Notes: A combination of values, variables, operators, and function calls that
  evaluates to a single value.

## Functions:
* Example: `def fyi(*l,**kw,):` (definition)
* Notes: Reusable blocks of code that perform a specific task. They can take
  inputs (arguments/parameters) and return outputs.

## Conditional statements (`if`, `if-else`, `elif`):
* Example: `if line:`
* Notes: Control flow statements that execute different blocks of code based on
  whether a condition is true or false.

## Ternary operator (conditional expressions):
* Example: `(y == "true") if y in ("true", "false") else x`
* Notes: A concise way to write `if-else` statements on a single line.
  The syntax is `value_if_true if condition else value_if_false`.

## Loops (`for`, `while`):
* Example: `for what in (int, float):`
* Notes: Control structures that allow code to be repeatedly executed.
  `for` loops iterate over sequences; `while` loops repeat as long as a condition is true.

## Iteration:
* Example: `for i,row in enumerate(csv(lines(EXAMPLE))):`
* Notes: The process of repeating a sequence of instructions over each item in a collection.

## Iterators:
* Example: `inits = iter(inits)`
* Notes: Objects that represent a stream of data. They implement the `__iter__()`
  and `__next__()` methods, allowing them to be used in `for` loops. `iter()`
  explicitly gets an iterator from an iterable.

## Generators (`yield`):
* Example: `for line in f: yield line`
* Notes: Functions that produce a sequence of results one at a time, instead of
  computing them all at once and returning a list. They use the `yield` keyword,
  making them memory-efficient for large sequences.

## Lists:
* Example: `all,x,y = [],[],[]` (creation)
* Notes: Ordered, mutable collections of items. They can store items of different
  data types and are defined using square brackets `[]`.

## List methods (`append()`, `remove()`, `pop()`):
* Example: `best._rows.pop(-1)`
* Notes: Built-in functions that operate on lists, such as adding elements (`append`),
  removing specific elements (`remove`), or removing and returning an element by index (`pop`).

## List comprehensions:
* Example: `[atom(s) for s in line.strip().split(',')]`
* Notes: A concise way to create lists. They provide a shorter syntax to
  construct new lists based on existing iterables, often in a single line.

## List slicing:
* Example: `data._rows[::-1]`
* Notes: A powerful way to extract a portion of a list using `[start:end:step]`.
  `[::-1]` is a common idiom to reverse a list.

## Dictionaries:
* Example: `has={}` (creation)
* Notes: Unordered collections of key-value pairs. Keys must be unique and immutable.
  Used for efficient lookup of values associated with specific keys.

## Dictionary methods (`get()`, `items()`, `values()`, `update()`):
* Example: `sym.has.get(s,0)`
* Notes: Functions that operate on dictionaries. `get()` safely retrieves a value
  with a default if the key is missing; `items()` returns key-value pairs;
  `values()` returns values; `update()` merges dictionaries or adds/updates items.

## Classes and Objects:
* Example: `class o:` (definition)
* Notes: Classes are blueprints for creating objects. Objects are instances of classes,
  encapsulating data (attributes) and behavior (methods). Used for
  object-oriented programming (OOP).

## Modules and Imports (`sys`, `math`, `random`, `re`, `traceback`):
* Example: `import traceback,random,math,sys,re`
* Notes: Modules are files containing Python definitions and statements.
  `import` statements bring functionalities from other modules into the current script.

## Built-in functions:
* Example: `print()`
* Notes: Functions that are always available for use in Python without explicit
  import. Examples: `len()`, `sum()`, `min()`, `max()`, `sorted()`.

## Error Handling (`try-except`):
* Example: `try: return what(x) except Exception: pass`
* Notes: A mechanism to gracefully manage errors (exceptions) that occur
  during program execution. Code that might cause an error is placed in the
  `try` block, and the `except` block handles specific types of errors.

## String methods (`strip()`, `split()`, `isupper()`, `startswith()`, `replace()`):
* Example: `line.strip().split(',')`
* Notes: Functions that operate on strings to perform common text manipulations,
  like removing whitespace (`strip`), dividing into substrings (`split`),
  checking case (`isupper`), or replacing parts of the string.

## Regular expressions (`re` module, `re.finditer()`, `re.sub()`):
* Example: `re.finditer(r"-\w+\s+(\w+)[^\(]*\(\s*([^)]+)\s*\)", __doc__)`
* Notes: A powerful language for defining search patterns in text. The `re` module
  provides functions for searching, splitting, and replacing text based on these patterns.

## File I/O operations (`open()`):
* Example: `with open(file, 'r', newline='', encoding='utf-8') as f:`
* Notes: The process of reading from or writing to files. `open()` creates a file
  object, and the `with` statement ensures the file is properly closed afterwards.

## `random` module functions:
* Example: `random.gauss(10,2)`
* Notes: Provides functions for generating pseudo-random numbers and sequences,
  including various distributions (`gauss`), shuffling (`shuffle`), and sampling (`sample`, `choices`).


