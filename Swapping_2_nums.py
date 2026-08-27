//Using a temporary variable//
a = 10
b = 20

temp = a
a = b
b = temp

print("a =", a)
print("b =", b)


//Without a temporary variable//
a = 10
b = 20

a = a + b
b = a - b
a = a - b

print("a =", a)
print("b =", b)


//Using Python's tuple swapping//
a = 10
b = 20

a, b = b, a

print("a =", a)
print("b =", b)


//Using multiplication and division//
a = 10
b = 20

a = a * b
b = a // b
a = a // b

print("a =", a)
print("b =", b)



