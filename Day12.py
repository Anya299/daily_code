#1.what is oop?
#Instead of keeping data and fucntions separataely
name = "Ananya"
age = 20

def introduce(name,age):
    print(f"I am {name}, age {age}")

#we can group realated data + behavior together

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce():
        print(f"I am {self.name}, age{self.age}")

#then 

student1 = Student("Ananya", 20)

student1.introduce()

'''
2. Class vs Object

Think:

Class = blueprint
Object = actual thing created from blueprint

Example:

class Car:
    pass

Car is the blueprint.

car1 = Car()
car2 = Car()

car1 and car2 are objects.'''

#3.__init__
#Tihs runs automatically when you create an object

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
#when
student = Student("Ananya",20)

#Python essentially initializes:

#student.name = "Ananya"
#student.age = 20        

'''4. What is self?

This is extremely important for interviews.

class Student:

    def __init__(self, name):
        self.name = name

self means:

the current object

So:

student1 = Student("Ananya")
student2 = Student("Rahul")

means:

student1.name → Ananya
student2.name → Rahul

Each object gets its own data.'''

#Methods
#A function inside a class is called a method

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print(self.name)
        print(self.marks)

#Usage
student = Student("Ananya", 85)
student.display()

# --------------------------------------------------
# 1. Basic Class
# --------------------------------------------------

class Student:
    def __init__ (self, name, age, cgpa):
        self.name = name
        self.age = age
        self.cgpa = cgpa

    def introduce(self):
        print(f"My name is {self.name}.")
        print(f"I am {self.age} years old.")
        print(f"My cgpa is {self.cgpa}")

    def is_high_cgpa(self):
        return self.cgpa >= 8.0

# --------------------------------------------------
# 2. Create Objects
# --------------------------------------------------

student1 = Student("Ananya",20,8.5)
student2 = Student("Rahul",21,7.6)

# --------------------------------------------------
# 3. Use Methods
# --------------------------------------------------

student1.introduce()
print()
student2.Introduce()

# --------------------------------------------------
# 4. Access Attributes
# --------------------------------------------------

print()
print("Student 1 name:", student1.name)
print("Student 2 cgpa:", student2.cgpa)

# --------------------------------------------------
# 5. Use Method with Condition
# --------------------------------------------------

print()

if student1.is_high_cgpa():
    print("Student 1 has a high CGPA.")
else:
    print("Student 1 need Improvement.")

if student2.is_high_cgpa():
    print("Student 2 has a high CGPA.")
else:
    print("Student 2 need Improvement.")    

# --------------------------------------------------
# 6. Another Real-World Class
# --------------------------------------------------

class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")
    def show_balance(self):
        print(f"{self.owner}'s balance: ${self.balance}")

# --------------------------------------------------
# 7. Bank Account Object
# --------------------------------------------------

account = BankAccount("Ananya", 10000)

account.show_balance()

account.deposit(2000)
account.show_balance()

account.withdraw(3000)
account.show_balance()

account.withdraw(15000)

#Exercise 1

#Create:

#class Employee:

#Attributes:

#name
#salary
#role

#Method:

#display()

#It should print all three.

class Employee:
    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role
    def display(self):
        print(f"The Employee name is {self.name}.")
        print(f"salary is {self.salary}.")
        print(f"The perticular employee role is {self.role}.")
employee1 = Employee("Ananya", 50000,"AI Engineer")

employee1.display()


#Exercise 2

#Create:

#class Rectangle:

#Attributes:

#length
#width

#Methods:

#area()
#perimeter()       

class Rectangle:
    def __init__(self,area,parameter):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimimeter(self):
        return 2 * (self.length + self.width)

rectangle = Rectangle(10, 5)

print("Area: ", rectangle.area())
print("Perimeter:", rectangle.perimeter())


#Exercise 3

#Create:

#class BankAccount:

#Methods:

#deposit()
#withdraw()
#show_balance()

#Add the rule:

#withdrawal > balance → reject               

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print("Deposit Successfully.")
    def withdraw(self, amount):
        if self.balance <= amount:
            self.balance -= amount
            print("Withrow is done.")
        else:
            print("insufficient balance.")
    def show_balance():
        print(f"{self.owner}'s balance: ${self.balance}")

account = BankAccount("Ananya", 10000)

account.show_balance()

account.deposit(2000)
account.show_balance()

account.withdraw(3000)
account.show_balance()

account.withdraw(15000)
account.show_balance()       




