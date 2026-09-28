# Day 10 - Array Searching and Optimization Patterns

# --------------------------------------------------
# 1. Find First Even
# --------------------------------------------------

def find_first_even(nums):
    for i, num in enumerate(nums):
        if num % 2 == 0:
            return i
    return -1


# --------------------------------------------------
# 2. Count Numbers Greater Than Target
# --------------------------------------------------

def count_greater(nums, target):
    count = 0

    for num in nums:
        if num > target:
            count += 1

    return count


# --------------------------------------------------
# 3. Pair Sum - Brute Force
# --------------------------------------------------

def has_pair_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return True

    return False


# --------------------------------------------------
# 4. Pair Sum - Two Pointers
#    Works when the array is SORTED
# --------------------------------------------------

def has_pair_sum_sorted(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return True

        elif current_sum < target:
            left += 1

        else:
            right -= 1

    return False


# --------------------------------------------------
# 5. Prefix Sum
# --------------------------------------------------

def prefix_sum(nums):
    result = []
    total = 0

    for num in nums:
        total += num
        result.append(total)

    return result


# --------------------------------------------------
# 6. Frequency Counting
# --------------------------------------------------

def frequency_count(nums):
    frequency = {}

    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

    return frequency


# --------------------------------------------------
# TESTING
# --------------------------------------------------

numbers = [3, 7, 2, 8, 5, 10]

print("Numbers:", numbers)

print("First even index:", find_first_even(numbers))

print("Numbers greater than 5:", count_greater(numbers, 5))

print("Has pair sum 10:", has_pair_sum(numbers, 10))

sorted_numbers = [1, 2, 3, 4, 6, 8]

print("Sorted numbers:", sorted_numbers)
print("Has pair sum 10:", has_pair_sum_sorted(sorted_numbers, 10))

print("Prefix sum:", prefix_sum(numbers))

print("Frequency:", frequency_count(numbers))
