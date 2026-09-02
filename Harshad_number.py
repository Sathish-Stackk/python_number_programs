num = int(input("Enter a number: "))

digit_sum = sum(int(digit) for digit in str(num))

if num % digit_sum == 0:
    print(num, "is a Harshad Number")
else:
    print(num, "is not a Harshad Number")
