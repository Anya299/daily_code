# 🚀 DAY 7 - PYTHON COLLECTIONS, FUNCTIONS & PROBLEM SOLVING


# ============================================================
# PART 1 — LOOP THROUGH A LIST
# ============================================================

numbers = [10, 20, 30, 40, 50]

for num in numbers:
    print(num)


# ============================================================
# LOOP + CONDITION
# ============================================================

numbers = [10, 20, 30, 40, 50]

for num in numbers:
    if num > 25:
        print(num)


# ============================================================
# PART 2 — DICTIONARY TRAVERSAL
# ============================================================

student = {
    "name": "Ananya",
    "age": 20,
    "cgpa": 9.0
}


# Keys
for key in student:
    print(key)


# Values
for value in student.values():
    print(value)


# Key + Value
for key, value in student.items():
    print(key, value)


# ============================================================
# PART 3 — SET + LOOP
# ============================================================

numbers = {1, 2, 3, 4, 5}

for num in numbers:
    print(num)


# A set is mainly used for:
# - unique values
# - fast membership checking
# - duplicate detection


# ============================================================
# PART 4 — FREQUENCY PATTERN
# ============================================================

nums = [2, 3, 2, 5, 3, 2, 7, 5]

frequency = {}

for num in nums:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print(frequency)


# Pattern:
# First time we see a number → store 1
# If we see it again → increase the count


# ============================================================
# PART 5 — FUNCTIONS
# ============================================================

def add(a, b):
    return a + b


result = add(10, 20)
print(result)


# ============================================================
# RETURN
# ============================================================

def square(n):
    return n * n


answer = square(25)
print(answer)


# ============================================================
# FUNCTION + LOOP
# ============================================================

def count_even(numbers):
    count = 0

    for num in numbers:
        if num % 2 == 0:
            count += 1

    return count


nums = [1, 2, 4, 7, 8]

answer = count_even(nums)

print(answer)


# ============================================================
# PROBLEM 1 — COUNT NUMBERS GREATER THAN 10
# ============================================================

def count_greater_than_10(nums):
    count = 0

    for num in nums:
        if num > 10:
            count += 1

    return count


nums = [5, 12, 8, 20, 15, 3]

print("Numbers greater than 10:",
      count_greater_than_10(nums))


# ============================================================
# PROBLEM 2 — FIND THE LARGEST NUMBER
# ============================================================

def find_largest(nums):
    largest = nums[0]

    for num in nums:
        if num > largest:
            largest = num

    return largest


nums = [4, 9, 2, 15, 6]

print("Largest number:", find_largest(nums))


# ============================================================
# PROBLEM 3 — COUNT FREQUENCY
# ============================================================

def frequency_count(nums):
    frequency = {}

    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    return frequency


nums = [1, 2, 2, 3, 1, 2, 4]

print("Frequency:", frequency_count(nums))


# ============================================================
# DAY 7 SUMMARY
# ============================================================

# Learned:
#
# 1. List traversal
# 2. Loop + condition
# 3. Dictionary traversal
# 4. Set traversal
# 5. Frequency counting
# 6. Functions
# 7. return
# 8. Running maximum / largest element
# 9. Dictionary-based frequency counting
#
# DSA patterns:
#
# Hash Map      → fast lookup / Two Sum
# Hash Set      → duplicates / unique values
# Frequency Map → counting occurrences
