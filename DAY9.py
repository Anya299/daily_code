#PART 1 -- for LOOP
#you already know lists.Now we use loops to process them

numbers = [10,20,30,40]

for num in numbers:
    print(num)

#Think:

#num = 10 → print
#num = 20 → print
#num = 30 → print
#num = 40 → print

#basic pattern 

for item in collection:
    #do something

#this is one of the most important patterns in python/dsa.

#PART 2 -- range()
#range() genrates numbers

for i in range(5):
    print(i)

#range(stop) starts at 0 , stops before stop.
#start and stop
for i in range(2,6):
    print(i)

#step
for i in range(0,10,2):
    print(i)

#reverse
for i in range(5,0,-1):
    print(i)

#interview rule
#range(start,stop,step)
# stop is never included

#PART 3 — LOOP THROUGH INDEXES
#Sometimes we need the index, not just the value.

numners = [10,20,30,40]

for i in range(len(numbers)):
    print(i, numbers[i])
#Think:
#i = index
#numbers[i] = value

#PART 4 — enumerate()

#There is an easier way.

numbers = [10,20,30,40]

for i, num in enumerate(numbers):
    print(i, num)

    #same result
    #remember : enumerate(list)
    #gives index + value

#PART 5 -- while LOOP
#A while loop continues while a condition is true

i = 0

while i < 5:
    print(i)
    i += 1
#(i += 1) without changing i, you can accidently create an infinte loop

#for vs while
#use for 
# when you know what you're iteration over

for num in numbers:
    print(num)

#use while
#when the loop depends on a condition

#while password != correct_password:
# ...

#for dsa you'll frequently see:
# while left < right:
#that's extemely imp

#PART 6 -- if/elif/else
# you already completed conditionals, so today we only use them inside loops.
# example

numbers = [1,2,3,4,5]

for num in numbers:
    if num % 2 == 0:
        print(num, "even")
    else:
        print(num, "odd")
#this is where python starts becoming actual problem solving

#PART 7 -- NESTED LOOPS
#A Loop inside another loop

for i in range(3):
    for j in range(3):
        print(i,j)

'''Think:

i = 0
    j = 0
    j = 1
    j = 2

i = 1
    j = 0
    j = 1
    j = 2

i = 2
    j = 0
    j = 1
    j = 2

The inner loop completes for every iteration of the outer loop.'''    

#why nested loops matter for dsa

#suppose
nums = [1,2,3,4]

#we want every pair

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        print(nums[i], nums[j])

#PART 8 -- ARRAY PATTERN 1: TRAVERSAL
# problem: find the largest number
# understand: we need to inspect every element
# example: [3,8,2,10,5]
# answer : 10
# Brute force idea
# python's
# max(nums)
# works, but interviewers often want you to understand the logic.

def find_largest(nums):
    largest = nums[0]

    for num in nums:
        if num > largest:
            largest = num
    return largest              

'''Dry run
largest = 3

8 > 3 → largest = 8

2 > 8 → no

10 > 8 → largest = 10

5 > 10 → no

Answer:

10
Complexity
Time: O(n)
Space: O(1)'''

#PART 9 — ARRAY PATTERN 2: COUNTING
#Problem: Count how many even numbers exit
#Example: [1,4,7,8,10]
#Answer: 3

def count_even(nums):
    count = 0

    for num in nums:
        if num % 2 == 0:
            count += 1
    return count

'''Pattern
count = 0

for item:
    if condition:
        count += 1

This pattern is extremely important.'''

#PART 10 -- ARRAY PATTERN 3: SEARCHING
#problem: find whether a target exists
#Example:

#nums = [4, 8, 2, 9]
#target = 8

def contains_target(nums, target):
    for num in nums:
        if num == target:
            return True
    return False

'''Dry run
4 == 8 ❌
8 == 8 ✅
return True

Notice something important:

We stop immediately after finding it.'''

#PART 11 -- SEARCHING WITH INDEXD
#sometimes we need the position

def find_index(nums, target):
    for i, num in enumerator(nums):
        if num == target:
            return i
    return -1

'''Example:

print(find_index([10, 20, 30], 20))

Output:

1

If not found:

-1

This -1 convention appears frequently in programming.'''

#PART 12 — BASIC PREFIX THINKING

'''This is your first introduction to a very important DSA idea.

Suppose:

nums = [2, 4, 3, 5]

We want the sum from the beginning up to each position.

Think:

2
2 + 4 = 6
2 + 4 + 3 = 9
2 + 4 + 3 + 5 = 14

So:

[2, 6, 9, 14]

This is a prefix sum array.'''

def prefix_sum(nums):
    result = []
    total = 0

    for num in nums:
        total += num
        result.append(total)

    return result

'''Example:

print(prefix_sum([2, 4, 3, 5]))

Output:

[2, 6, 9, 14]'''

'''🧠 WHY PREFIX SUM?

Suppose you repeatedly need sums of sections of an array.

Without prefix sums, you may repeatedly add elements.

With prefix sums:

prefix[right] - prefix[left - 1]

can give a range sum.

You don't need to master range-sum problems today.

Today just remember:

Prefix = information accumulated from the beginning.'''

#🧩 DAY 9 PRACTICE — DO THESE YOURSELF

#problem 1:
'''Problem 1

Write:

def count_positive(nums):

Return the number of positive numbers.

Example:

[-2, 5, 7, -1, 3]

Answer:

3'''

def count_positive(nums):
    count = 0

    for num in nums:
        if num > 0:
        count += 1

    return count

'''Problem 2

Write:

def find_smallest(nums):

Example:

[7, 2, 9, 1, 5]

Answer:

1'''

def find_smallest(nums):
    smallest = nums[0]

    for num in nums:
        if num < smallest:
        smallest = num
    return smallest

'''Problem 3

Write:

def find_index(nums, target):

Return the index of the target.

Example:

nums = [10, 20, 30, 40]
target = 30

Answer:

2'''

def find_index(nums, target):
    for i, num in enumerate(nums):
        if num == target:
        return i
    return -1

'''Problem 4

Write:

def count_occurrences(nums, target):

Example:

nums = [2, 3, 2, 5, 2]
target = 2

Answer:

3'''

def count_occurrences(nums, target):
    count = 0

    for num in nums:
        if num == target:
            count += 1
    return count


'''Problem 5

Write:

def prefix_sum(nums):

Example:

[1, 2, 3, 4]

Answer:

[1, 3, 6, 10]'''

def prefixfd_sum(nums):
    result = []
    total = 0

    for num in nums:
        total += num 
        result.append(total)
    return result

