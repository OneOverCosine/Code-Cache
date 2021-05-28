# w.i.p.
def getSmallestString(n, k):
    letters = "abcdefghijklmnopqrstuvwxyz"    
    result = ""

def basicGetSmallestString(n, k):
    letters = "abcdefghijklmnopqrstuvwxyz"    
    result = ""

    for i in range(25, -1, -1):
        if i + 1 > k:
            continue

        k -= i
        result += letters[i]

    return result[::-1]

n = 5 # no. of characters
k = 73 # numeric value of string

print(getSmallestString(n, k))