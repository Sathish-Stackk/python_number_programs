# Prime Numbers in a Range
start = 1
end = 20

for num in range(start, end + 1):
    if num > 1:
        count = 0

        for i in range(1, num + 1):
            if num % i == 0:
                count += 1

        if count == 2:
            print(num, end=" ")



# Sum of Even and Odd Numbers in a List
numbers = [1, 2, 3, 4, 5, 6]

even_sum = 0
odd_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print("Even sum:", even_sum)
print("Odd sum:", odd_sum)
