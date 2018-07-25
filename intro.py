# create a list
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# count an item occurence
print(fruits.count('apple'))
print(fruits.count('tangerine'))

print(fruits.index('banana'))
# 3
print(fruits.index('banana', 4))  # Find next banana starting a position 4
# 6
fruits.reverse()
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
fruits.append('grape')
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
fruits.sort()
# ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
print(fruits.pop())
# 'pear'
