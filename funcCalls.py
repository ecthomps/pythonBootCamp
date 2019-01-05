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

# multiple args --> returns a tuple
def ensure_correct_info(*args):
    if "Chris" in args and "Young" in args:
        return "Welcome back CY"
    return "Not found"
print(ensure_correct_info(1, "yo", True, "Chris", 17, "Young"))

def sum_all_even_num(*args):
    total = 0
    for even in args:
        if even%2 == 0: total+=even
    return total
print(sum_all_even_num(1,2,3,4,5,6))

def contains_purple(*args):
    if "purple" in args: return True
    return False
print(contains_purple(25, "purple"))

# keyword arguments --> returns a dictionary
def special_greeting(**kwargs):
    if "Young" in kwargs and kwargs["Young"] == "Yo!":
        return "You the man Young Chris"
    elif "Young" in kwargs:
        return f"{kwargs['Young']} Young!"
    return "Who is this..."
print(special_greeting(Young="Yo!"))

def combine_words(word, **kwargs):
    if "prefix" in kwargs:
        return kwargs['prefix']+word
    elif "suffix" in kwargs:
        return word+kwargs['suffix']
    return word
print(combine_words("child", prefix="man"))

# tuple/list unpacking 
nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]
def count_sevens(*args):
    return args.count(7)
print(count_sevens(1,4,7))
print(count_sevens(*nums))

#dict unpacking
def calculate(**kwargs):
    message = "The result is"
    oper_lkup = {
        "add": kwargs.get('first', 0) + kwargs.get('second', 0),
        "subtract": kwargs.get('first', 0) - kwargs.get('second', 0),
        "multiply": kwargs.get('first', 0) * kwargs.get('second', 0),
        "divide": kwargs.get('first', 0) / kwargs.get('second', 0)
    }
    isFloat = kwargs.get('make_float', False)
    oper_val = oper_lkup[kwargs.get('operation', '')]
    if isFloat:
        return f"{kwargs.get('message', message)} {float(oper_val)}"
    return f"{kwargs.get('message', message)} {int(oper_val)}"
print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4))
print(calculate(make_float=True, operation='divide', first=3.5, second=5)) # "The result is 0.7"
