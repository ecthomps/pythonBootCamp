def chunk(lst, size):
    return [lst[i:i + size] for i in range(0, len(lst), size)]
print(chunk([1,2,3,4,5], 2))