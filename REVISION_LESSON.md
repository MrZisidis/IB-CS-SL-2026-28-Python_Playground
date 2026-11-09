# Python Fundamentals: Revision Lesson

**Audience:** introductory Python / IB Computer Science students  
**Suggested time:** 75–90 minutes  
**Purpose:** revise the ideas explored across the Python scripts in this project. The scripts are practice snapshots, so some contain unfinished exercises or bugs; use this lesson to understand, test, and improve them rather than assuming every file is ready to run.

## Learning goals

By the end, you should be able to:

- read input, convert types, store values, and format output;
- calculate with numbers and strings;
- select actions with `if`/`elif`/`else` and Boolean conditions;
- repeat work with `for` and `while` loops;
- inspect and transform strings;
- recognize common runtime and syntax errors, and handle expected exceptions;
- test a program with normal, boundary, and invalid inputs.

## 1. Output, input, and types

`print()` displays a value. `input()` always returns text (`str`), so convert it before doing numeric calculations. Use `int()` for whole numbers and `float()` for decimal values.

```python
name = input("What is your name? ")
hours = float(input("Hours worked: "))
rate = float(input("Hourly wage: "))
pay = hours * rate

print(f"{name}, your pay is €{pay:.2f}")
```

In an f-string, expressions go inside `{}`. `\n` makes a new line and `\t` inserts a tab. `type(value)` can help inspect a value while debugging.

**Project connections:** `lesson1.py` prints a value; `lesson2_14.09.2026.py` uses `input`, `print`, tabs, and newlines; `lessson3_16.09.2026.py` stores profile information and displays it; `progExericeCond.py` converts wage and hours to decimal numbers.

## 2. Expressions and calculations

Python evaluates arithmetic expressions using the usual operators: `+`, `-`, `*`, `/`, `//` (integer division), and `%` (remainder). For example, `60 * 24 * 365` gives the minutes in a 365-day year. Division by zero is an error.

```python
points = int(input("Points: "))
print("Remainder when divided by 5:", points % 5)
```

The wage exercise calculates `wage * hours` and doubles the result on Sunday. Its final `print(day + day)` is string concatenation, not part of the wage calculation; remove it unless repeated text is intentional.

## 3. Selection and Boolean conditions

An `if` chooses a block based on a Boolean expression. Use `elif` for another mutually exclusive case and `else` for the remaining case. Indentation defines each block. Comparisons include `==`, `!=`, `<`, `<=`, `>`, and `>=`; combine conditions with `and`, `or`, and `not`.

```python
age = int(input("Age: "))

if age >= 18:
    print("Adult")
else:
    print("Under 18")
```

For a range such as 50–79 inclusive, write `50 <= points <= 79`. For a grade-boundary exercise, first write down the boundary table, then test each boundary value and the values just below and above it.

The project menu should repeatedly ask until the choice is valid, then select one action:

```python
while True:
    print("1. Play game\n2. Instructions\n3. Quit")
    choice = input("Choose 1–3: ")

    if choice == "1":
        print("Starting the game")
        break
    elif choice == "2":
        print("Instructions...")
    elif choice == "3":
        print("Goodbye")
        break
    else:
        print("Enter 1, 2, or 3.")
```

Keeping the choice as text avoids a `ValueError` if the user types a non-number. Notice that option 2 returns to the menu, while options 1 and 3 end the loop.

**Project connections:** `conditional.py` demonstrates `if`/`else` and a nested condition (but its “teenager” test is inconsistent: an age over 80 is not a teenager); `combining_conditions.py` is an unfinished grade-boundary prompt; `conditional_Student_work.py` is the menu exercise (it currently asks only once, and its `while` condition does not repeat for invalid choices); `progExericeCond.py` selects Sunday pay.

## 4. Repetition: `for` and `while`

Use `for` when iterating over a sequence or a known range. `range(start, stop, step)` excludes `stop`.

```python
for number in range(1, 11):
    print(number)  # 1 through 10
```

Use `while` when repetition depends on a condition. Change the condition's state or use `break`, or the loop may never end.

```python
total = 0
count = 0

while True:
    text = input("Enter a number, or q to finish: ")
    if text == "q":
        break
    number = float(text)
    total += number
    count += 1

if count > 0:
    print("Total:", total)
    print("Average:", total / count)
else:
    print("No numbers entered.")
```

**Project connections:** `for_loop_1.py` contains examples of ranges, steps, nested loops, countdowns, and character iteration; `simple_loop.py` sketches a running total, maximum, and average, but its active `while True` prints forever. Do not run that file unchanged; add an exit condition or stop it with the IDE's stop control.

## 5. Strings and character-by-character processing

Strings are sequences: indexing starts at zero, slicing selects a portion, and methods such as `.find()`, `.replace()`, `.upper()`, and `len()` help inspect or transform text. `+` joins strings. `.find()` returns `-1` when the text is absent, so check for that before using the result as a slice position.

This ROT13 example uses modulo to wrap from the end of the alphabet to the beginning:

```python
alphabet = "abcdefghijklmnopqrstuvwxyz"
text = input("Lowercase text: ")
encoded = ""

for char in text:
    if char in alphabet:
        index = alphabet.index(char)
        encoded += alphabet[(index + 13) % 26]
    else:
        encoded += char

print(encoded)
```

It preserves spaces and punctuation and handles lowercase letters; uppercase characters remain unchanged. The character-indexing attempt in `for_loop_1.py` has an incorrect wraparound calculation and may index outside the alphabet. `strings_1.py` explores indexing, slicing, finding separators, and replacing words; compare its manually rebuilt result with `course.replace(...)`.

## 6. Debugging and exceptions

When a program behaves unexpectedly:

1. Reproduce the problem with a small input.
2. Read the error type and line number.
3. Print relevant variable values and types.
4. Check indentation, boundary conditions, and arithmetic.
5. Test the corrected program again.

Use `try`/`except` for specific expected runtime errors. Handle only the errors you can respond to meaningfully.

```python
try:
    people = int(input("Number of people: "))
    total = int(input("Total amount: "))
    share = total // people
except ValueError:
    print("Enter whole numbers.")
except ZeroDivisionError:
    print("Number of people must be greater than zero.")
else:
    print("Each person gets:", share)
```

`finally`, when used, runs whether or not an exception occurred. Avoid a bare `except:` when a specific exception is known.

**Project connections:** `debug_1.py` demonstrates tracing values and exception handling, but an indented `raise` is outside any block and causes an `IndentationError`; its broad `except:` also hides the specific error. `exception_handling.py` shows named exception handlers and `finally`; its active calculation divides `people` by `total`, so `people = 0` does **not** cause division by zero. Reverse the operands to calculate a share, and ensure the divisor is nonzero.

## 7. Revision challenge

Write a program that repeatedly asks for item prices until the user enters `q`. Then display the number of items, the total, and the average price. Give a 20% discount if the total is over €100. Reject non-numeric entries with a clear message, and handle the case where no prices were entered.

Before calling it complete, test:

- `q` immediately;
- one price;
- several prices whose total is exactly €100;
- several prices whose total is above €100;
- invalid text instead of a price.

## Quick self-check

1. What type does `input()` return?
2. Does `range(2, 8)` include 8?
3. What value does `"python".find("z")` return?
4. Why can `while True` continue forever?
5. Which exception should be handled for `int("hello")`?

**Answers:** 1. `str`. 2. No. 3. `-1`. 4. It has no false condition or reachable `break`. 5. `ValueError`.

## Source coverage

This lesson draws on all 12 Python scripts in the project: `lesson1.py`, `lesson2_14.09.2026.py`, `lessson3_16.09.2026.py`, `conditional.py`, `combining_conditions.py`, `StudentCode\progExericeCond.py`, `StudentCode\conditional_Student_work.py`, `for_loop_1.py`, `simple_loop.py`, `strings_1.py`, `exception_handling.py`, and `debug_1.py`.
