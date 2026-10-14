def pair_sum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [numbers[left], numbers[right]]

        if current_sum < target:
            left += 1

        if current_sum > target:
            right -= 1
