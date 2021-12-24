# Q11:

def count_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for item in string:
        if item in vowels:
            count += 1
    return count

# If we want to return the number of vowels in the given list instead of string.
def count_vowels_list(listA):
    count = 0
    for item in listA:
        count += count_vowels(item)
    return count

# -------------------------------------------------------

# Q12:

def combine_dict(dictA, dictB):
    newDict = {}
    for keyA, valueA in dictA.items():
        if keyA in dictB.keys():
            newDict[keyA] = valueA + dictB[keyA]
    dictA.update(newDict)
    dictB.update(dictA)
    return dictB

# --------------------------------------------------------

# Q13:

def unique_items(list1, list2):
    result = []
    for i in list1:
        if i not in list2 and i not in result:
            result.append(i)
    return result

# --------------------------------------------------------

# Q14:

def update_dict(myDict, myTuple):
    myDict[myTuple[0]] = myTuple[1]
    return myDict

# ---------------------------------------------------------

# Q15:

def mean(my_dict):
    sum = 0
    for value in my_dict.values():
        sum += value
    return sum / len(my_dict)

# ---------------------------------------------------------

# Q16:

def generate_dicts(n):
    return {item: item**2 for item in range(1, n+1)}

# ---------------------------------------------------------

# Q17:

name = input("What is your name? :)")
print(f"Hello dear {name}, you are very welcomed.")

# --------------------------------------------------------

# Q18:

user_age = int(input("How old are you?"))

if user_age >= 18:
    print("You are allowed to have a driving licence.\nHave fun!")
else:
    print("Your age is bellow 18 so you are not allowed to have driving licence.")
    










