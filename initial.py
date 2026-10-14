print("Rayaridare...")
print("Hello, anya")
print("My python placement journey starts today!")

#print() displays something on the screen.
print("Ananya")
print(20)
print(10 + 5)
print("Python" + "Placement")

#Printing multiple things
name = "Ananya"
age = 19
print(name, age)

#can also do 
print("Name:", name)
print("Age:", age)

#Comments
#This is a comment

#Indentation ⭐
age = 20

if age >= 18:
    print("Adult")

#mini exercise

name = "Ananya"
age = 19
college = "SIET"

print("Name:", name)
print("Age:", age)
print("College:", college)

#Hello
#I am learning Python
#I want to crack a high-paying placement

print("Hello")
print("I am learning python")
print("I want to crack a hifh-paying placement")

#Problem 2

#Print your:

#name
#age
#college
#goal

name = "Ananya"
age = 19
college = "SIET"
goal = "Happiness"

print("NAme:", name)
print("Age:", age)
print("College:", college)
print("Goal:", goal)

#Problem 3

#Make Python calculate:

#25 + 15
#25 - 15
#25 * 15
#25 / 15

print(25 + 15)
print(25 - 15)
print(25 * 15)
print(25 / 15)

#Problem 4 ⭐

#Write a program that prints:

#====================
#PYTHON PLACEMENT
#====================
#Day: 1
#Status: Started
#Goal: High Company
#====================

print("========================")
print("PYTHON PLACEMENT")
print("========================")
print("Day: 1")
print("Status: Started")
print("Goal: High Company")
print("========================")

#Variables
#A variable stores a value.

name = "Ananya"
age = 20
cgpa = 9.0
is_student = True

#Think:
#name      → "Ananya"
#age       → 20
#cgpa      → 9.0
#is_student → True

#Think:

#name      → "Ananya"
#age       → 20
#cgpa      → 9.0
#is_student → True

print(name)
print(age)
print(cgpa)
print(is_student)

#Changing a variable--A variable can be reassigned.


age = 20
print(age)
age = 21
print(age)

#Multiple variables

name, age, city = "Ananya", 20, "Tumkur"

print(name)
print(age)
print(city)

#input() allows the user to enter information.
name = input("Enter your name: ")
print("Hello", name)

#input() always returns a string initially so...
age = int(input("Enter your age: "))
print(type(age))

#input() with numbers
age = int(input("Enter your age: "))
print(age + 1)

#Decimal
cgpa = float(input("Enter your CGPA: "))
print(cgpa)

#Problem 1 — Personal information
#Ask the user for:
#name
#age
#college

print(input("Your name: "))
print(int(input("Your age: ")))
print(input("YOur College name: "))

#Problem 2 — Addition
#Ask the user for two numbers and print their sum.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
sum = (a + b)
print("Sum: ", sum)


#Problem 3 — Age calculator
#Ask for the user's current age.
#Print their age after 5 years.

age = int(input("Enter your current age: "))
sum = (age + 5)
print("Age after 5 years: ", sum)

#Problem 4 — Rectangle
#Ask for:
#length
#width
#Calculate:
#Area = length × width

length = float(input("length: "))
width = float(input("Width: "))
Area = length * width
print("Area: ", Area)

#🔥 Mini placement challenge

name = input("Enter your name:")
age = int(input("Enter your age:"))
branch = input("Enter your branch:")
cgpa = float(input("Enter your cgpa:"))
cmp = input("Enter your target company:")

print("------STUDENT_PROFILE-------")
print("Name: ", name)
print("Age: ", age)
print("Branch: ", branch)
print("CGPA: ", cgpa)
print("Target Comapny: ", cmp)
print("THANK YOU:)")

#🟢 Problem 1 — Sum of Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
sum = a + b
print("Sum: ",sum)

#🟢 Problem 1 — Sum of Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
sum = a + b + c
print(("Sum: ", sum))
avg = sum / 3
print(("Average: ", avg))

#🟢 Problem 4 — Simple Interest
P = float(input("Enter principal amount: "))
R = float(input("Enter rate of interest: "))
T = float(input("Enter the time: "))

SI = (P * R * T) / 100

print("Simple Interst: ", SI)

#🔵 Problem 5 — Placement Salary Calculator
sn = input("Enter your name: ")
cs = float(input("Enter your current salary: "))
es = float(input("Enter your Expected Salary: "))

sir = es - cs

print("==============================")
print("PLACEMENT PROFILE")
print("==============================")
print("Name: ",sn)
print("Curent Salary: ",cs)
print("Expected Salary: ", es)
print("Required Salary: ", sir)
print("==============================")
