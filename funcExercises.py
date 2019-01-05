def product(num1, num2):
    return num1*num2
print(product(2, 2))

def return_day(num):
    days_of_wk = {"1": "Sunday", "2": "Monday", "3": "Tuesday", "4": "Wednesday", "5": "Thursday", "6": "Friday", "7": "Saturday"}
    return days_of_wk.get(str(num), None)
# alternative
def return_day2(num):
    days = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
    # Check to see if num valid
    if num > 0 and num <= len(days):
        # use num - 1 because lists start at 0 
        return days[num-1]
    return None
print(return_day2(5))

def last_element(myList):
    if len(myList) != 0:
        return myList.pop()
    return None
# alternative
def last_element2(l):
    if l:
        return l[-1]
    return None
print(last_element2([1,2,3]))

def number_compare(first, second):
    if(first > second): return "First is greater"
    elif(second > first): return "Second is greater"
    else: return "Numbers are equal"
print(number_compare(1,2))

def single_letter_count(word, letter):
        return word.lower().count(letter.lower())
print(single_letter_count("Hello World", "l"))

def multiple_letter_count(word):
    return {k:word.count(k) for k in word}
print(multiple_letter_count("awesome"))

def list_manipulation(myList, comm, loc, val=None):
   if(comm == "remove" and loc == "end"): return myList.pop()
   elif(comm == "remove" and loc == "beginning"): return myList.pop(0)
   elif(comm == "add" and loc == "beginning"): 
       myList.insert(0, val)
       return myList
   elif(comm == "add" and loc == "end"):
       myList.append(val) 
       return myList
print(list_manipulation([1,2,3], "remove", "end"))

def is_palindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]
print(is_palindrome("a man a plan a canal panama"))

def frequency(myList, srch_term):
    return myList.count(srch_term)
print(frequency([1,2,3,4,4,4], 4))

def multiply_even_numbers(myList):
    tot = 1
    for x in myList:
      if x % 2 == 0:
          tot *= x
    return tot
print(multiply_even_numbers([2,3,4,5,6]))

def capitalize(word):
    return word.capitalize()
print(capitalize("jamaica"))

def compact(myList):
  return [item for item in myList if item] 
print(compact([0,1,2,"",[], False, {}, None, "All done"])) 

def intersection(list1, list2):
    return [item for item in list1 if item in list2]
    # return [item for item in set(list1) & set(list2)]
    #return list(set(list1) & set(list2))
print(intersection([1,2,3], [2,3,4]))

def isEven(num):
    return num%2 == 0        

def partion(lst, fn):
    return [[even for even in lst if fn(even)], [odd for odd in lst if not fn(odd)]]
print(partion([1,2,3,4,5,6], isEven))