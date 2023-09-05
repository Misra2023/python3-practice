def remove_duplicates(sequence):
    seen = set()
    result = []
    for item in sequence:
        # If the item hasn't been encountered before, add it to the result and set
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]