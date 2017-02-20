# knights-and-knaves
A brute-force solver for problems about truth tellers (knights) and liars (knaves)

# How to use
Below the `# Your code goes below!` comment, you should describe the problem. You can check if two people act the same (that is, if they are both knights or both knaves) using the equality operator `==`, or if they are different using the inequality operator `!=`. You can check if they are a knight using the `.isKnight()` method, and if they are a knave using the `.isKnave()` method.

You can supply an array of many conditions, and if you want to quote what somebody has said you can use the `person.said()` method.

All the people involved are supplied in an array.

# Example

In these examples, we only have one condition. If multiple people in the world of knights and knaves are speaking, you will want to pass more functions into the array of functions.

## I am a liar!
:warning: Spoiler alert, the following examples contain answers to some knights-and-knaves puzzles. Instead of reading on, I suggest you have a go at solving them.

Let's say you have one person, let's call them A, that says `I'm a liar!`, and you want to check if this is actually possible in a world where people either *always* lie, or *always* tell the truth.

First, you need to describe the problem. We need to use the `.said()` method to quote A, and we need to describe what A said using `.isKnave()`.

The first argument is the amount of people we want. In this case, we only want one person, A.

```python
print(calc(1, [lambda people: people[0].said(people[0].isKnave())]))
```

And that will output

```
[]
```

because it is impossible to say you are a liar. If you *are* a liar, then when you say `I am a liar!`, you are actually lying about that. But that means you are a truth-teller. Contradiction!

If you are a truth-teller, then you are directly saying you are a liar. Again, contradiction!

## Between my brother and I, at least one of us is a liar!
Let's call the speaker A, and the brother B. We will want to use `.said()` to quote what A said, and then we will have to explain what A did say.

We need two people. Let's write code! :D

```python
print(calc(2, [lambda people: people[0].said(people[0].isKnave() or people[1].isKnave())]))
```

This will output

```
['10']
```

That means there is only *one* combination that will fit the criteria supplied. This combination is `10`. `1` means knight, and `0` means knave, so `10` means A is a knight, and B is a knave.

Does this solution work? Well, yes, and in fact, it is the only solution.

# Ending remarks

This is a tool that is intended to speed up solving those knights-and-knaves puzzles. However, I *do* suggest you do them yourself and then use this if you want to check your answer.

By the way, if you want to check if somebody happens to be somebody else, e.g. "Are you the criminal we are looking for, who said you were a knave" then you should directly compare them using the `==` operator, and that *should* work. Good luck!
