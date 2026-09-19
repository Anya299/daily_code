#arithmetic operation
a = 10
b= 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

#  /   → division
#  //  → floor division
#  %   → remainder
#  **  → power

#comparison operators

a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#x = 10      # assignment

#x == 10     # comparison

#Logical operators

#and (Both must be true.)

age = 20
cgpa = 8.5

print(age >=18 and cgpa >= 8.0)

#or (At least one must be true.)

print(age >= 10 or cgpa >= 9)

#not (reverse True/False)

is_student = True
print(not is_student)

#Assignment operators

x = 10

x += 5    #x = x + 5
print(x)

x -= 2
print(x)

x *= 3
print(x)

x /= 2
print(x)

#Membership operators(Used to check whether something exists inside a sequence.)

name = "Ananya"

print("A" in name)
print("z" in name)
print("z" not in name)

numbers = [10, 20, 30]

print(20 in numbers)
print(50 not in numbers)

#identity operators 

user = None

print(user is None)
print(user is not None)

# a == b (do these have the same value? )
# a is b (are these the same object? )


#Operator precedence

#basic order 

#  ()
#  **
#  * / // %
#  + -
#  comparisons
#  not
#  and
#  or

result = 2 + 3 * 4
print(result)

result = (2 + 3) * 4

#Problem 1 — Arithmetic Calculator
#Take two integers and print:
#Sum
#Difference
#Product
#Division
#Floor Division
#Remainder
#Power

a = 10
b = 2

print("Input:" )
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)


#Problem 2 — Even or Odd
#Take a number.
#Print:
#Even
#if divisible by 2, otherwise:
#Odd
#Use %.

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#Problem 3 — Age Check
#Take age as input.
#Print whether:
#True
#or
#False
#for:
#age >= 18 

age = int(input("Enter your age: "))

if age >= 18:
    print("True")
else:
    print("False")

#Problem 4 — Student Eligibility
#Input:
#age
#cgpa
#Eligible if:
#age >= 18 and cgpa >= 7
#Output:
#Eligible
#or
#Not Eligible 

age = int(input("Enter your age: "))
cgpa = float(input("Enter your CGPA: "))

if age>=18 and cgpa>=8.0:
    print("Eligible")
else:
    print("Not Eligible")

#Problem 5 — Number Range
#Take a number.
#Check whether it is between 10 and 50 inclusive.
#Condition:
#number >= 10 and number <= 50

num = int(input("Enter a number: "))
print(num >= 10 and num <= 50 )

#Problem 6 — Membership Check
#Use:
#skills = "Python SQL AI DSA"
#Check whether:
#Python
#Java
#AI
#are present.

skills =  "Python SQL AI DSA"
print("Python" in skills)
print("Java" in skills)
print("AI" in skills)

#Problem 7 — Salary Calculator
#Take:
#increment percentage
#Calculate the new salary.
#Example:
#Salary = 50000
#Increment = 20
#Output:
#60000
#Formula:
#new_salary = salary + (salary * increment / 100)

salary = 50000
increment = 20
new_salary = salary + (salary * increment / 100)
print(new_salary)

#Problem 8 — Last Digit
#Take a number and print its last digit.
#Example:
#Input: 4587
#Output: 7

num = int(input("Enter a number: "))
print( num % 10 )

#Problem 9 — Predict the Output
#Don't run it first.
x = 10
y = 20
print(x > 5 and y < 30)
print(x > 15 or y == 20)
print(not(x == 10))
#Write down the three outputs first.

#Problem 10 — Placement Eligibility ⭐
#Build this:
#Take:
#CGPA
#Backlogs
#Age
#A student is eligible when:
#cgpa >= 8
#and backlogs == 0
#and age >= 18
#Output:
#Eligible
#or:
#Not Eligible
#This combines:
#arithmetic/input
#comparison
#logical operators

cgpa = float(input("Enter your cgpa: "))
backlogs = int(input("Enter the number of backlogs you have right now: "))
age = int(input("Enter your age: "))

if cgpa >= 8 and backlogs == 0 and age >= 18:
    print("your ELIGIBLE")
else:
    print("NOT ELIGIBLE")    


