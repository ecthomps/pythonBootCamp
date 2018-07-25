numbers = [1, 2, 3]

res = [x*10 for x in numbers]
print(res)

name = ['chris']
res = [char.upper() for char in name]
print(res)

friends = ['mary', 'jenny', 'temi']
res = [friend[0].upper() for friend in friends]
print(res)

res = [num*10 for num in range(1,6)]
print(res)

# convert int to str
number = [1,2,3,4,5]
res = [str(num) for num in number]
print(res)
