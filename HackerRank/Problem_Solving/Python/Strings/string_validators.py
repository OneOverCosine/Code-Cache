# working with string validators

s = "w0rD"

# print(s.isalnum())
# print(s.isalpha())
# print(s.isnumeric())
# print(s.islower())
# print(s.isupper())

for i in range(len(s)):
    if s[i].isalnum():
        print(True)
        break
    elif s[i].isalnum() == False and i == len(s) - 1:
        print(False)

for i in range(len(s)):
    if s[i].isalpha():
        print(True)
        break
    elif s[i].isalpha() == False and i == len(s) - 1:
        print(False)

for i in range(len(s)):
    if s[i].isnumeric():
        print(True)
        break
    elif s[i].isnumeric() == False and i == len(s) - 1:
        print(False)

for i in range(len(s)):
    if s[i].islower():
        print(True)
        break
    elif s[i].islower() == False and i == len(s) - 1:
        print(False)

for i in range(len(s)):
    if s[i].isupper():
        print(True)
        break
    elif s[i].isupper() == False and i == len(s) - 1:
        print(False)