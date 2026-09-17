#int
age = 20
marks = 85
year = 2025

print(type(age))

#float 
cgpa = 8.7
price = 99.50
temperature = 36.5

print(type(cgpa))

#important

a = 10
b = 10.0
print(type(a))
print(type(b))

#str

name = "Ananya"
college = "SIET"
language = 'python'

#a string can contain numbers, but it's not an integer
age = "20"

print(type(age))

#bool

is_student = True
has_job = False

print(type(is_student))

#for example

age = 20

print(age >= 18)

#None

result = None

print(result)
print(type(result))

#for example

user = None

if user is None:
    print("no user found")

#none is not a 0 or false instead it is its own special value

#type()

print(type(10))
print(type(10.5))
print(type("python"))
print(type(True))
print(type(None))

#it tells about object's type

#type conversion

age = "20"
age = int(age)

print(age)
print(type(age))

#string to float

price = "99.5"
price = float(price)
print(price)

#integer to float

x = 10
y = float(x)
print(y)

#float to int

x = 10.0
y = int(x)
print(y)

#it does not rounf it removes the decimal portion

#boolean string

age = 10

text = str(age)

print(text)
print(type(text))

#boolean conversion

print(bool(0))
print(bool(1))

bool("")
bool("hello")
bool(0)
bool(10)
#this is called truthiness

#important

a = input("Enter number: ")
b = input("Enter number: ")

print(a + b)

#If you enter:

10
20

#Output:

1020

#because input() returns strings.

#Correct:

a = int(input("Enter number: "))
b = int(input("Enter number: "))

print(a + b)

#Output:

30

#Remember this permanently:

#input() → str by default.


#Problem 1 — Type Explorer
#Create variables:
#age
#cgpa
#name
#is_student
#result
#Give them appropriate values.
#Print each value and its type.

age = 10
cgpa = 8.5
name = "anya"
is_student = True
result = None

print(age, cgpa, name, is_student, result)
print(type(age), type(cgpa), type(name), type(is_student), type(result))

#Problem 2 — Input Conversion
#Ask the user for:
#age
#CGPA
#name
#Convert age to int and CGPA to float.
#Print their values and types.

age = int(input("Enter your age: "))
cgpa = float(input("Enter your CGPA: "))
name = input("Enter your name: ")

age = int(age)
cgpa = float(cgpa)

print(age, cgpa, name)
print(type(age), type(cgpa), type(name))

#ake two numbers as input.
#Print:
#Sum
#Difference
#Product
#Division
#Make sure the inputs are converted to numbers.

a = input("Enter first number: ")
b = input("Enter second number: ")
a = int(a)
b = int(b)

print("Sum: ", a+b)
print("Difference: ", a-b)
print("Product: ", a*b)
print("Divison: ", a/b)

#Problem 3 — Calculator
#Take two numbers as input.
#Print:

#Sum
#Difference
#Product
#Division
#Make sure the inputs are converted to numbers.
#Problem 4 — Temperature
#Take Celsius as input.
#Convert it to Fahrenheit:
#F = (C × 9/5) + 32

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit: ", fahrenheit)

#Problem 5 — String to Number ⭐
#Start with:
#x = "100"
#Convert it to an integer and calculate:
#100 + 50
#Expected:
#150

x = "100"
x = int(x)
print(x + 50)

#Problem 6 — Boolean Challenge
#Take an age as input.
#Create a Boolean variable that represents whether the person is 18 or older.
#Example:
#Enter age: 20
#Adult: True

age = int(input("Enter your age: "))
is_adult = age >= 18
print("Adult:", is_adult)

#Problem 7 — Data Type Detective 🔥
#Without running the code first, predict the output:

a = "10"
b = 20
c = 2.5
d = True
e = None

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

#Problem 8 — ⭐ Placement Challenge

name = input("Enter stududent name: ")
age = int(input("Enter student age: "))
cgpa = float(input("Enter student CGPA: "))

age = int(age)
cgpa = float(cgpa)
add = (cgpa + 0.2)
is_cgpa >= 8.0

print("==============================")
print("STUDENT DATA")
print("==============================")
print("Name: ", name)
print("Age: ", age)
print("CGPA: ", cgpa)
print("CGPA after improvement: ",cgpa)
print("CGPA >= 8.0: ", is_cgpa)
print("==============================")

