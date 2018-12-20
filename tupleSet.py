#tuples are commonly used for UNCHANGING data:
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
for month in months:
    print(month)

#tuples can be used as keys in dictionaries
locations = {
    (35.6895, 39.6917): "Tokyo Office",
    (40.7128, 74.0060): "New York Office",
    (37.7749, 122.4194): "San Francisco Office",
}
print(locations[(37.7749, 122.4194)])

cat = {"name": "biscuit", "age": 0.5, "favorite_toy": "my chapstick"}
print(cat.items())

x = (1, 2, 3, 3, 3)
print(x.count(3))

#sets
s = {1, 'a', 4, 5, 'b', 23.3334}
for thing in s:
    print(thing)

#generate all set of students without any duplicate
math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
biology_students = {"Jane", "Matthew", "Charlotte", "Mesut", "Oliver", "James"}
print(math_students | biology_students) #use the | for union
print(math_students & biology_students) #students that are in both classes

#set comprehension
res = {x**2 for x in range(10)}
print(res)
res = {char.upper() for char in 'hello'}
print(res)
#check if word contains all the 5 vowel
string = 'sequoia'
res = len({char for char in string if char in 'aeiou'}) == 5
print(res)