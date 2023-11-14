def distinct(seq):
    result = []
    seen = set()  # Set to keep track of seen elements

    for item in seq:
        if item not in seen:
            result.append(item)
            seen.add(item)  # Add the element to the set

    return result

# Example usage
seq = [1, 1, 2, 3, 4, 4, 4, 5]
distinct_seq = distinct(seq)
print(distinct_seq)
