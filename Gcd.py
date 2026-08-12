# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# x = a
# y = b

# while y != 0:
#     x, y = y, x % y

# gcd = x
# lcm = (a * b) // gcd

# print("GCD =", gcd)
# print("LCM =", lcm)

n=int(input("Enter perfect number :"))

total =0

for i in range(1,n // 2+1):
    if n % i ==0:
        total+=i
if total == n:
    print("Perfect number")
else:
    print("Not a perfect number")