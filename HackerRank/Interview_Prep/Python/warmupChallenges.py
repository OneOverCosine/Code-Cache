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
     
    val = "a" # as this is the character I'm checking for in this challenge

    if(val not in s):
        return 0 # the character will never show up

    # no. times s fits in n * no. times a appears in s
    count = n//len(s) * s.count(val)

    if(n%len(s) != 0):
        count += s[:n%len(s)].count(val) # no. times a appears in first v chars of string

    return count

def main():
    # this is only setup for problems

    print("running main")

    #c = [0, 1, 0, 0, 0, 1, 0]

    #print("It takes " + str(jumpingOnClouds(c)) + " jumps to get to the end")

    #-------------------------

    s = "acg"
    n = 16

    output = "The number of a's in a string of length {} is {}"

    print(output.format(n, repeatedString(s, n)))

main()