# liars-and-truth-tellers
A brute-force solver for problems about truth tellers and liars

# How to use
Below the `# Your code goes below!` comment, you should describe the problem. You can check if two people act the same (that is, if they are both truth tellers or both liars) using the equality operator `==`, or if they are different using the inequality operator `!=`. You can check if they are a truth teller using the `.isTruthTeller()` method, and if they are a liar using the `.isLiar()` method.

You can supply an array of many conditions, and if you want to quote what somebody has said you can use the `person.said()` method.

All the people involved are supplied in an array.

# Examples

## I am a liar!
:warning: **Spoiler alert**, the following examples contain answers to some truth-tellers-and-liars puzzles. Instead of reading on, I suggest you have a go at solving them.

Let's say you have one person, let's call them A, that says `I'm a liar!`, and you want to check if this is actually possible in a world where people either *always* lie, or *always* tell the truth.

First, you need to describe the problem. We need to use the `.said()` method to quote A, and we need to describe what A said using `.isLiar()`.

The first argument is the amount of people we want. In this case, we only want one person, A.

```python
def verify_conditions_satisfied(people):
  A = people[0]
  return A.said(A.isLiar())

number_of_people = 1

print(list_all_solutions(number_of_people, verify_conditions_satisfied))
```

And that will output

```
[]
```

because it is impossible to say you are a liar.

- If you are a liar, you would be lying about being a liar, hence you are a truth teller. (Contradiction)
- If you are a truth-teller, you would be telling the truth about being a liar, hence you are a liar. (Contradiction)

Here is a more succint way of doing the same thing:
```python
print(list_all_solutions(1, lambda people: people[0].said(people[0].isLiar())))
```

## Between my brother and I, at least one of us is a liar!
Let's call the speaker A, and the brother B. We will want to use `.said()` to quote what A said, and then we will have to explain what A did say.

```python
def verify_conditions_satisfied(people):
  A, B = people[0], people[1]
  return A.said(A.isLiar() or B.isLiar())
  
number_of_people = 2
 
print(list_all_solutions(number_of_people, verify_conditions_satisfied)) 
```

This will output

```python
['10']
```

Each element in the array refers to one combination which works. In this case, there is only one combination which works. In this case, it is "A is a truth-teller, and B is a liar"

<table>
  <tr><th>A</th><th>B</th></tr>
  <tr><td>1</td><td>0</td></tr>
  <tr><td>T</td><td>L</td></tr>
</table>

1 = Truth-teller; 0 = Liar.

Here is, again, a shorter (but perhaps less readable) way of writing out the same thing.

```python
print(list_all_solutions(2, lambda p: p[0].said(p[0].isLiar() or p[1].isLiar())))
```

## My sister and I are either both truth-tellers or both liars

In this case, you can use the equality operator

```python
def verify_conditions_satisfied(people):
  A, B = people[0], people[1]
  return A.said(A == B)
  
print(list_all_solutions(2, verify_conditions_satisfied))
```
or, less readably:
```python
print(list_all_solutions(2, lambda p: p[0].said(p[0] == p[1])))
```
will yield:
```python
['01', '11']
```

This means that A (the person speaking) could be either a truth-teller or a liar, because the first digit is `0` in one case, but `1` in the other; but the sister (B) must be a truth-teller, because the second digit in each element is always `1`.

