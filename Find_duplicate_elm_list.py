numbers = [1, 2, 3, 2, 4, 5, 3]

duplicates = []

for i in numbers:
    if numbers.count(i) > 1 and i not in duplicates:
        duplicates.append(i)

print(duplicates)


Time Complexity : O(n²)
Space Complexity : O(n)
