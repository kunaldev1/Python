# Python Data Types

A data type describes the kind of value a variable refers to. Python determines a variable's type from the value assigned to it.

## Common built-in types

| Type | Example | Purpose |
| --- | --- | --- |
| `int` | `42` | Whole numbers |
| `float` | `3.14` | Decimal numbers |
| `str` | `"hello"` | Text |
| `bool` | `True`, `False` | Truth values |
| `list` | `[1, 2, 3]` | Ordered, mutable collection |
| `tuple` | `(1, 2, 3)` | Ordered, immutable collection |
| `dict` | `{"name": "Kunal"}` | Key-value mapping |
| `set` | `{1, 2, 3}` | Collection of unique values |
| `NoneType` | `None` | Absence of a value |

## Check a type

```python
age = 18
print(type(age))  # <class 'int'>
```

## Type conversion

Convert compatible values explicitly:

```python
age_text = "18"
age = int(age_text)
price = float("19.99")
message = str(age)
```

Invalid conversions raise errors. For example, `int("hello")` raises `ValueError`.

## Important distinction

`input()` returns a string, even when the user types digits. Convert input before doing arithmetic:

```python
first = int(input("First number: "))
second = int(input("Second number: "))
print(first + second)
```

## Practice

1. Create one variable of type `int`, `float`, `str`, and `bool`.
2. Print each variable's type with `type()`.
3. Convert the string `"25"` to an integer.
4. Try converting `"twenty-five"` to an integer and explain the error.

## Next topic

Continue to [Operations](../03_Operations/notes.md).
