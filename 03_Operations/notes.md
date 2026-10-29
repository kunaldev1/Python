# Python Operations and Operators

Operators perform actions on values. The values used by an operator are called operands.

## Arithmetic operators

| Operator | Meaning | Example result |
| --- | --- | --- |
| `+` | Addition | `5 + 2 == 7` |
| `-` | Subtraction | `5 - 2 == 3` |
| `*` | Multiplication | `5 * 2 == 10` |
| `/` | Division | `5 / 2 == 2.5` |
| `//` | Floor division | `5 // 2 == 2` |
| `%` | Remainder | `5 % 2 == 1` |
| `**` | Exponentiation | `5 ** 2 == 25` |

## Comparison operators

Comparisons return a Boolean value: `==`, `!=`, `<`, `<=`, `>`, and `>=`.

```python
age = 18
print(age >= 18)  # True
```

Use `==` to compare values and `=` to assign a value.

## Logical operators

- `and`: both conditions must be true.
- `or`: at least one condition must be true.
- `not`: reverses a Boolean result.

```python
age = 20
has_id = True
print(age >= 18 and has_id)
```

## Assignment operators

`+=`, `-=`, `*=`, and `/=` update a variable using its current value.

```python
score = 10
score += 5
print(score)  # 15
```

## Operator precedence

Multiplication and division generally happen before addition and subtraction. Use parentheses when they make the intended order clearer.

## Practice

1. Calculate the remainder when 29 is divided by 5.
2. Check whether a number is between 1 and 100 inclusive.
3. Use `and` to check whether a number is positive and even.
4. Rewrite an expression with parentheses to make its order explicit.

## Next topic

Continue to [Conditions](../04_Conditions/notes.md).
