# write a lambda that accepts and cube a single num
cube = lambda num: num**3
print(cube(2))

# square each num in a list
nums = [2, 4, 6, 8, 10]
def square(lst):
    return list(map(lambda num: num**2, lst))
print(square(nums))

# capitalize each letter in list
people = ["Darcy", "Christina", "Dana", "Annabel"]
def capitalizeAll(lst):
    return list(map(lambda name: name.upper(), lst))
print(capitalizeAll(people))

# show first names
names = [
    {"first": "Chris", "last": "Young"},
    {"first": "Colt", "last": "Steele"},
    {"first": "Mary", "last": "Bessman"}
]
def showFirstNames(lst):
    return  list(map(lambda fname: fname['first'], lst))
print(showFirstNames(names))

# decrement list
def decrement_list(lst):
    return list(map(lambda num: num-1, lst))
print(decrement_list([20,14,11])) 

# less than zero
number_list = range(-5,5)
def less_than_zero(lst):
    return list(filter(lambda num: num < 0, lst))
print(less_than_zero(number_list))

# new namelist
names = ["austin", "penny", "anthony", "angel", "billy"]
def new_name_list(lst):
    return list(filter(lambda name: name[0] == 'a', lst))
print(new_name_list(names))

# tweet
users = [
    {"username": "samuel", "tweets": ["I love cake", "I love pie"]},
    {"username": "katie", "tweets": ["I love cat"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo_lur", "tweets": ["dogs are the best"]},
    {"username": "guitar_gal", "tweets": []}
]
def inactive_users(lst):
    return list(map(lambda name: name['username'],
                    filter(lambda user: not user['tweets'], lst)))
    # return [names['username'] for names in lst if not names['tweets']]
print(inactive_users(users))

# instructor name
names = ["Lassie", "Colt", "Rusty"]
def instr_name(lst):
    return list(map(lambda name: f"Your instructor is {name}", 
                    filter(lambda name: len(name) < 5, lst)))
print(instr_name(names))     

def is_all_strings(lst):
    return all([type(string) is str for string in lst])
print(is_all_strings(['a', 'b', 'c']))

def sort_users(lst):
    return sorted(lst, key=lambda user: len(user['tweets']), reverse=True)
print(sort_users(users))

names = ["Arya", "Samson", "Dora", "Tim", "Ollivander"]
def min_str_len(lst):
    return min(names, key=lambda name: len(name))
print(min_str_len(names))

def extremes(lst):
    return (min(lst), max(lst))
print(extremes((99.25,30,-7)))

def sum_even_values(*args):
   return sum(filter(lambda num: num%2==0, args))
print(sum_even_values(1,2,3,4,5,6))

# zip
def print_grades():
    midterms = [80,91,78]
    finals = [98,89,53]
    students = ['dan', 'ang', 'kate']
    # return {t[0]:max(t[1], t[2]) for t in (zip(students, midterms, finals))}
    return dict(zip(students, map(lambda res: max(res), zip(midterms, finals))))
print(print_grades())

def interleave(str1, str2):
    return "".join(["".join(word) for word in zip(str1, str2)])
print(interleave("aaa", "zzz"))

def triple_and_filter(lst):
    return list(map(lambda n: n*3, filter(lambda num: num%4==0, lst)))
    # return [num*3 for num in lst if num%4==0]
print(triple_and_filter([6,8,10,12]))

def extract_full_name(lst):
    # return [f"{name['first']} {name['last']}" for name in lst]
    return list(map(lambda name: f"{name['first']} {name['last']}", lst))
print(extract_full_name([{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]))