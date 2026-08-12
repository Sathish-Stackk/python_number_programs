
n=int(input("Enter perfect number :"))

total =0

for i in range(1,n // 2+1):
    if n % i ==0:
        total+=i
if total == n:
    print("Perfect number")
else:
    print("Not a perfect number")


# Time Complexity = O(n)
# Space Complexity = O(1)
