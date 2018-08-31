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

#LC with conditional logic
numbers = [1, 2, 3, 4, 5, 6]

evens = [num for num in numbers if num % 2 == 0]
print(f'even numbers:  {evens}')

odd = [num for num in numbers if num % 2 == 1]
print(f'odd numbers: {odd}')

res = [num*2 if num % 2 == 0 else num/2 for num in numbers]
print(f'results: {res}')

with_vowels = "This is so much fun!"
res = ''.join(char for char in with_vowels if char not in "aeiou")
print(res)


#create a list containing first letter of each name
person = ['Ellie', 'Tim', 'Matt']
answer = [char[0] for char in person]
print(answer)

#create a list that is the intersection of two list
l1 = [1,2,3,4]
l2 = [3,4,5,6]

res = [instc for instc in l1 if instc in l2]
print(res)

#create a list with each word reversed and in lower case
answer = [name.lower()[::-1] for name in person]
print(answer)

#create a list with all numbers from 0 - 100 that are divisible by 12
number = range(1, 101)
answer = [num for num in number if num % 12 == 0]
print(answer)

#create a list containing all consonants
word = "amazing"
answer = [char for char in word if char not in "aeiou"]
print(answer)