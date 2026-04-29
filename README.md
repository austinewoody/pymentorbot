# pymentorbot

**pymentorbot** is a beginner-friendly Python learning assistant package.

It explains Python keywords, built-in functions, common errors, and programming concepts in simple language.

## Features

- Explains Python keywords such as `lambda`, `yield`, `class`, `async`, `await`, `match`, and `case`
- Explains common concepts such as `args`, `kwargs`, slicing, decorators, OOP, modules, packages, and virtual environments
- Explains built-in functions such as `len`, `range`, `zip`, `map`, `filter`, `enumerate`, and `print`
- Explains common errors such as `NameError`, `TypeError`, `ValueError`, and `IndentationError`
- Includes a command-line interface
- Includes friendly fallback messages when a topic is not found

## Installation

```bash
pip install pymentorbot
```

## Command Line Usage

Explain a topic:

```bash
pymentorbot explain lambda
```

List all available topics:

```bash
pymentorbot list
```

Search topics:

```bash
pymentorbot search error
```

Try quiz mode:

```bash
pymentorbot quiz
```

## Python Usage

```python
from pymentorbot import explain

print(explain("lambda"))
print(explain("kwargs"))
print(explain("NameError"))
```

## Example Output

```text
lambda creates a small anonymous function. Example: square = lambda x: x * x
```

## Why this package?

Many Python beginners struggle to understand keywords and concepts when reading code. pymentorbot gives short, simple explanations that are easy to understand from the terminal or inside Python code.

## Author

Austine Onwubiko  
Software Engineer | Cybersecurity Researcher | PhD Candidate
