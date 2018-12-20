import random

def flipCoin():
    face = ["Head", "Tail"]
    return random.choice([item.upper() for item in face])

print(flipCoin())

def generate_evens():
    print([even for even in range(1, 50) if even % 2 == 0])
generate_evens()

def sumOddNumbers(numbers):
    total = [num for num in numbers if num % 2 == 1]
    return sum(total)

print(sumOddNumbers([1,2,3,4,5,6,7]))

#default parameter
def speak(animal='dog'):
    noises = {'pig':'oink', 'duck':'quack', 'cat':'meow', 'dog':'woof'}
    return noises.get(animal, '?')

print(speak('yo'))