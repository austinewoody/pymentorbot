"""
pymentorbot.core

Beginner-friendly explanations for Python keywords, built-ins, errors, and concepts.
"""

EXPLANATIONS = {
    # Python constants / keywords
    "false": "False is a Boolean value that means something is not true. Example: is_active = False",
    "none": "None means no value or empty value. Example: result = None",
    "true": "True is a Boolean value that means something is true. Example: is_active = True",
    "and": "and is used when two conditions must both be true. Example: age > 18 and has_id",
    "as": "as gives something a temporary name. Example: import pandas as pd",
    "assert": "assert checks that a condition is true. If not, it raises an AssertionError.",
    "async": "async defines an asynchronous function. It is used for code that can wait without blocking.",
    "await": "await pauses an async function until another async task finishes.",
    "break": "break stops a loop early. Example: break out of a for or while loop.",
    "class": "class defines a blueprint for creating objects. Example: class Dog:",
    "continue": "continue skips the current loop step and moves to the next one.",
    "def": "def defines a function. Example: def greet():",
    "del": "del deletes a variable, item, or object reference. Example: del my_list[0]",
    "elif": "elif means else-if. It checks another condition after an if statement.",
    "else": "else runs when the if condition is false.",
    "except": "except catches errors in a try block. Example: except ValueError:",
    "finally": "finally runs after try/except whether an error happened or not.",
    "for": "for repeats code over a sequence. Example: for item in items:",
    "from": "from imports a specific part of a module. Example: from math import sqrt",
    "global": "global lets you modify a global variable inside a function.",
    "if": "if runs code only when a condition is true.",
    "import": "import loads a module so you can use its code. Example: import math",
    "in": "in checks membership. Example: 'a' in 'cat' returns True.",
    "is": "is checks whether two variables refer to the same object in memory.",
    "lambda": "lambda creates a small anonymous function. Example: square = lambda x: x * x",
    "nonlocal": "nonlocal lets an inner function modify a variable from an outer function.",
    "not": "not reverses a Boolean value. Example: not True gives False.",
    "or": "or is used when at least one condition must be true.",
    "pass": "pass does nothing. It is used as a placeholder where code is required.",
    "raise": "raise manually triggers an error. Example: raise ValueError('Invalid input')",
    "return": "return sends a value back from a function.",
    "try": "try starts a block of code where errors may be caught with except.",
    "while": "while repeats code as long as a condition is true.",
    "with": "with manages resources safely, such as opening and closing files.",
    "yield": "yield returns a value from a generator without ending the function completely.",
    "match": "match compares a value against patterns. It was introduced in Python 3.10.",
    "case": "case is used inside match to define each pattern to compare against.",

    # Common concepts
    "args": "*args collects extra positional arguments into a tuple.",
    "kwargs": "**kwargs collects extra named arguments into a dictionary.",
    "*args": "*args collects extra positional arguments into a tuple.",
    "**kwargs": "**kwargs collects extra named arguments into a dictionary.",
    "slicing": "Slicing extracts part of a sequence. Example: name[0:3] gets characters from index 0 up to 2.",
    "list slicing": "List slicing extracts part of a list. Example: nums[1:4] gets items at index 1, 2, and 3.",
    "decorator": "A decorator wraps a function to add extra behavior without changing the function body.",
    "decorators": "Decorators wrap functions to add extra behavior. Example: @login_required",
    "oop": "OOP means Object-Oriented Programming. It organizes code using classes and objects.",
    "object": "An object is an instance of a class. Example: dog = Dog()",
    "method": "A method is a function that belongs to a class or object.",
    "attribute": "An attribute is data stored inside an object. Example: user.name",
    "inheritance": "Inheritance lets one class reuse features from another class.",
    "polymorphism": "Polymorphism means different objects can use the same method name in different ways.",
    "encapsulation": "Encapsulation means keeping data and related methods together inside a class.",
    "module": "A module is a Python file that contains reusable code.",
    "package": "A package is a folder of Python modules, usually containing an __init__.py file.",
    "virtual environment": "A virtual environment keeps project dependencies separate from other projects.",
    "venv": "venv is Python's built-in tool for creating virtual environments.",
    "pip": "pip installs Python packages. Example: pip install requests",
    "pypi": "PyPI is the Python Package Index where Python packages are published and installed from.",
    "comprehension": "A comprehension is a short way to create lists, sets, or dictionaries.",
    "list comprehension": "A list comprehension creates a list in one line. Example: [x*x for x in nums]",
    "dictionary": "A dictionary stores key-value pairs. Example: {'name': 'Austine'}",
    "dict": "dict is Python's dictionary type for storing key-value pairs.",
    "list": "A list stores ordered items and can be changed. Example: [1, 2, 3]",
    "tuple": "A tuple stores ordered items and cannot be changed. Example: (1, 2, 3)",
    "set": "A set stores unique items. Example: {'a', 'b', 'c'}",
    "string": "A string stores text. Example: 'hello'",
    "str": "str is Python's text type. Example: str(123) gives '123'.",
    "integer": "An integer is a whole number. Example: 7",
    "int": "int is Python's whole number type. Example: int('5') gives 5.",
    "float": "A float is a decimal number. Example: 3.14",
    "boolean": "A Boolean is True or False.",
    "bool": "bool is Python's Boolean type. Example: bool(1) gives True.",
    "function": "A function is a reusable block of code. It is defined with def.",
    "variable": "A variable stores a value. Example: age = 20",
    "loop": "A loop repeats code. Python commonly uses for and while loops.",
    "condition": "A condition is an expression that evaluates to True or False.",
    "recursion": "Recursion is when a function calls itself.",
    "generator": "A generator produces values one at a time, often using yield.",
    "iterator": "An iterator is an object that returns values one at a time.",
    "exception": "An exception is an error that happens while a program is running.",
    "error handling": "Error handling uses try, except, else, and finally to handle problems safely.",

    # Built-in functions
    "print": "print displays output on the screen. Example: print('Hello')",
    "len": "len returns the number of items in something. Example: len('cat') gives 3.",
    "range": "range creates a sequence of numbers. Example: range(5) gives 0 to 4.",
    "input": "input asks the user to type something and returns it as a string.",
    "type": "type returns the data type of a value. Example: type(5)",
    "id": "id returns the unique identity of an object in memory.",
    "sum": "sum adds numbers in an iterable. Example: sum([1, 2, 3]) gives 6.",
    "min": "min returns the smallest value.",
    "max": "max returns the largest value.",
    "sorted": "sorted returns a new sorted list.",
    "enumerate": "enumerate gives both index and value while looping.",
    "zip": "zip combines items from multiple iterables together.",
    "map": "map applies a function to every item in an iterable.",
    "filter": "filter keeps only items that pass a condition.",
    "open": "open opens a file. It is best used with with.",
    "round": "round rounds a number. Example: round(3.14159, 2) gives 3.14.",
    "abs": "abs returns the positive distance from zero. Example: abs(-5) gives 5.",
    "all": "all returns True if every item is true.",
    "any": "any returns True if at least one item is true.",
    "help": "help shows documentation for Python objects.",
    "dir": "dir lists the attributes and methods available on an object.",

    # Common errors
    "syntaxerror": "SyntaxError means Python cannot understand your code structure.",
    "nameerror": "NameError means you used a name that has not been defined.",
    "typeerror": "TypeError means an operation was used with the wrong data type.",
    "valueerror": "ValueError means the data type is correct but the value is invalid.",
    "indexerror": "IndexError means you tried to access a list index that does not exist.",
    "keyerror": "KeyError means you tried to access a dictionary key that does not exist.",
    "attributeerror": "AttributeError means an object does not have the attribute or method you tried to use.",
    "indentationerror": "IndentationError means your code spacing/indentation is not correct.",
    "zerodivisionerror": "ZeroDivisionError means you tried to divide by zero.",
    "modulenotfounderror": "ModuleNotFoundError means Python cannot find the module you tried to import.",
}


def normalize_topic(topic):
    """Normalize user input for matching."""
    return str(topic).strip().lower().replace("_", " ")


def explain(topic):
    """
    Return a beginner-friendly explanation for a Python topic.
    """
    key = normalize_topic(topic)

    if key in EXPLANATIONS:
        return EXPLANATIONS[key]

    compact_key = key.replace(" ", "")
    if compact_key in EXPLANATIONS:
        return EXPLANATIONS[compact_key]

    suggestions = suggest(topic)
    suggestion_text = ", ".join(suggestions[:8]) if suggestions else "lambda, args, kwargs, list, dict, for, class"

    return (
        f"Sorry, no explanation found for '{topic}'.\n\n"
        f"Try one of these topics: {suggestion_text}\n\n"
        "Use: pymentorbot list\n"
        "to see all available topics."
    )


def list_topics():
    """Return all available topics sorted alphabetically."""
    return sorted(EXPLANATIONS.keys())


def search(query):
    """Return topics containing the search query."""
    q = normalize_topic(query)
    return [topic for topic in list_topics() if q in topic]


def suggest(topic):
    """Very simple suggestion helper."""
    q = normalize_topic(topic)
    if not q:
        return list_topics()[:8]

    first = q[0]
    matches = [topic for topic in list_topics() if topic.startswith(first)]
    contains = [topic for topic in list_topics() if q in topic and topic not in matches]
    return matches + contains


def quiz():
    """Return a simple quiz question."""
    return {
        "question": "What does *args do in Python?",
        "answer": "*args collects extra positional arguments into a tuple."
    }
