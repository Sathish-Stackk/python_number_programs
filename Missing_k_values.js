//Missing number from 1 to N//
numbers = [1, 2, 3, 5, 6]

n = 6
total = n * (n + 1) // 2

missing = total - sum(numbers)

print("Missing number:", missing)

//Multiple missing numbers//
numbers = [1, 3, 5, 6, 8, 10]

for i in range(1, 11):
    if i not in numbers:
        print(i, "is missing")

//Find missing value K in multiple test cases//
test_cases = [
    [1, 2, 3, 5],
    [2, 3, 4, 6],
    [10, 11, 13, 14]
]

for numbers in test_cases:
    n = len(numbers) + 1
    total = (n * (n + 1)) // 2
    missing = total - sum(numbers)
    print("Missing:", missing)
