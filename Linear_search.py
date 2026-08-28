# Linear Search
numbers = [10, 20, 30, 40, 50]
target = 30

found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Element found at index:", i)
        found = True
        break

if not found:
    print("Element not found")
# 6. Sort a List Without sort()
numbers = [5, 2, 8, 1, 3]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print("Sorted list:", numbers)
