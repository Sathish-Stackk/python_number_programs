from collections import Counter

filename = input("Enter log file name: ")

status_codes = Counter()

with open(filename, "r") as file:
    for line in file:
        parts = line.split()

        if len(parts) >= 9:
            status_code = parts[8]
            status_codes[status_code] += 1

print("\nHTTP Status Code Report")

for code, count in status_codes.items():
    print(code, ":", count)
