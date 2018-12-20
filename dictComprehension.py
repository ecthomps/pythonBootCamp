instructor = { 
        "name": "colt",
        "city": "san francisco",
        "color": "purple"
    }

print(instructor)

#make key and value uppercase
yelling_instruc = {k.upper():v.upper() for k,v in instructor.items()}
print(yelling_instruc)

yelling_clr_instruc = {(k.upper() if k is 'color' else k):v.upper() for k,v in instructor.items()}
print(yelling_clr_instruc)

number = [1, 2, 3, 4, 5, 6]
res = {num:("even" if num % 2 == 0 else "odd") for num in number}
print(res)

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
# make sure your solution is assigned to the answer variable so the tests can work!
answer = {list1[i]:list2[i] for i in range(0, len(list1))}
print(answer)

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
# use the person variable in your answer
answer = {k:v for k,v in person}
print(answer)
#alternative
# print(dict(person))

answer = {char:0 for char in 'aeiou'}
print(answer)
#alternative
# print(dict.fromkeys('aeiou', 0))

answer = {i:chr(i) for i in range(65, 91)}
print(answer)