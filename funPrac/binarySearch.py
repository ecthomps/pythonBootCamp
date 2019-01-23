lst = [3,7,8,9,11,13,17,25,27,28,30]

def binary_search(lst, item):
    first = 0
    last = len(lst)-1
    found = False
    midpoint = 0

    while(first < last and not found):
        midpoint = int((first + last) / 2)
        if(lst[midpoint] > item):
            last = midpoint - 1
        elif(lst[midpoint] < item):
            first = midpoint + 1
        else:
            found = True
    
    if found:
        return f"Item found...\nIndex position is {midpoint}"
    return 0

print(binary_search(lst, 17))

