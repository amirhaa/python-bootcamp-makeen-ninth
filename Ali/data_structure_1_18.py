# Q1
print('----------------------------------------------------------------\nQ1')

l1 = ['T', 'm', '2', 'k', 'y', 'e', 'L', ':', 'j']
l2 = ['a', 's', 'e', 'H', 'n', 'p', ')', '3']
res = []

i, j = 1, 0
while i <= len(l1) - 1 or j <= len(l2)-1:
    
    print(f'i={i} j={j}')
    
    if not i > len(l1)-1:
        res.append(l1[i])
        i += 2
    if not j > len(l2)-1:
        res.append(l2[j])
        j += 2

print(res)



# Q2
print('----------------------------------------------------------------\nQ2')

lst = [34, 54, 67, 89, 11, 43, 94]

index_4 = lst.pop(4)
lst.insert(-1, index_4)

print(lst)



# Q3
print('----------------------------------------------------------------\nQ3')

lst = [11, 45, 8, 23, 14, 12, 78, 45, 89]

if len(lst) % 3 != 0:
    print('Sorry, you can\'t do this action on this list!')
else:
    i = 0
    res = []
    while i <= len(lst):
        L = []
        L = lst[i:i+3]
        L = L[::-1]
        for num in L:
            res.append(num) 
        i += 3

    print(res)


# Q4
print('----------------------------------------------------------------\nQ4')

lst = [11, 45, 8, 11, 23, 45, 23, 45, 89]

dikt = {}
for num in lst:
    dikt[num] = lst.count(num)

print(dikt)


# Q5
print('----------------------------------------------------------------\nQ5')

def mix(l1, l2):
    return {(l1[i], l2[i]) for i in range(0, len(l1))}

l1 = [2, 3, 4, 5, 6, 7, 8]
l2 = [4, 9, 16, 25, 36, 49, 64]
print(mix(l1, l2))



# Q6
print('----------------------------------------------------------------\nQ6')

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

new_first_set = first_set.copy()

for num in first_set:
    if num in second_set:
        new_first_set.discard(num)

print(f'first_set before : {first_set}')
print(f'first_set after  : {new_first_set}')



# Q7
print('----------------------------------------------------------------\nQ7')

nums = [47, 64, 69, 37, 76, 83, 95, 97]
dikt = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
res = []

for num in nums:
    if num in dikt.values():
        res.append(num)

print(res)



# Q8
print('----------------------------------------------------------------\nQ8')

dikt = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
# res = [val for val in speed.values() if val not in res]           # this doesn't work
res = []
for val in dikt.values():
    if val not in res:
        res.append(val)

print(res)



# Q9
print('----------------------------------------------------------------\nQ9')

lst = [87, 45, 41, 65, 94, 41, 99, 94]
lst = tuple(set(lst))

print(f'min = {min(lst)}\nmax = {max(lst)}')



# Q10
print('----------------------------------------------------------------\nQ10')

from math import floor

str1 = "james"

if len(str1) % 2 == 0:              # string length is and "even" number
    mid_index = floor(len(str1) / 2) - 1
else:
    mid_index = floor(len(str1) / 2)

str2 = str1[0] + str1[mid_index] + str1[-1]

print(str2)



# Q11
print('----------------------------------------------------------------\nQ11')

str1 = 'PyNaTive'

lowers_list = [ch for ch in str1 if ch.islower()]
uppers_list = [ch for ch in str1 if ch.isupper()]

print(''.join(lowers_list + uppers_list))


# Q12
print('----------------------------------------------------------------\nQ12')

str1 = "P@#yn26at^&i5ve"

Chars ,Digits, Symbols = 0, 0, 0

for ch in str1:
    if ch.isalpha():
        Chars += 1
    elif ch.isdigit():
        Digits += 1
    elif ch.isascii():
        Symbols += 1

print(f'Chars: {Chars}\nDigits: {Digits}\nSymbols: {Symbols}')



# Q13
print('----------------------------------------------------------------\nQ13')

str1 = "Welcome to Iran. iran is awesome, isn't it?"
print(f'Iran count is {str1.lower().count("iran")}')



# Q14
print('----------------------------------------------------------------\nQ14')

str1 = "PYnative29@#8496"

digits = [int(ch) for ch in str1 if ch.isdigit()]
print(f'Sum is {sum(digits)} and Average is {sum(digits) / len(digits)}')



# Q15
print('----------------------------------------------------------------\nQ15')

str1 = "Apple"

dikt = {}
for ch in str1:
    dikt[ch] = str1.count(ch)

print(dikt)



# Q16
print('----------------------------------------------------------------\nQ16')

import re
str1 = "/*Jon is @developer & musician"

print(" ".join(re.sub(r'[^\w]', ' ', str1).split()))


# Q17
print('----------------------------------------------------------------\nQ17')

import re
str1 = "Emma25 is Data scientist50 and AI Expert"

res = re.findall(r'(?:\d+[a-zA-Z]+|[a-zA-Z]+\d+)', str1)
print(res)



# Q18
print('----------------------------------------------------------------\nQ18')

from collections import defaultdict

def def_value():
    return "Doesn\n't exist"

str1 = "welcome to makeen python bootcamp!"
     
dikt = defaultdict(def_value)

for ch in str1:
    dikt[ch] = str1.count(ch)

print(dict(dikt))
