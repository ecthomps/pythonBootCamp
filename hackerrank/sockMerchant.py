arr = [10,20,20,10,10,30,50,10,20]

def printNumOfPairs(lst):
    count = 0
    k = set(lst) 
    for i in k:
        if lst.count(i)//2>=1:
            count += (lst.count(i)//2)
    return count
print(printNumOfPairs(arr))