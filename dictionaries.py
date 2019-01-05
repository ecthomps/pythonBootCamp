cat = {"name": "boots",
       "age": 3.5,
       "isCute": True}
print(cat)

#another way to declare a dictionary
cat2 = dict(name = "perry",
            age = 2.5 ,
            isCute = True)
print(cat2)

#retrieving data from a dict
cat['age']

#iterating through a dictionary
instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "fav_lang": "Python",
    "is_hilarious": False,
    44: "my favorite number"
}

for v in instructor.values():
    print(v)
for k in instructor.keys():
    print(k)
for k,v in instructor.items():
    print(f"key is  {k} and value is {v}")

#check if a key is in a dictionary
"name" in instructor #returns true
instructor.get("name") #returns the key value