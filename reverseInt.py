def reverseInt(num):
    if num < 0: 
        strNum = str(abs(num))
        return int(strNum[::-1]) * -1
    return int(num[::-1])
print(reverseInt(-15))