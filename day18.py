```python
"""
============================================================
DAY 18 — SOFTWARE ENGINEERING FINAL DAY
============================================================

Phase 1:
Python → OOP → Testing → Packaging → Clean Code → SOLID
→ Git + Professional Workflow

Goal:
Move from "I can code Python" to
"I can engineer a Python project."

============================================================
DAY 18 OUTCOMES
============================================================

By the end of today, I should be able to:

- Use Git professionally
- Create meaningful commits
- Work with branches
- Understand merge conflicts
- Write a professional README
- Structure a Python project
- Write tests
- Apply SOLID principles
- Review my own code
- Explain engineering decisions in interviews

============================================================
1. GIT — PROFESSIONAL WORKFLOW
============================================================

Typical workflow:

main
 |
 ├── feature/login
 ├── feature/payment
 └── feature/testing

Normally, development should happen on feature branches
instead of directly on main.

Example:

git checkout -b feature/calculator-tests

After making changes:

git add .
git commit -m "Add calculator unit tests"
git push -u origin feature/calculator-tests


============================================================
2. IMPORTANT GIT COMMANDS
============================================================

Check status:

git status

View commits:

git log --oneline

Create a branch:

git checkout -b feature/testing

Switch branch:

git checkout main

See branches:

git branch

Stage changes:

git add .

Commit:

git commit -m "Add unit tests"

Push:

git push

Pull:

git pull

Compare changes:

git diff


============================================================
3. MERGE CONFLICTS
============================================================

A merge conflict happens when Git cannot automatically determine
which changes should be kept.

Example:

<<<<<<< HEAD
return "Hello"
=======
return "Hello World"
>>>>>>> feature/greeting

Resolve the conflict manually.

Example final code:

return "Hello World"

Then:

git add .
git commit -m "Resolve merge conflict"

Interview answer:

"A merge conflict occurs when Git cannot automatically determine
which changes should be kept. I inspect the conflicting section,
choose or combine the correct implementation, test it, and then
commit the resolved version."


============================================================
4. PROFESSIONAL COMMIT MESSAGES
============================================================

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

A good commit message tells another engineer what changed.


============================================================
5. README.md
============================================================

A professional project should explain itself.

Recommended structure:

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

project/
├── app/
├── tests/
├── requirements.txt
└── README.md

## Installation

python -m venv .venv

pip install -r requirements.txt

## Usage

python -m app.main

## Testing

python -m pytest

## Design

Explain important architectural decisions.

## Future Improvements

- Improvement 1
- Improvement 2


============================================================
6. DAY 18 CAPSTONE — NOTIFICATION SYSTEM
============================================================

Project structure:

notification_system/
|
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── services.py
│   └── main.py
|
├── tests/
│   ├── __init__.py
│   └── test_services.py
|
├── requirements.txt
├── .gitignore
└── README.md


============================================================
7. MODELS
============================================================

User model:

"""


class User:
    """Represents a notification recipient."""

    def __init__(self, name, email):
        self.name = name
        self.email = email


"""
============================================================
8. NOTIFICATION SERVICES
============================================================

This architecture demonstrates:

- Abstraction
- Dependency Injection
- SOLID
- Polymorphism
"""


from abc import ABC, abstractmethod


class NotificationSender(ABC):
    """Abstract notification sender."""

    @abstractmethod
    def send(self, user, message):
        """Send a notification to a user."""
        pass


class EmailSender(NotificationSender):
    """Send notifications through email."""

    def send(self, user, message):
        return f"Email sent to {user.email}: {message}"


class SMSender(NotificationSender):
    """Send notifications through SMS."""

    def send(self, user, message):
        return f"SMS sent to {user.name}: {message}"


class WhatsAppSender(NotificationSender):
    """
    Send notifications through WhatsApp.

    This is the Day 18 challenge implementation.
    """

    def send(self, user, message):
        return f"WhatsApp sent to {user.name}: {message}"


class NotificationService:
    """
    Coordinates notification delivery.

    The sender is injected from outside instead of being
    directly created inside this class.
    """

    def __init__(self, sender):
        self.sender = sender

    def notify(self, user, message):
        return self.sender.send(user, message)


"""
============================================================
9. MAIN PROGRAM
============================================================

Example usage:

sender = EmailSender()
service = NotificationService(sender)

result = service.notify(
    user,
    "Your application has been submitted."
)

print(result)

Expected:

Email sent to ananya@example.com:
Your application has been submitted.
"""


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


"""
============================================================
10. WHATSAPP EXAMPLE
============================================================

The NotificationService does not need to be modified.

We simply inject another implementation.
"""


def whatsapp_example():

    user = User(
        "Ananya",
        "ananya@example.com"
    )

    sender = WhatsAppSender()

    service = NotificationService(sender)

    result = service.notify(
        user,
        "Hello"
    )

    print(result)


"""
Expected:

WhatsApp sent to Ananya: Hello


============================================================
11. TESTING
============================================================

The actual project should place these tests inside:

tests/test_services.py

Example tests:

"""


def test_email_sender():

    user = User(
        "Ananya",
        "ananya@example.com"
    )

    sender = EmailSender()

    result = sender.send(
        user,
        "Hello"
    )

    assert result == (
        "Email sent to ananya@example.com: Hello"
    )


def test_sms_sender():

    user = User(
        "Ananya",
        "ananya@example.com"
    )

    sender = SMSender()

    result = sender.send(
        user,
        "Hello"
    )

    assert result == (
        "SMS sent to Ananya: Hello"
    )


def test_notification_service():

    user = User(
        "Ananya",
        "ananya@example.com"
    )

    sender = EmailSender()

    service = NotificationService(sender)

    result = service.notify(
        user,
        "Welcome"
    )

    assert result == (
        "Email sent to ananya@example.com: Welcome"
    )


def test_whatsapp_sender():

    user = User(
        "Ananya",
        "ananya@example.com"
    )

    sender = WhatsAppSender()

    result = sender.send(
        user,
        "Hello"
    )

    assert result == (
        "WhatsApp sent to Ananya: Hello"
    )


"""
============================================================
12. SOLID ANALYSIS
============================================================

SRP — Single Responsibility Principle
--------------------------------------

User:
    Handles user data.

NotificationService:
    Handles notification orchestration.

EmailSender:
    Handles email notification behavior.

SMSender:
    Handles SMS notification behavior.

WhatsAppSender:
    Handles WhatsApp notification behavior.


OCP — Open/Closed Principle
----------------------------

The system is open for extension but closed for modification.

For example, we can add:

class WhatsAppSender(NotificationSender):

    def send(self, user, message):
        return f"WhatsApp sent to {user.name}: {message}"

without changing NotificationService.


LSP — Liskov Substitution Principle
------------------------------------

EmailSender, SMSender and WhatsAppSender can be used wherever
NotificationSender is expected.


DIP — Dependency Inversion Principle
-------------------------------------

NotificationService depends on the abstraction:

NotificationSender

rather than directly depending on:

EmailSender


Dependency Injection
--------------------

The dependency is provided from outside:

service = NotificationService(sender)

Instead of:

self.sender = EmailSender()

inside NotificationService.


============================================================
13. PROJECT ARCHITECTURE
============================================================

User
 |
 v
NotificationService
 |
 v
NotificationSender
 |
 +----------------+
 |       |        |
 v       v        v
Email   SMS    WhatsApp


============================================================
14. .gitignore
============================================================

Recommended .gitignore:

.venv/
__pycache__/
*.pyc
.env
.pytest_cache/


============================================================
15. requirements.txt
============================================================

pytest


============================================================
16. GIT WORKFLOW FOR DAY 18
============================================================

Check status:

git status

Stage files:

git add .

Commit:

git commit -m "Day 18 - build SOLID notification system"

Push:

git push origin day6-first-contribution

Check latest commits:

git log --oneline -5


============================================================
17. DAY 18 INTERVIEW QUESTIONS
============================================================

Question 1:
What is the difference between Git and GitHub?

Answer:

Git is a distributed version-control system used to track
changes in source code.

GitHub is a cloud-based platform for hosting Git repositories
and collaborating with other developers.


Question 2:
What is a Git branch?

Answer:

A branch is an independent line of development that allows
developers to work on features or fixes without directly
changing the main branch.


Question 3:
Why do developers use branches?

Answer:

Branches isolate development work, reduce the risk of
breaking the main codebase, and make collaboration easier.


Question 4:
What is a merge conflict?

Answer:

A merge conflict occurs when Git cannot automatically combine
changes because different branches modified the same part of
a file differently.


Question 5:
What makes a good commit message?

Answer:

A good commit message is concise, specific, and explains the
actual change made.

Example:

"Add notification service tests"


Question 6:
Why is a README important?

Answer:

A README explains what a project does, how to install it,
how to use it, how to test it, and important design decisions.
It helps other developers understand the project quickly.


Question 7:
Explain dependency injection using today's notification system.

Answer:

Dependency injection means providing a dependency to a class
from outside instead of creating it internally.

In this project:

sender = EmailSender()

service = NotificationService(sender)

The NotificationService receives its sender dependency from
outside.


Question 8:
Why is NotificationService not directly creating EmailSender?

Answer:

If NotificationService created EmailSender internally, it would
be tightly coupled to one notification method.

By receiving NotificationSender through dependency injection,
the service can work with EmailSender, SMSender, WhatsAppSender,
or future implementations without modifying its own code.


Question 9:
Which SOLID principles are demonstrated?

Answer:

The project demonstrates:

- SRP — Single Responsibility Principle
- OCP — Open/Closed Principle
- LSP — Liskov Substitution Principle
- DIP — Dependency Inversion Principle

Dependency Injection is also used to provide the sender.


Question 10:
How would you add WhatsApp notifications without modifying
NotificationService?

Answer:

Create another implementation of NotificationSender:

class WhatsAppSender(NotificationSender):

    def send(self, user, message):
        return f"WhatsApp sent to {user.name}: {message}"

Then inject it:

sender = WhatsAppSender()

service = NotificationService(sender)

The NotificationService itself does not need to change.


============================================================
18. DAY 18 DSA
============================================================

Required Problem 1:

LeetCode #238
Product of Array Except Self

Focus:

- Prefix product
- Suffix product
- O(n) time
- O(1) extra space excluding output


Required Problem 2:

LeetCode #155
Min Stack

Focus:

- Stack
- Minimum tracking
- O(1) push
- O(1) pop
- O(1) getMin


Review:

LeetCode #15
3Sum

Focus:

- Sorting
- Two pointers
- Duplicate handling
- O(n²) complexity

Do not memorize the solution.

Be able to explain why the solution works.


============================================================
19. OPEN SOURCE — DAY 18
============================================================

Today's task:

Inspect a real Python or AI repository.

Find:

1. One class
2. Its responsibility
3. Its dependencies
4. Whether it follows SRP
5. Whether dependencies are injected
6. One thing you would refactor

Record the findings in:

open_source_day18.md

Goal:

Learn to read production code instead of only collecting
contribution counts.


============================================================
20. DAY 18 CAREER TARGET
============================================================

Weekly target:

5 targeted applications
+
2 networking/referral messages

Target roles:

- AI Engineer Intern
- Applied AI Intern
- Python Backend Intern
- ML Engineer Intern
- GenAI Intern
- Software Engineer Intern

Do not mass-apply randomly.

Focus on targeted applications.


============================================================
21. FINAL DAY 18 CHECKLIST
============================================================

[ ] Understand Git branches
[ ] Understand merge conflicts
[ ] Understand professional commits
[ ] Build notification_system
[ ] Implement EmailSender
[ ] Implement SMSender
[ ] Implement WhatsAppSender
[ ] Write tests
[ ] All tests pass
[ ] Write README
[ ] Create .gitignore
[ ] Create requirements.txt
[ ] Commit project
[ ] Push to GitHub
[ ] Solve LeetCode #238
[ ] Solve LeetCode #155
[ ] Review LeetCode #15
[ ] Complete open-source inspection
[ ] Complete weekly career target
[ ] Answer all 10 interview questions


============================================================
DAY 18 FINAL PRINCIPLE
============================================================

Do not measure today by how much code you copied.

Measure it by this:

"Can I open an empty VS Code folder and independently build
this architecture?"

If yes:

PHASE 1 — SOFTWARE ENGINEERING COMPLETE.


============================================================
PHASE 2 STARTS TOMORROW
============================================================

DAY 19 — BACKEND ENGINEERING

Topics:

- FastAPI
- REST APIs
- HTTP
- API architecture
- Request/response models
- Pydantic
- Routing
- CRUD
- API testing

The goal is to move from:

"I can build Python applications"

to:

"I can build production-style backend APIs."


============================================================
EXECUTION
============================================================
"""


if __name__ == "__main__":
    # Run the main notification-system demonstration.
    main()

    print("\n--- WhatsApp Demo ---")
    whatsapp_example()

    print("\n--- Running Basic Tests ---")
    test_email_sender()
    test_sms_sender()
    test_notification_service()
    test_whatsapp_sender()

    print("All Day 18 demonstration tests passed.")
```
