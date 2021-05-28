def minPartitions(n):
    
    for i in range(9, 0, -1):
        if str(i) in n:
            return i

n = "32"