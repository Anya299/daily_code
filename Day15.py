'''1. What is testing?

Suppose you write:'''

def add(a, b):
    return a + b

#You could manually test:

print(add(2, 3))

#and see:

#5

#But professional software needs repeatable tests.

#A test asks:

#"Given this input, do I get the expected output?"

#For example:
'''
Input:  2, 3
Expected: 5
2. Assertions

Python has a built-in assert.'''

def add(a, b):
    return a + b


assert add(2, 3) == 5

#If it's correct, Python continues.

#If it's wrong:

assert add(2, 3) == 10

#Python raises:

#AssertionError
#Think of it as:
#assert actual == expected
#3. More assertions
def is_even(number):
    return number % 2 == 0

#Tests:

assert is_even(10) == True
assert is_even(7) == False
assert is_even(0) == True

#You're checking multiple cases.

#4. Why edge cases matter

#Consider:

def divide(a, b):
    return a / b

# test:

#divide(10, 2)

#Works.

#But:

#divide(10, 0)

#causes an error.

#So good testing asks:
'''
Normal input
Small input
Zero
Negative input
Empty input
Very large input
Invalid input

Not every function needs every category, but you should think about boundaries.
'''
#5. Unit testing

#A unit test tests a small unit of code, usually a function or method.

#Example:

def multiply(a, b):
    return a * b

#Test:

def test_multiply():
    assert multiply(3, 4) == 12

#The function is the unit.

#6. pytest

#pytest is a popular Python testing framework.

#First check whether it is installed:

#& "C:\Users\DELL\AppData\Local\Python\bin\python.exe" -m pytest --version

#If it isn't installed:

#& "C:\Users\DELL\AppData\Local\Python\bin\python.exe" -m pip install pytest
#7. Your first pytest test

#Create:

#calculator.py
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b

#Now create:

#test_calculator.py
from calculator import add, subtract, multiply


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(3, 4) == 12

#8. Why test_?

#Pytest automatically discovers files and functions following common naming conventions.

#For example:

#test_calculator.py

and:

def test_add():

#This is why we use the test_ prefix.

#9. Testing edge cases

#Suppose:

def is_even(number):
    return number % 2 == 0

#Don't test only:

assert is_even(10) == True

#Add:

def test_is_even():
    assert is_even(10) is True
    assert is_even(7) is False
    assert is_even(0) is True
    assert is_even(-4) is True

#Now you're thinking like a tester.

#10. Testing classes

#This connects directly to your Day 13 and Day 14 OOP.

#Create:

class BankAccount:

    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return False

        self._balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0:
            return False

        if amount > self._balance:
            return False

        self._balance -= amount
        return True

    def get_balance(self):
        return self._balance

#Tests:

def test_deposit():
    account = BankAccount(1000)

    account.deposit(500)

    assert account.get_balance() == 1500

#Another:

def test_withdraw():
    account = BankAccount(1000)

    account.withdraw(300)

    assert account.get_balance() == 700

#Edge case:

def test_insufficient_balance():
    account = BankAccount(1000)

    result = account.withdraw(2000)

    assert result is False
    assert account.get_balance() == 1000

#Notice something important:

#We're checking both:

#return value
#+
#state of the object

#That's good engineering.

#11. Testing invalid input

#Suppose:

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")

    return a / b

#How do we test the error?

'''Pytest provides:

pytest.raises()

Example:'''

import pytest


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

'''This means:

"I expect this code to raise ValueError."

12. A complete Day 15 project

Create:

day15_testing/
│
├── calculator.py
└── test_calculator.py
calculator.py'''
class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")

        return a / b
#test_calculator.py
import pytest

from calculator import Calculator


def test_add():
    calculator = Calculator()

    assert calculator.add(2, 3) == 5


def test_subtract():
    calculator = Calculator()

    assert calculator.subtract(10, 4) == 6


def test_multiply():
    calculator = Calculator()

    assert calculator.multiply(3, 4) == 12


def test_divide():
    calculator = Calculator()

    assert calculator.divide(10, 2) == 5


def test_divide_by_zero():
    calculator = Calculator()

    with pytest.raises(ValueError):
        calculator.divide(10, 0)

#Run from inside the folder:

#& "C:\Users\DELL\AppData\Local\Python\bin\python.exe" -m pytest
#13. Understanding a failing test

#Suppose you accidentally write:

def add(self, a, b):
    return a - b

#Then:

#assert calculator.add(2, 3) == 5

#fails.

#Don't immediately change random code.

#Read:

#Expected: 5
#Actual:   -1

#Then ask:

#Where did the actual value come from?

#Trace:
'''
test
 ↓
calculator.add()
 ↓
implementation
 ↓
wrong operation

This is the beginning of professional debugging.

14. Test pyramid — basic idea

You'll encounter this later.

        /\
       /  \
      / E2E\
     /------\
    /Integration\
   /------------\
  / Unit Tests   \
 /________________\

Generally:

Unit tests

Small and fast.

function
method
class behavior
Integration tests

Check whether components work together.

Example:

FastAPI → database
End-to-end tests

Test a larger real workflow.

Example:

User → API → AI model → database → response

For now, focus heavily on unit tests.'''
