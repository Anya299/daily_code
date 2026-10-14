def contains_duplicate(numbers):
    seen = set()

    for number in numbers:
        if number in seen:
            return True

        seen.add(number)

    return False
