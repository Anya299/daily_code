#1st List Basics
#A list stores multiple values.
numbers = [10,20,30,40,50]
#lists are:
#ordered
#indexed
#mutable
#allow duplictes

#Access
print(numbers[0])
print(numbers[2])
print(numbers[-1])

#list operations
#add
numbers.append(60)

#adds 15 at indexd 1.
numbers.insert(1,15)

#remove by value
numbers.remove(30)

#remove by index
numbers.pop(2)

#length
len(numbers)

#check existencs
if 20 in numbers:
    print("Found")

#Indexing

names = ["Ananya", "EEya", "nandini","raya"]

print(names[0])
print(names[1])
print(names[-1])
print(names[-2])

#interview trap 
#print(names[4])
#Indexerror
#because the indexes are 0 1 2 3

#slicing
#syntax
#list[start:stop]
#stop is excluded
numbers = [10,20,30,40,50]
print(numbers[1:4])
#from begining
numbers[:3]
#until end
numbers[2:]
#copy using slicing
copy = numbers[:]
#reverse
numbers[::-1]

#Mutation
#list can be changed after creation
numbers = [10,20,30]
numbers[1] = 99
print(numbers)
#this is called mutation
#compare
name = "Ananya"
#strings cannot be changed directly
#but
numbers[0] = 100
#works because lists are mutable

#copying very important
#this is a common interview question
#this does not create an independent copy

a = [1,2,3]
b = a

b[0] = 99

print(a)

#because a and b refer to the same list

#proper copy 
a = [1,2,3]
b = a.copy()
b[0] = 99
print(a)
print(b)

#creates a shallow copy
b = a[:]

#important list methods
numbers = [3,1,4,2]

#append
numbers.append(5)

#insert
numbers.insert(1,100)

#remove
numbers.remove(4)

#pop
numbers.pop()

#sort
numbers.sort()

#reverse
numbers.reverse()

#count
numbers.count(2)

#index
numbers.index(2)

#clear
numbers.clear()

#important

numbers = [3,1,2]
result = numbers.sort()
print(result)

#output:None
#because .sort() modifies the original list
#if you want a new sorted list
result = sorted(numbers)

#problem 1 -- find largest

def find_largest(nums):
    largest = nums[0]

    for num in nums:
        if num > largest:
            largest = num

    return largest

#example
print(find_largest([4,8,2,10,5]))

#problem 2 -- smallest

def find_smallest(nums):
    smallest = nums[0]

    for num in nums:
        if num < smallest:
            smallest = num
    return smallest

#problem 3 -- count even numbers
def count_even(nums):
    count = 0

    for num in nums:
        if num % 2 == 0:
            count += 1
    return count

#problem 4 -- Reverse a list
def reverse_list(nums):
    return nums[::-1]

#example
print(reverse_list([1,2,3,4])) 

#problem 5 -- find sum
def list_sum(nums):
    total = 0

    for num in nums:
        total += num
    return total

#problem 6 -- Remove duplicates
def remove_duplicated(nums):
    return list(set(nums)) 
#we dont gurantee the orginal order

#problem 7 -- seconf largest 

def secound_largest(nums):
    unique_nums = list(set(nums)) 
    unique_nums.sort()

    return unique_nums[-2]

#example
print(secound_largest([10,5,8,10,3])) 

#problem 8 -- rotate list right by one

def rotate_right(nums):
    if len(nums) <= 1:
        return nums

    last = nums.pop()
    nums.insert(0, last)

    return nums

#example
print(rotate_right([1,2,3,4]))

