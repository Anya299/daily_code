#1️⃣ LIST
#A list stores multiple values.
#Lists are mutable.
#That means you can change them.
numbers = [10,20,30,40]
print(numbers[0])
print(numbers[1])
#list are mutable
#that means you can change them
numbers[0] = 100
print(numbers)
#important methods
#numbers.append(50)
#numbers.remove(20)
#numbers.pop()
#numbers.sort()
#numbers.reverse()

#interview idea
numbers = [1,2,3]
numbers[0] = 100

#Tuple
#a tuple looks like 

student = ("Ananya",20,8.5)
#Access:

print(student[0])

#tuples are immutable
#when would you use one?
#when the data shoudn't normally change

cordinates = (10,20)

#set
#A set stores unique values

numbers = {1,2,3,3,3}
print(numbers)

#duplicate disappear
#very usefull for dsa
names = ["Ananya","Diya", "Ananya","Nandini"]
unique_names = set(names)
print(unique_names)

#sets are extremely usefull for:
#duplicate detection
#membership checking
#unique elements
skills = ["Python","JAva","html"]
if "Python" in skills:
    print("Python found")

#Dictinory
#This is one of the most imp python structures for dsa and interviews.
#example

student = {
    "Name" : "Ananya",
    "age" : 20,
    "cgpa" : 8.5
}

#Access

print(student["Name"])
print(student["cgpa"])

#change
student["cgpa"] = 9.0
#add
student["branch"] = "AI"

#why dictinories matter for dsa
#consider

nums = [1, 2, 3, 2, 1, 2]

#like how many times does each number appear?
#we can use dictionary

frequency = {}
for num in nums:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
print(frequency)

#this idea is called frequency counting
#you will use it repeatedly

#Mutable: can be changed after creation
#list
#set
#dictionary

#Immutable: cannot be changed after creation
#int
#float
#string
#tuple
#bool

#this is common interview question

## DAY 6 - PYTHON COLLECTIONS

# 1. LIST
numbers = [10, 20, 30, 40, 50]

print("First:", numbers[0])

numbers.append(60)
numbers[1] = 200

print("List:", numbers)


# 2. TUPLE
student = ("Ananya", 20, 8.5)

print("Name:", student[0])
print("CGPA:", student[2])


# 3. SET
skills = {"Python", "SQL", "Python", "DSA"}

print("Skills:", skills)


# 4. DICTIONARY
student_info = {
    "name": "Ananya",
    "age": 20,
    "cgpa": 8.5
}

print("Student:", student_info)
print("Name:", student_info["name"])

student_info["cgpa"] = 9.0

print("Updated CGPA:", student_info["cgpa"])

#Problem 1 — List
#Given:
#numbers = [10, 20, 30, 40, 50]
#Print:
#10
#50
#Then add 60.

numbers = [10, 20, 30, 40, 50]
print(numbers[0])
print(numbers[1])
numbers.append(60)
print(numbers)

#Problem 3 — Frequency counting ⭐
#Given:
#numbers = [1, 2, 2, 3, 1, 2]
#Create a dictionary containing:
#1 → 2
#2 → 3
#3 → 1
#This is your first real DSA-style Python problem.
nums = [1, 2, 2, 3, 1, 2]

frequency = {}

for num in nums:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print(frequency)
