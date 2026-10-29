# Python Lists

A list is an ordered, mutable collection. Lists can contain values of different types, though a list of one logical type is often easier to work with.

## Create and access a list

```python
languages = ["Python", "Java", "C"]
print(languages[0])   # Python
print(languages[-1])  # C
print(languages[0:2]) # ['Python', 'Java']
```

Indexing starts at zero. Slices use an exclusive stop index.

## Modify a list

```python
numbers = [10, 20, 30]
numbers.append(40)
numbers[0] = 5
numbers.remove(20)
print(numbers)
```

Common methods include `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `sort()`, and `reverse()`.

## Iterate over a list

```python
for language in languages:
    print(language)
```

Use `enumerate(languages)` when both the index and value are needed.

## Common pitfalls

- Accessing an index that doesn't exist raises `IndexError`.
- Mutating a list while iterating over it can lead to skipped or unexpected items.
- `list.sort()` changes the list in place and returns `None`.

## Practice

1. Find the smallest and largest number in a list.
2. Count how many times a value appears.
3. Build a new list containing only even numbers.
4. Remove duplicates while preserving the original order.

## Next topic

Continue to [Tuples](../08_Tuples/notes.md).
