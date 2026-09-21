name = "Ananya"
college = 'SIET'
message = """This is 
a multiline
strinf"""

print(name)
print(college)
print(message)

#2. String Indexing ⭐
#Python starts counting from 0.

name = "Ananya"

print(name[0])
print(name[1])
print(name[2])

#3. Negative Indexing
#Python can count from the end.

name = "Ananya"

print(name[-1])
print(name[-2])
print(name[-3])

#4. String Slicing ⭐

name = "Ananya"
print(name[0:3])

#Syntax:
# #string[start:end]
#Important:
#start is included, end is excluded.

#More examples

print(name[:3])
print(name[2:])
print(name[:])

#Step
#You can also use:
#string[start:end:step]

name = "Ananya"
print(name[::2])

print(name[::-1])
#🔥 This is a very common interview technique for reversing a string.

#len()

name = "Ananya"
print(len(name))

#index → starts at 0
#length → starts counting at 1

#lower()

text = "HELLO"
print(text.lower())

#upper

greet = "hola"
print(greet.upper())

#strip()

text = "      Ananya       "
print(text.strip())
#It does not remove spaces between words.

#replace()

text = "I LIKE java"

print(text.replace("java", "python"))

#find()

text = " I love pyhton"
print(text.find("python"))
#Finds the position of a substring.


#If it cannot find it:
#print(text.find("Java"))
#returns:
#-1
#🔥 Remember -1.

#split()

text = "Python  SQL AI DSA"
skills = text.split()
print(skills)

#You can also specify a separator:
text = "Python  SQL AI DSA"
print(text.split(","))

#concatenation
#joining strings with +.

first = "Wizard"
last = "liz"

full_name = first + " " + last

print(full_name)

#For modern Python, f-strings are usually cleaner:

print(f"{first} {last}")



#Problem 1 — Character Explorer
#Take a name as input.
#Print:
#first character
#last character
#length
#Example:
#Input: Ananya
#First: A
#Last: a
#Length: 6

name = input("Enter your name: ")
print(name)

first = name([0])
last = name([-1])
length = len(name)

print("First:", first)
print("Last:", last)
print("Length:", length)

#Problem 2 — Reverse a String ⭐
#Input:
#Python
#Output:
#nohtyP
#Use slicing.
#Don't use a loop yet.

name = input("Enter your name: ")
print(name)

print(name[::-1])

#Problem 3 — First Three Characters
#Take a string and print its first 3 characters.
#Example:
#Input: Computer
#Output: Com

string = input("Enter your fav word: ")
print(string[:3])

#Problem 4 — Clean Name
#Input may contain spaces:
#   Ananya
#Remove unnecessary spaces and print:
#Ananya
#Use:
#strip()

name = "         raya                       "
print(name.strip())

#Problem 5 — Case Converter
#Take a string and print:
#UPPERCASE
#lowercase
#Example:
#Input: Python
#PYTHON
#python

text = input("Enter your text: ")
print(text.upper())
print(text.lower())

#Problem 6 — Replace Word
#Given:
#sentence = "I love Java"
#Change Java to Python.
#Expected:
#I love Python

like = "i like to eat biriyani"
print(like.replace("like","love"))

#Problem 7 — Find a Word
#Take a sentence and a word.
#Print the index where the word starts.
#Example:
#Sentence: I love Python
#Word: Python
#Output: 7
#If it doesn't exist, print:
#Not Found

sentence = input("Enter a sentence: ")
word = input("Enter the word: ")

position = sentence.find(word)

if position == -1:
    print("Not Found")
else:
    print("Index:", position)
#Problem 8 — Simple Palindrome ⭐
#A palindrome reads the same forward and backward.
#Examples:
#madam
#level
#racecar
#Take a word and check whether it is a palindrome.

palindrome = input("Enter the palindrome: ")

if palindrome == palindrome[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")    
   

