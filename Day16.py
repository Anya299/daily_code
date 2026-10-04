'''1. Module vs package
Module

A Python file is a module.

calculator.py

can contain:'''

def add(a, b):
    return a + b

#Then another file can import it:

from calculator import add

print(add(2, 3))
#Package

#A package is a directory containing related Python modules.

#Example:
'''
my_project/
│
├── math_tools/
│   ├── __init__.py
│   ├── calculator.py
│   └── statistics.py
│
└── main.py

Think:

module  → file
package → folder of modules
2. __init__.py

You'll see this file everywhere:

math_tools/
└── __init__.py

It tells Python that the directory is intended to behave as a package and can also contain package initialization/export logic.

For modern Python, namespace packages can exist without __init__.py, but you'll still encounter __init__.py constantly in real projects.

For now, remember:

__init__.py is commonly used to define and initialize a Python package.
'''
#3. Importing from a module

#Create:

#calculator.py
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b

#Then:

#main.py
from calculator import add, subtract


print(add(10, 5))
print(subtract(10, 5))

'''This is separation of responsibility.

Instead of putting everything into one file:

main.py

you separate functionality.'''

'''4. import vs from ... import

You can write:'''

import calculator

print(calculator.add(2, 3))

#Or:

from calculator import add

print(add(2, 3))

#Both are valid.

#Interview difference
import calculator

#imports the module.

#You access:

calculator.add()

#Whereas:

from calculator import add

#imports the specific function.

#You access:

#add()
#5. if __name__ == "__main__"

#This is very important.

#Consider:

def greet():
    print("Hello")


print("This file is running.")

#If another file imports it:

import greetings

#the top-level print() also executes.

#Instead, write:

def greet():
    print("Hello")


if __name__ == "__main__":
    print("This file is being run directly.")
'''
Now:

If you run:
python greetings.py

the block executes.

If another file does:
import greetings

the block does not execute.

6. Why this matters

Consider:'''

def main():
    print("Application started.")


if __name__ == "__main__":
    main()

#This creates a clean entry point.

#You'll see this pattern frequently in Python projects.

#7. Real project structure
'''
Instead of:

project/
├── main.py
├── random.py
├── test.py
├── stuff.py
└── final.py

we want something more organized.

For example:

ai_project/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── services.py
│   └── utils.py
│
├── tests/
│   ├── __init__.py
│   └── test_services.py
│
├── requirements.txt
├── README.md
└── .gitignore

Don't worry about memorizing every folder yet.

The important idea is:

app/       → application code
tests/     → tests
README.md  → documentation
requirements.txt → dependencies
.gitignore → files Git shouldn't track
8. Virtual environments

Suppose Project A needs:

FastAPI 1.x

and Project B needs another version.

Installing everything globally can cause conflicts.

A virtual environment gives the project its own Python environment.

Create one:

& "C:\Users\DELL\AppData\Local\Python\bin\python.exe" -m venv .venv

This creates:

.venv/
9. Activate it on Windows PowerShell
.\.venv\Scripts\Activate.ps1

You should see something similar to:

(.venv) PS C:\...

Now you're working inside the virtual environment.

To leave it:

deactivate
10. Installing packages

With the environment activated:

python -m pip install pytest

Then:

python -m pip list

You can see installed packages.

11. requirements.txt

Suppose your project uses:

pytest
requests
fastapi

You can record dependencies:

pytest
requests
fastapi

in:

requirements.txt

Then another developer can install them:

python -m pip install -r requirements.txt

This is important for reproducibility.

12. pip freeze

You can generate a dependency list:

python -m pip freeze > requirements.txt

Then:

type requirements.txt

will show the installed package versions.

Important

pip freeze records the packages installed in that environment, which can include transitive dependencies you didn't explicitly choose.

For larger production projects, dependency management can become more sophisticated. We'll cover that later.

13. .gitignore

You generally should not commit your virtual environment.

Create:

.gitignore

and include:

.venv/
__pycache__/
*.pyc
.env

Why?

Because:

.venv/

can be huge and should be recreated from dependencies.

And:

.env

may contain secrets.

For example:

OPENAI_API_KEY=...
DATABASE_URL=...

Never commit API keys.

14. Day 16 project

Create this:

day16_project/
│
├── app/
│   ├── __init__.py
│   ├── calculator.py
│   └── main.py
│
├── tests/
│   ├── __init__.py
│   └── test_calculator.py
│
├── requirements.txt
└── .gitignore
app/calculator.py'''
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")

    return a / b
#app/main.py
from app.calculator import add, subtract, multiply, divide


def main():
    print("Calculator")

    print("Add:", add(10, 5))
    print("Subtract:", subtract(10, 5))
    print("Multiply:", multiply(10, 5))
    print("Divide:", divide(10, 5))


if __name__ == "__main__":
    main()

#Notice:

if __name__ == "__main__":
    main()
#tests/test_calculator.py
import pytest

from app.calculator import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
#requirements.txt

#For today's project:
'''
pytest
.gitignore
.venv/
__pycache__/
*.pyc
.env
15. Run the project

From inside:

day16_project

run:

& "C:\Users\DELL\AppData\Local\Python\bin\python.exe" -m pytest

Then:

& "C:\Users\DELL\AppData\Local\Python\bin\python.exe" -m app.main

You should get:

Calculator
Add: 15
Subtract: 5
Multiply: 50
Divide: 2.0
16. The engineering idea

Notice what we've built:

                day16_project
                     │
        ┌────────────┴────────────┐
        │                         │
       app                       tests
        │                         │
 calculator.py             test_calculator.py
        │
      main.py

This is much closer to how you'll structure your future:

FastAPI
RAG
LLM
AI agent
ML

projects.'''
