import re

def halvesAreAlike(s):
        vowels = "[aeiou]"
        a = s[0:len(s)//2].lower()
        b = s[len(s)//2:len(s)].lower()

        return len(re.findall(vowels, a)) == len(re.findall(vowels, b))

s = "hwllow"
print(halvesAreAlike(s))