s = "aab"
n = 10

def countChar(s, n):
    # cnt = s.count('a')
    # rem = n%len(s)
    # div = n//len(s)
    # cnt = div*cnt

    # for i in range(rem):
    #     cnt += 1
    # return cnt
    return s.count('a') * (n//len(s)) + s[:n%len(s)].count('a')
print(countChar(s,n))
