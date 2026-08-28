LCM of Two Numbers
a = 12
b = 18

for i in range(max(a, b), a * b + 1):
    if i % a == 0 and i % b == 0:
        print("LCM:", i)
        break



Decimal to Binary
num = 10
binary = ""

while num > 0:
    binary = str(num % 2) + binary
    num //= 2

print("Binary:", binary)
