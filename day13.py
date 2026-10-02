#Day 13 — Software Engineering: OOP II
#1. Class attributes vs instance attributes
#Instance attribute
#Each object has its own value
class Student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

student1 = Student("Ananya",8.5)
student2 = Student("Nandini", 7.8)

#student1.name → Ananya
#student2.name → Rahul

#Class attribute
#Shared by the class

class Student:
    college = "SIET"

    def __init__(self, name):
        self.name = name

#Both objects can access:
#student1.college
# student2.college

#Encapsulation
#Encapsulation means keeping an object's data and the operations that control it together, while controlling how that data is accessed or changed.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
#Instead of allowing random changes everywhere, we put the rules inside the class.

#3. Python's _ and __
# _balance
# self._balance
#Conventionally means: "This is intended for internal use."
#it isn't truly private

#__balance
#self.__balance
#Python applies name mangling, making accidental external access harder.
#For interviews, remember:

#_balance   → protected-style convention
#__balance  → name mangling

#4. Property

#A property lets us expose controlled access to an attribute.

class Employee:

    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value >= 0:
            self._salary = value
        else:
            print("Salary cannot be negative.") 

#Now

employee = Employee(50000)

print(employee.salary)

employee.salary = 60000

#You don't need:

#employee.get_salary()

#The property gives cleaner access.

#5. Class method

#A class method works with the class, not a particular object.

#it uses :  @classmethod

#and: cls

class Employee:
    company = "AI Labs"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

#6. Static method

#A static method doesn't need the object or class.            

class MathTools:

    @staticmethod
    def is_even(number):
        return number % 2 == 0

#use:

print(MathTools.is_even(10))

#Think:
'''
instance method → self
class method    → cls
static method   → neither

This is an important interview question.'''

# Day 13 - OOP II
# Encapsulation, Properties, Class Methods, Static Methods


# --------------------------------------------------
# 1. Class Attribute + Instance Attribute
# --------------------------------------------------

class Student:
    college = "SIET"

    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

    def display(self):
        print(f"Name: {self.name}")
        print(f"CGPA: {self.cgpa}")
        print(f"College: {self.college}")

student1 = Student("Ananya", 8.5)
student2 = Student("Nandini", 7.8)

student1.display()
print()

student2.display()

# --------------------------------------------------
# 2. Encapsulation
# --------------------------------------------------

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit.")
        else:
            self._balance += amount
            print("Deposit successful.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal.")
        elif amount > self._balance:
            print("Insufficient balance.")
        else:
            self._balance -= amount
            print("Withdrawal successful.")

    def show_balance(self):
        print(f"Balance: ₹{self._balance}")


account = BankAccount("Ananya", 1000)

account.show_balance()

account.deposit(2000)
account.show_balance()

account.withdraw(500)
account.show_balance()

account.withdraw(5000)
account.show_balance()
# --------------------------------------------------
# 3. Property
# --------------------------------------------------

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value >= 0:
            self._salary = value
        else:
            print("Salary cannot be negative.")

employee = Employee("Ananya", 50000)

print()
print("Salary:", employee.salary)

employee.salary = 60000

print("Updated Salary:", employee.salary)

employee.salary = -5000

# --------------------------------------------------
# 4. Class Method
# --------------------------------------------------

class Company:

    company_name = "AI Labs"

    def __init__(self, employee):
        self.employee = employee

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name

print()
print("Company :", Company.company_name)

Company.change_company("Open AI Systems")

print("Updated company:", Company.company_name)

# --------------------------------------------------
# 5. Static Method
# --------------------------------------------------

class MathTools:

    @staticmethod
    def is_even(number):
        return number % 2 == 0

    @staticmethod
    def square(number):
        return number * number

print()
print("IS 10 even?", MathTools.is_even(10))
print("Square of 9:", MathTools.square(9))

'''Exercise 1 — Employee

Create:

class Employee:

Use:

name
salary

Make salary controlled through a property.

Rule:

salary < 0 → reject
salary >= 0 → accept'''

class Employee:
    
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value >= 0:
            self._salary = value
        else:
            print("Salary cannot be negative.")        

'''Exercise 2 — BankAccount

Create:

class BankAccount:

Use:

owner
_balance

Methods:

deposit()
withdraw()
show_balance()

Rules:

deposit <= 0 → reject
withdraw <= 0 → reject
withdraw > balance → reject'''

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Reject")
        else:
            self._balance += amount
            print("Deposit Successful.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Reject")
        elif amount <= self._balance:
            print("Withdraw successfull")
        else:
            print("Invalid Withdraw")

    def show_balance(self, amount):
        print(f"Balance: ${self._balance}")

'''Exercise 3 — MathTools

Create:

class MathTools:

Use two static methods:

is_even()
is_prime()'''                             

class MathTools:

    @staticmethod
    def is_even(number):
        return number % 2 == 0

    @staticmethod
    def is_prime(number):
        if number <= 1:
            return False
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False

        return True
'''| Method          | First parameter | Used for                  |
| --------------- | --------------- | ------------------------- |
| Instance method | `self`          | Individual object         |
| Class method    | `cls`           | Class-level data/behavior |
| Static method   | None            | Independent utility       |
'''                        
