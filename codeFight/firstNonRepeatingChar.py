s = "abacabad"
NO_OF_CHARS = 256

def getCharCountArr(string):
    count = [0] * NO_OF_CHARS
    for i in string:
        count[ord(i)]+=1
    return count

def firstNonRepeatingChar(string):
    count = getCharCountArr(string)
    index = -1
    k = 0

    for i in string:
        if count[ord(i)] == 1:
            index = k
            break
        k += 1
    if index==1:
        return "_"
    return string[index]
print(firstNonRepeatingChar(s))