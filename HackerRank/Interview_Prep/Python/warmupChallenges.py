def jumpingOnClouds(c):

    # always want to jump 2, but can't if target cloud is a thunderhead
    # so jump 2 if possible, otherwise jump 1
    jumps = 0
    i = 0
    
    while(i < len(c)):
        
        if((i + 2) <= len(c) - 1 and c[i+2] != 1):
            i += 2
        else:
            if(i == len(c) - 1):
                return jumps
            
            i += 1
        
        jumps += 1

    return jumps

def repeatedString(s, n):
    # 

    nString = s * (n//len(s)) + s[0:n%len(s)] # the first n characters to work with

    val = "a" # as this is the character I'm checking for in this challenge

    print(nString) # test

    return -1

def main():
    # this is only setup for problems

    print("running main")

    c = [0, 1, 0, 0, 0, 1, 0]

    print("It takes " + str(jumpingOnClouds(c)) + " jumps to get to the end")

    #-------------------------

    s = "abcac"
    n = 16

    repeatedString(s, n)

main()