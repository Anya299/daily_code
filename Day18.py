'''1. Git — Professional Workflow

You already know basic:

git add .
git commit -m "message"
git push

Today understand the workflow behind it.

Typical workflow
main
  │
  ├── feature/login
  │
  ├── feature/payment
  │
  └── feature/testing

You normally don't directly develop everything on main.

Example:

git checkout -b feature/calculator-tests

Work:

git add .
git commit -m "Add calculator unit tests"

Then:

git push -u origin feature/calculator-tests
2. Git Commands You Must Know
Check status
git status
See commits
git log --oneline
Create branch
git checkout -b feature/testing
Switch branch
git checkout main
See branches
git branch
Stage
git add .
Commit
git commit -m "Add unit tests"
Push
git push
Pull
git pull
Compare changes
git diff'''


'''3. Merge Conflicts

A conflict happens when two branches modify the same part of a file differently.

Example:

<<<<<<< HEAD
return "Hello"
=======
return "Hello World"
>>>>>>> feature/greeting

You manually decide what the final code should be.

For example:

return "Hello World"

Then:

git add .
git commit -m "Resolve merge conflict"
Interview answer

A merge conflict occurs when Git cannot automatically determine which changes should be kept. I inspect the conflicting section, choose or combine the correct implementation, test it, then commit the resolved version.'''


'''4. Professional Commit Messages

Avoid:

update
changes
final
done
abc
test

Prefer:

Add calculator unit tests
Fix divide by zero validation
Refactor notification service
Add AI model abstraction
Improve error handling
Update project documentation

A good commit tells another engineer what changed.'''


'''5. README.md

A professional project should explain itself.

Your README structure:'''
'''
# Project Name

## Overview

Short explanation of what the project does.

## Features

- Feature 1
- Feature 2
- Feature 3

## Tech Stack

- Python
- Pytest
- Git

## Project Structure

```text
project/
├── app/
├── tests/
├── requirements.txt
└── README.md'''


'''Installation
python -m venv .venv
pip install -r requirements.txt
Usage
python -m app.main
Testing
python -m pytest
Design

Explain important architectural decisions.

Future Improvements
Improvement 1
Improvement 2

---

# 6. DAY 18 CAPSTONE 🧠

We're going to combine:

**OOP + SOLID + testing + packaging + Git**

Build this:

## `notification_system`

```text
notification_system/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── services.py
│   └── main.py
│
├── tests/
│   ├── __init__.py
│   └── test_services.py
│
├── requirements.txt
├── .gitignore
└── README.md
7. models.py

Create:

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
8. services.py

Here we're applying Dependency Injection + abstraction.
'''
from abc import ABC, abstractmethod


class NotificationSender(ABC):

    @abstractmethod
    def send(self, user, message):
        pass


class EmailSender(NotificationSender):

    def send(self, user, message):
        return f"Email sent to {user.email}: {message}"


class SMSender(NotificationSender):

    def send(self, user, message):
        return f"SMS sent to {user.name}: {message}"


class NotificationService:

    def __init__(self, sender):
        self.sender = sender

    def notify(self, user, message):
        return self.sender.send(user, message)

#Notice this:

class NotificationService:

    def __init__(self, sender):
        self.sender = sender

#We inject the sender.

#We don't do this:

#self.sender = EmailSender()

#inside the service.

#That's the important engineering decision.

#9. main.py
from app.models import User
from app.services import EmailSender, NotificationService


def main():

    user = User(
        "Ananya",
        "ananya@example.com"
    )

    sender = EmailSender()

    service = NotificationService(sender)

    result = service.notify(
        user,
        "Your application has been submitted."
    )

    print(result)


if __name__ == "__main__":
    main()

#Run:

#& "C:\Users\DELL\AppData\Local\Python\bin\python.exe" -m app.main

#Expected:

#Email sent to ananya@example.com: Your application has been submitted.
#10. Testing

#Create:

#tests/test_services.py

from app.models import User
from app.services import EmailSender, SMSender, NotificationService


def test_email_sender():

    user = User("Ananya", "ananya@example.com")

    sender = EmailSender()

    result = sender.send(
        user,
        "Hello"
    )

    assert result == "Email sent to ananya@example.com: Hello"


def test_sms_sender():

    user = User("Ananya", "ananya@example.com")

    sender = SMSender()

    result = sender.send(
        user,
        "Hello"
    )

    assert result == "SMS sent to Ananya: Hello"


def test_notification_service():

    user = User("Ananya", "ananya@example.com")

    sender = EmailSender()

    service = NotificationService(sender)

    result = service.notify(
        user,
        "Welcome"
    )

    assert result == "Email sent to ananya@example.com: Welcome"

#Run:

#& "C:\Users\DELL\AppData\Local\Python\bin\python.exe" -m pytest

#You should get:

#3 passed
#11. Now Apply SOLID Yourself
'''
Look at this architecture:

User
 │
 ▼
NotificationService
 │
 ▼
NotificationSender
 │
 ├── EmailSender
 │
 └── SMSender
SRP

User handles user data.

NotificationService handles notification orchestration.

EmailSender handles email sending.

Each has a focused responsibility.

OCP

We can add:'''

class WhatsAppSender(NotificationSender):

    def send(self, user, message):
        return f"WhatsApp sent to {user.name}: {message}"

'''without changing NotificationService.

LSP

EmailSender and SMSender can be used wherever NotificationSender is expected.

DIP

NotificationService depends on the abstraction:

NotificationSender

rather than:

EmailSender
Dependency Injection

The sender is passed from outside:

service = NotificationService(sender)
12. Your Challenge 🔥

Now don't copy the next part immediately.

Add:

WhatsAppSender

It must implement:

send(user, message)

Then:

sender = WhatsAppSender()
service = NotificationService(sender)

Expected result:

WhatsApp sent to Ananya: Hello

Then write one pytest test for it.

This is important because I want you to start writing without seeing the answer.

13. README Challenge

Write a professional README.md for this project.

Include:

Project overview
Features
Tech stack
Project structure
Installation
Usage
Testing
SOLID design decisions
Future improvements

Don't make it fancy.

Make it professional.

14. .gitignore

Use:

.venv/
__pycache__/
*.pyc
.env
.pytest_cache/
15. requirements.txt

For this project:

pytest
16. Git Workflow

After your project works:

git status

Then:

git add .

Commit:

git commit -m "Day 18 - build SOLID notification system"

Push:

git push origin day6-first-contribution

Then check:

git log --oneline -5


'''
