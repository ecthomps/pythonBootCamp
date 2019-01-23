arr = [2,3,6,1,5,2,1,1,3]

def firstDuplicate(lst):
    l = set()
    for elem in lst:
        if elem in l:
            return elem
        else:
            l.add(elem)
print(firstDuplicate(arr))