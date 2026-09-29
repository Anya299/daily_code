#Functions: Engineering Level
#I already used :
def add(a,b):
    return a + b
#Now understand what makes a function good engineering
#Bad
def calculate(a,b):
    print(a + b)
#this display only the result
#Better    
def calculate(a,b):
    return a + b
#now another part of your program cna use the result
#result = calculate(a,b)
#print(result)

#Rule
#Functions should generally return data; the caller decides what to do with it.    

#2. Parameters vs Arguments
def greet(name):
    return f"Hello, {name}"
#name : parameter
#"Ananya": argument
greet("Ananya")

#3.Default Arguments
def greet(name="Developer"):
    return f"Hello, {name}"
#Now
print(greet())
print(greet("Ananya"))

#Keyword Arguments
#Instead of
def introduce(name, role):
    return f"{name} is a {role}"

print(introduce("Ananya", "AI Engineer"))

#You can write
print(introduce(
    name ="Ananya",
    role = "AI Engineer"
))
#This becomes very useful when functions have many parameters.

#5. *args
#Suppose you don't know how many arguments will be passed.

def total(*numbers):
    result = 0

    for num in numbers:
        result += num
    return result
#Now
print(total(10,20))
print(total(10,20,30,40))
#*args collects positional arguments into a tuple.
        
#6. **kwargs
#**kwargs collects keyword arguments into a dictionary.        

def profile(**details):
    return details

print(profile(
    name="Ananya",
    role="AI Engineer",
    country="India"
))    

#Remember:
#*args      → tuple
#**kwargs   → dictionary

#7. Scope
#This is important for interviews.
#    x = 20
#    print(x)
#test()
#print(x)

x = 10

def test():
    x = 20
    print(x)
test()

print(x)

#Why?
#Because the x inside the function is local.
#The outside x is global.
#Avoid unnecessary global variables.
#Prefer:

def calculate_salary(salary, bonus):
    return salary + bonus
#instead of relying on variable scattered throughout the program
 
#8.. OOP Begins Today
'''
This is one of the major changes in your roadmap.

Think of a class as a blueprint.

For example:

Class: Student

        ↓

name
branch
cgpa

        ↓

study()
code()

An object is an actual instance created from that blueprint. '''

#9. Your First Class

#Paste this mentally first:

class Student:
    pass
student1 = Student()

#Student = class
#student1 = object

#10. __init__
#Usually we want every object to have some information.

class Student:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

#create an object
student1 = Student("Ananya", "AI & Data Science")

print(student1.name)
print(student1.branch)

#11. What is self?
#This is extremely important.
#self.name
#means: the name belonging to this particular object.
'''For example:

student1 = Student("Ananya", "AI & Data Science")
student2 = Student("Rahul", "Computer Science")

Then:

student1.name

is:

Ananya

while:

student2.name

is:

Rahul

Same class.

Different objects.

Different data.'''

#12. Methods
#Objects can also have behavior.
class Student:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

    def introduce(self):
        return f"I am {self.name} from {self.branch}"

#Then:

#student = Student("Ananya", "AI & Data Science")

#print(student.introduce())            

'''14. YOUR CODING TASKS

Don't copy these from me.

Write them yourself.

Task 1

Create:

def calculate_average(numbers):

Return the average.

Example:

calculate_average([10, 20, 30])

Expected:

20'''

def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)
   

'''Task 2

Create:

def find_maximum(*numbers):

Return the largest number.

Example:

find_maximum(4, 8, 2, 10)

Expected:

10'''

def find_maximum(*numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
           largest = num
    return largest

'''Task 3 — OOP

Create:

class Employee:

It should have:

name
salary

and a method:

annual_salary()

Example:

employee = Employee("Ananya", 50000)

print(employee.annual_salary())

Expected:

600000'''

class Employee:

    def __init__(self, name, salary):
       self.name = name
       self.salary = salary

    def annual_salary(self):
        return self.salary * 12
employee = Employee("Ananya", 50000)
print(employee.annual_salary())

