# Q1:

listA = [0, 1, 2, 3, 4]
listB = [5, 6, 7, 8, 9]

def create_list(listA, listB):
    res = []
    for index, i in enumerate(listA):
        if index % 2 != 0:
            res.append(i)
    for index, j in enumerate(listB):
        if index % 2 == 0:
            res.append(j)

    return res

print(create_list(listA, listB))

# --------------------------------------

# Q2:

lst = [34, 54, 67, 89, 11, 43, 94]

def remove_item(lst):
    item = lst.pop(4)
    lst.insert(2, item)
    lst.append(item)
    return lst

print(remove_item(lst))

# ------------------------------------

# Q3:

main_list =[11, 45, 8, 23, 14, 12, 78, 45, 89]

def change_list(lst):
    res = []
    for i in range(0, len(lst), 3):
        item = lst[i:i + 3]
        item.reverse()
        res.extend(item)
    return res

print(change_list(main_list))

# -------------------------------------

# Q4:

lst = [11, 45, 8, 11, 23, 45, 23, 45, 89]

def count_item(lst):
    dict = {}
    for item in lst:
        if item not in dict.keys():
            count = lst.count(item)
            dict[item] = count
    return dict

print(count_item(lst))

# ------------------------------------

# Q5:

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

def merge(list1, list2):
    return {(list1[i], list2[i]) for i in range(0, len(list1))}

print(merge(first_list, second_list))

# -------------------------------------

# Q6:

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

def intersection_remove(setA, setB):
    intersection = [i for i in setA if i in setB]
    setA.difference_update(intersection)
    return setA

print(intersection_remove(first_set, second_set))

# --------------------------------------

# Q7:

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

for number in roll_number:
    if number not in sample_dict.values():
        roll_number.remove(number)

print(roll_number)

# ----------------------------------------

# Q8:

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

res = []
for item in speed.values():
    if item not in res:
        res.append(item)

print(res)

# ----------------------------------------

# Q9:

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

unique_items = tuple([item for item in sample_list if sample_list.count(item) == 1])
print(f"Min: {min(unique_items)}\nMax: {max(unique_items)}")

# -----------------------------------------

# Q10:

def change_string(string):
    return string[0]+string[len(string) // 2]+string[-1]

print(change_string("James"))

# ------------------------------------------

# Q11:

def lower_upper_string(string):
    lower = ""
    upper = ""
    for ch in string:
        if ch == ch.lower():
            lower += ch
        else:
            upper += ch
    return lower+upper

print(lower_upper_string("PyNaTive"))

# -------------------------------------------

# Q12:

def characters(string):
    chars = 0
    digits = 0
    symbols = 0

    for ch in string:
        if ch.isdigit():
            digits += 1
        elif ch.isalpha():
            chars += 1
        else:
            symbols += 1
    return f"chars: {chars}\ndigits: {digits}\nsymbols: {symbols}"

print(characters("P@#yn26at^&i5ve"))

# ------------------------------------------

# Q13:

str1 = "Welcome to Iran. iran awesome, isn't it?"

string = list(map(lambda x: x.strip(",.?!"), str1.lower().split()))
dict = {}
for word in string:
    if string.count(word) > 1 and word not in dict.keys():
        dict[word] = string.count(word)
for key, value in dict.items():
    print(f"{key}: {value}")

# --------------------------------------------

# Q14:

def calculate(string):
    sum = 0
    count = 0
    for ch in string:
        if ch.isdigit():
            count += 1
            sum += int(ch)
    return f"sum is: {sum} and average is {sum / count}"

print(calculate("PYnative29@#8496"))

# --------------------------------------------

# Q15:

def count_ch(string):
    dict = {}
    for ch in string.lower():
        if ch not in dict.keys():
            dict[ch] = string.lower().count(ch)
    return dict

print(count_ch("Apple"))

# ----------------------------------------------

# Q16:

import re

str1 = "/*Jon is @developer & musician"

print(" ".join(re.sub(r'[^\w]', ' ', str1).split()))

# -----------------------------------------------

# Q17:

str1 = "Emma25 is Data scientist50 and AI Expert"

for word in str1.split():
    if word.isalnum():
        if word.isalpha() or word.isdigit():
            pass
        else:
            print(word)

# ----------------------------------------------

# Q18:

from collections import defaultdict

string = 'This is a example for defaultdict'
chars = defaultdict(int)

for char in string.lower():
    if char != " ":
        chars[char] += 1
    
for key, value in chars.items():
    print(f"{key}: {value}")

        




