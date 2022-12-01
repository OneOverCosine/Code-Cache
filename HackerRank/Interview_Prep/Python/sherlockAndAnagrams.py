from collections import Counter

def find_anagrams(s):
    # now try it using a dictionary

    return "[placeholder]"

def my_find_anagrams(s):
    # using Counter(string) to check for anagrams
    # 1. traverse all possible substrings
    # 2. check if any strings of equal length are anagrams

    count = 0
    window = 1

    for i in range(len(s)):
        temp = []
        
        for j in range(len(s) - window + 1):
            current = s[j:j+window]
            if len(temp) < 1:
                temp.append(current)
                continue

            for value in temp:
                if Counter(current) == Counter(value):
                    print(f"{current} and {value} are anagrams of eachother")
                    count += 1

            temp.append(current) # after comparing all the values I can add the newest one

        window += 1
    
    return count


if __name__ == "__main__":
    
    s = "ifailuhkqq"

    print(f"There are {my_find_anagrams(s)} anagrams in the string {s}")