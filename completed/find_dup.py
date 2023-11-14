def find_duplicates(nums):
    seen = set()
    duplicates = []

    for num in nums:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)

    return duplicates

numbers = [1, 2, 3, 4, 2 ,7, 8, 1, 8]
result = find_duplicates(numbers)
print(result)