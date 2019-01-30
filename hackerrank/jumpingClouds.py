c = [0,0,0,0,1,0]

def printNumOfJumps(lst):
    cur = 0
    end = len(lst)-1
    jumps = 0
    while cur < end:
        if(cur+2 <= end and lst[cur+2]==0):
            cur+=2
            jumps+=1
        elif lst[cur+1]==0:
            cur+=1
            jumps+=1
    return jumps
print(printNumOfJumps(c))