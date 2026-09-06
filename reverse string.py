def reverse_string(text):
    characters = list(text)

    left = 0
    right = len(characters) - 1

    while left < right:
        charcters[left], characters[right] = characters[right], characters[left]

        left += 1
        right -= 1

        return ''.join(characters)
