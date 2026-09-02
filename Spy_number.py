num = int(input("Enter a number: "))

original = num
digit_sum = 0
product = 1

while num > 0:
    digit = num % 10
    digit_sum += digit
    product *= digit
    num //= 10

if digit_sum == product:
    print(original, "is a Spy Number")
else:
    print(original, "is not a Spy Number")
