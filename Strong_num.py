n = int(input("Enter a number: "))

temp = n
total = 0

while temp > 0:
    digit = temp % 10

    factorial = 1

    for i in range(1, digit + 1):
        factorial *= i

    total += factorial
    temp //= 10

if total == n:
    print("Strong Number")
else:
    print("Not a Strong Number")


# Final time complexity = O(d)
# Space complexity = O(1)
