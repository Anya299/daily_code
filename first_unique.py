def first_unique(text):
    frequency = {}

    # Step 1: count
    for character in text:
        frequency[character] = frequency.get(character, 0) + 1

    # Step 2: find first character appearing once
    for character in text:
        if frequency[character] == 1:
            return character

    return None
