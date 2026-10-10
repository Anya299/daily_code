#Day 17 — Software Engineering: Clean Code + SOLID Principles

#1. What is Clean Code?

def x(a,b,c):
    if a:
        if b:
            if c:
                return True

'''It might work.

But another developer has to spend time figuring out:

What are a, b, and c?

Compare:'''

def can_process_payment(user, payment, account):
    if user.is_verified and payment.is_valid and account.has_balance:
        return True
    return False

'''Much easier to understand.

Clean code generally means:
meaningful names
small focused functions
clear responsibilities
minimal duplication
predictable behavior
easy testing
easy modification'''

#2.Meaningful Names
#Bad:

x = 50000
y = 10
z = x * y

#better:

salary = 50000
months = 10
total_salary = salary * months

'''future AI code might contain:

embedding_model
retriever
documents
similarity_score

Those names communicate intent.'''

#3. Functions should have one clear job

#Bad:

def process_user(user):
    validate_user(user):
    save_user(user):
    send_email(user):
    create_invoice(user):
    generate_report(user):

#That's doing many unrelated things.

#Better:

def process_user(user):
    validate_user(user)
    save_user(user)

#Then separately:

#def send_welcome_email(user):
#    ...
#def create_invoice(user):
#    ...

#This leads directly to our first SOLID principle'''

'''4. S — Single Responsibility Principle
SRP

A class should have one primary responsibility and one reason to change.

Suppose:'''

class User:
    def save_to_database(self):
        pass

    def send_email(self):
        pass

    def generate_report(self):
        pass

'''The class has too many responsibilities.'''

#a cleaner design:

class User:
    def __init__(self, name):
        self.name = name

class UserRepository:
    def save(self, user):
        pass

class EmailService:
    def send(self, user):
        pass

class ReportGenerator:
    def generate(self, user):
        pass                

'''Now:

User
 ↓
user data

UserRepository
 ↓
database

EmailService
 ↓
email

ReportGenerator
 ↓
reports

This is much easier to test and modify.'''



'''5. O — Open/Closed Principle

Software should be open for extension but closed for modification.

Sounds complicated.

Imagine:'''

def calculate_discount(customer_type):
    if customer_type == "student":
        return 0.10
    elif customer_type == "employee":
        return 0.20
    elif customer_type == "premium":
        return 0.30

'''Every time a new customer type appears, you modify this function.
A better design can use separate strategies/classes.'''

class Discount:
    def calculate(self, amount):
        return 0

class StudentDiscount(Discount):
    def calculate(self, amount):
        return amount * 0.10

class PremiumDicount(Discount):
    def calculate(self, amount):
        return amount * 0.30

#Now adding

class EmployeeDiscount(Discount):
    def calculate(self, amount):
        return amount * 0.20

#doesn't require changing existing discount classes.

#That's the basic idea of Open/Closed.                              

#6. L — Liskov Substitution Principle

'''This sounds scary but the idea is simple.

A child class should be usable wherever its parent class is expected without breaking the program's expected behavior.

Classic example:'''

class Bird:
    def fly(self):
        print("Flying")

#then
# class penguin(Bird):
#   def fly(self):
#     print("flying") 
# this design is problematic
# why?
# Beacuse the program expects:
# bird.fly()
# to work for every bird
# instead, model the abstraction correctly

class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        print("Flying")

class Penguin(Bird):
    pass

class Eagle(FlyingBird):
    pass

'''Now the hierarchy better reflects behavior.

Interview answer

LSP means subclasses should preserve the expected behavior of their base class.'''

#7. I — Interface Segregation Principle

#A class should not be forced to depend on methods it does not need.

#Imagine:

class Machine:

    def print_document(self):
        pass

    def scan_documenty(self):
        pass
    def fax_documnet(self):
        pass


'''Now imagine a simple printer that only prints.

It shouldn't be forced to implement:

scan
fax

Instead, separate interfaces/abstract classes.'''

from abc import ABC, abstractmethod

class Printable(ABC):

    @abstractmethod
    def print_document(self):
        print("Printing....")
        pass

class Scannable(ABC):

    @abstractmethod
    def scan_documnet(self):
        pass


'''8. D — Dependency Inversion Principle

This one is especially important for your future FastAPI + AI projects.

High-level code should depend on abstractions rather than concrete implementations.

Bad:

class AIService:

    def __init__(self):
        self.model = OpenAIModel()

Now AIService is tightly connected to OpenAIModel.

If you later want:

OpenAI
↓
Gemini
↓
Ollama
↓
local model

you have to modify the service.

Instead:

class AIService:

    def __init__(self, model):
        self.model = model

    def generate(self, prompt):
        return self.model.generate(prompt)

Now:

service = AIService(OpenAIModel())

or:

service = AIService(OllamaModel())

The AIService doesn't care which implementation it receives.

This leads to dependency injection.'''

#9. Dependency Injection

#Dependency injection means:

#Instead of creating a dependency inside a class, provide it from outside.

#Bad:

class NotificationService:
    def __init__(self):
        self.email = EmailService()

#Better:

class NotificationService():
    def __init__(self, email_service):
        self.email = email_service

#then

email = EmailService()

notification = NotificationService(email)

#This is easier to test because you can provide a fake service.

'''10. Why this matters for AI engineering

Imagine your future application:

FastAPI
   ↓
AI Service
   ↓
Model Provider

You don't want:

FastAPI
   ↓
hardcoded OpenAI API

Instead:

FastAPI
   ↓
AIService
   ↓
Model interface
   ↓
 ┌─────────┬─────────┬─────────┐
OpenAI   Gemini    Ollama

Now you can change the model provider without rewriting the entire application.

This is software engineering, not just Python syntax.'''


from abc import ABC, abstractmethod

# --------------------------------------------------
# 1. Model abstraction
# --------------------------------------------------

class AIModel(ABC):
    @abstractmethod
    def generate(self, prompt):
        pass

# --------------------------------------------------
# 2. Concrete implementations
# --------------------------------------------------

class OpenAIModel(AIModel):
    def generate(Self, prompt):
        return f"OpenAi response for: {prompt}"

class OllamaMode(AIModel):
    def generate(self, prompt):
        return f"Ollama response for: {prompt}"

# --------------------------------------------------
# 3. Dependency Injection
# --------------------------------------------------

class AIService:
    def __init__(self,model):
        self.model = model

    def ask(self, prompt):
        return self.model.generate(prompt)                      

# --------------------------------------------------
# 4. Application
# --------------------------------------------------

openai_model = OpenAIModel()

service = AIService(openai_model)

print(service.ask("Explain Python OOP."))


ollama_model = OllamaModel()

service = AIService(ollama_model)

print(service.ask("Explain machine learning."))


'''Notice:

AIService(model)

doesn't care whether model is:

OpenAI
Ollama
Gemini
another model

as long as it follows the expected interface.'''

#12. Refactoring exercise

#Here's deliberately bad code:

class Order:

    def __init__(self, items):
        self.items = items

    def calculate_total(self):
        total = 0

        for item in self.items:
            total += item["price"] * item["quantity"]

        return total

    def save_to_database(self):
        print("Saving order to database...")

    def send_email(self):
        print("Sending confirmation email...")

    def generate_invoice(self):
        print("Generating invoice...")

#whats wrong?
# order is responsible for 
'''        Order data
+
calculation
+
database
+
email
+
invoice'''

#That's a violation of SRP
#Acleaner version

class Order:
    def __init__(self, items):
        self.items = items
    def calculate_total(self):
        total = 0

        for item in self.items:
            total += item["price"] * item["quantity"]

        return total

class OrderRepository:
    def save(self, order):
        print("Saving order to databases...")

class EmailService:

    def send_confirmation(self, order):
        print("Sending confirmation email....")

class InvoiceService:
    def generate(self, order):
        print("Generating invoice....")

#Now each class has a clearer responsibility.



 '''14. Day 17 interview questions

Answer these from memory after coding:

What is clean code?
What is SRP?
What is OCP?
What is LSP?
What is ISP?
What is DIP?
What is dependency injection?
Why is dependency injection useful for testing?
Difference between inheritance and composition?
Why should an AI service not be tightly coupled to one model provider?
The one-line version to memorize conceptually
SRP → One responsibility
OCP → Extend without repeatedly modifying existing code
LSP → Child should safely substitute parent
ISP → Don't force unnecessary methods
DIP → Depend on abstractions, not concrete implementations

Don't memorize those mechanically—understand the problem each one prevents.'''

