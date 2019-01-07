def maxChar(string):
    maxVal, maxChar = 0, ''
    for char in set(string):
        count = string.count(char)
        if count > maxVal:
            maxVal = count
            maxChar = char
    return maxChar
# alternative
# return max(string, key=string.count) 
print(maxChar("Hello There!"))        

# bonus
def isCharFound(string, item):
    if item in set(string): return True
    return False
print(isCharFound("Hey There", 'a'))