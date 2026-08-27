text = "hello"

for char in text:
    if text.index(char) == text.find(char):
        print(char, text.count(char), end="")




text = "hello"
counted = ""

for char in text:
    if char not in counted:
        print(char, text.count(char), end="")
        counted += char
