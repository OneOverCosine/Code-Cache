''' to sumarise, I want to find out if s1 and s2 share
a common substring. That means as soon as I find 1 (even
if there are multiple) I can return YES '''

import re

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    ''' things to keep in mind...
    strings can be of length 10^5 (100000)
    All I need to do is check that the two strings
    contain one letter that's the same in both
    '''

    #create a dictionary for the first string
    sDict = {}

    # add each letter that occurs in s1 to dictionary
    for char in s1:
        if len(sDict) == 26:
            return 'YES' # I should be able to return 'YES' here since s1 contains every letter of the alphabet at this point
        elif char not in sDict.keys():
            sDict[char] = 1

    # now check if s2 contains the
    for char in s2:
        if char in sDict.keys():
            return 'YES'

    # if we get to this point, s1 and s2 have no substring in common
    return 'NO'

def main():

    s1 = 'abcdefghijklmnopqrstuvw'
    s2 = 'xzya'

    print(twoStrings(s1, s2))

main()