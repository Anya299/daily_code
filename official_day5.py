#1. String Formatting
# #f-strings ⭐⭐⭐
#Use this most often in interviews/projects.

name = "byA"
age = 19
cgpa = 8.7

print(f"My name is {name}")
print(f"I am {age} years old")
print(f"My CGPA is {cgpa}")

#You can also calculate inside:

a = 10
b = 20

print(f"Sum = {a +b}")

#Formatting decimals

price = 99.5678
print(f"{price:.2f}")

#2. More String Methods
#count()
#Counts occurrences.

text = "banana"
print(text.count("a"))

#startswitch()

email = "byA@gmail.com"
print(email.startswith("byA"))


#endswith
email = "byA@gmail.com"

print(email.endswith(".com"))

#isdigit()
#checks whether all characters are digits

x = "123"
print(x.isdigit())

x = "12a"
print(x.isdigit())

#isalpha()
print("Python".isalpha())

print("123a".isalpha())

#isalnum()
#Letters + numbers:

print("Python123".isalnum())

#join()
words = ["python","DSA","SQL"]
result = " ".join(words)
print(result)

#Interview trap
#split() → string → list

text = "python dsa sql"
words = text.split()
print(words)

#join() → list → string
words = ["python", "DSa","sql"]
text = " ".join(words)
print(text)

#Remember:
#split = break
#join = combine

#4. String Replacement
text = "I love Java"
text = text.replace("Java", "Python")
print(text)

#5. Removing Extra Spaces

text = "         byA        "
print(text.strip())

#Also:

print(text.lstrip())

#removes spaces from the left.

print(text.rstrip())

#removes spaces from the right.

#6. String Comparison
a = "python"
b = "python"

print(a == b)

a = "python"
b = "Python"

print(a == b )

#For case-insensitive comparison:

a = "python"
b = "pythoN"

print(a.lower() == b.lower())

#7. Important Interview Pattern — Normalize Input

name = input("Enter name: ").strip().lower()
print(name)

#This is extremely common in real programs.


#Problem 1 — Username Cleaner ⭐
#Input:

#   ByA   

#Output:

#bya

#Requirements:

#remove extra spaces
#convert to lowercase

name = input("Enter your name: ").strip().lower()

print(name)

#Problem 2 — Count Character ⭐

#Input:

#banana

#Output:

#3

#Count how many times "a" appears

text = input("Enter anything in english: ")
print(text.count("a"))

#Problem 3 — Email Validator

#Ask:

#Enter email:

#Print True if:

#contains "@"
#ends with ".com"

#Example:

#ananya@gmail.com

#Output:

#True

email = input("Enter your email: ")

if "@" in email and email.endswith(".com"):
    print(True)
else:
    print(False)

#Problem 4 — Password Checker ⭐⭐
#Ask for a password.
#Check whether:
#length ≥ 8
#contains a digit
#Example:
#Python123
#Output:
#Strong enough
#Hint:
#len(password)
#password.isdigit()
#But be careful: isdigit() checks whether the whole string is digits.
#You need to think about how to check whether at least one character is a digit.

email = input("Enter your email: ")

if "@" in email and email.endswith(".com"):
    print(True)
else:
    print(False)


#8. Problem 5 — Word Counter ⭐⭐
#Input:
#Python is easy to learn
#Output:
#5
#Hint:
#words = sentence.split()
#Then find the number of words.

sentence = input("Enter your sentence: ")

words = sentence.split()

print(len(words))

#9. Problem 6 — Reverse Words ⭐⭐

#Input:

#Python DSA SQL

#Output:

#SQL DSA Python

#Hint:

#words = sentence.split()

#Then reverse the list.

sentence = input("Enter your words: ")

words = sentence.split()

words.reverse()

print(" ".join(words[::-1]))

#10. Problem 7 — Palindrome Checker ⭐⭐

#Input:

#madam

#Output:

#Palindrome

#Input:

#python

#Output:

#Not Palindrome

#Core idea:

#text == text[::-1]

msg = input("Enter your word: ")

if msg == msg[::-1]:
    print("Palindrom")
else:
    print("Not palindrome")

#11. Problem 8 — Anagram Checker ⭐⭐⭐

#This is an interview-style problem.

#Two strings are anagrams if they contain the same characters.

#Example:

#listen
#silent

#Output:

#Anagram

#Think about:

#sorted()

#Example:

#print(sorted("listen"))
#print(sorted("silent"))

#Both produce the same character sequence.

a = input ("Enter your string1: ")
b = input("Enter your string2: ")

if sorted(a) == sorted(b):
    print("Anagram")
else:
    print("Not Anagram")

#12. Problem 9 — Remove Spaces ⭐⭐

#Input:

#I love Python

#Output:

#IlovePython

#Hint:

#replace()

word = input("Enter : ")
print(word)
print(word.replace(" ",""))

#13. Problem 10 — Find Longest Word ⭐⭐⭐

#Input:

#Python is powerful

#Output:

#powerful

#Think:

#words = sentence.split()

#Then compare their lengths.

#Do not use max() yet if you want stronger problem-solving practice.

#Try solving it with a loop.

msg = input("Enter a sentence: ")

words = msg.split()

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)
