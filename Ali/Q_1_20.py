# Q1
print("------------------------------------------------------------------\nQ1")

# method_1
def reverse_list(lst):
    return list(reversed(lst))

lst1 = [1, 45, 27, 500, -2, 100, 912]
print(reverse_list(lst1))
    
# method_2 (more detailed)    
def reverse_list(lst):
    res = []
    i = len(lst) - 1
    while i>=0:
        res.append(lst[i])
        i -= 1
    return res

lst1 = [1, 45, 27, 500, -2, 100, 912]
print(reverse_list(lst1))


# Q2
print("------------------------------------------------------------------\nQ2")

def get_2_highests(nums):
    if len(set(nums)) < 2:
        return nums
    else:
        new = sorted(set(nums))[::-1]
        return new[0], new[1]

lst1 = [1, 45, 27,912, 500, -2, 100, 912, 912]
print(get_2_highests(lst1))


# Q3
print("------------------------------------------------------------------\nQ3")

def invert(lst):
    # res = [num-num*2 if num>=0 else num+num*2 for num in lst]
    res = []
    for num in lst:
        res.append(num * (-1))
    
    return res

lst1 = [1, 45, -27, 500, 0, -2, 100, 912]
print(invert(lst1))


# Q4
print("------------------------------------------------------------------\nQ4")

def Slice(num):
    num = str(num)
    res = [ch for ch in num]
    return res

num1 = 145556
print(Slice(num1))


# Q5
print("------------------------------------------------------------------\nQ5")

def filter_list(lst):
    res = [ch for ch in lst if type(ch) == int]
    return res

lst1 = ['s', 45, -27, 'hello', 0, 'ali', 100, 912]
print(filter_list(lst1))


# Q6
print("------------------------------------------------------------------\nQ6")

# method_1
def odd_or_even_sum(lst):
    if not lst:
        return 'even'
    if sum(lst) % 2 == 0:
        return 'even'
    else:
        return 'odd'


lst1 = [1, 45, 27, 500, -2, 100, 912]
print(odd_or_even_sum(lst1))
    

# Q7
print("------------------------------------------------------------------\nQ7")

def sort_strings(strings):
    return sorted(strings, key=len, reverse=True)

lst1 = ["Java", "Python", "Go", "Js"]
print(sort_strings(lst1))


# Q8
print("------------------------------------------------------------------\nQ8")

def flattened_list(lst):
    res = []
    for nums in lst:
        res.extend(nums)
    return sorted(res)
    # res = []
    # for nums in lst:
    #     for num in nums:
    #         res.append(num)

    # return sorted(res)

lst1 = [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]
print(flattened_list(lst1))


# Q9
print("------------------------------------------------------------------\nQ9")

def bellow_the_limit(nums, limit):
    for num in nums:
        if num > limit:
            return False
    return True

lst1 = [4, 7, 10, 20, 18]
limit = 20
print(bellow_the_limit(lst1, limit))


# Q10
print("------------------------------------------------------------------\nQ10")

def descending_numbers(num):
    # reverse_sorted_list = sorted(str(num), reverse=True)
    # return ''.join(reverse_sorted_list)
    return ''.join(sorted(str(num), reverse=True))

number = 1452635
print(descending_numbers(number))


# Q11
print("------------------------------------------------------------------\nQ11")

def count_vowels(string1):
    vowels = ['a', 'e', 'i', 'o', 'u']
    v_count = 0
    for ch in string1:
        if ch in vowels:
            v_count += 1
    return v_count

string1 = 'airplane'
print(f'"{string1}" has {count_vowels(string1)} vowels')


# Q12
print("------------------------------------------------------------------\nQ12")

def combine_dict(d1, d2):
    d1.update(d2)
    return d1

dictA = {'a': 10, 'b': 20, 'c': 30}
dictB = {'a': 3, 'c': 6, 'd': 3}
print(combine_dict(dictA, dictB))


# Q13
print("------------------------------------------------------------------\nQ13")

def unique_items(lst1, lst2):
    res = []
    for num in set(lst1):
        if num not in lst2:
            res.append(num)
    return res

list1 = [1, 2, 3, 3, 4]
list2 = [1, 4, 5]
print(unique_items(list1, list2))


# Q14
print("------------------------------------------------------------------\nQ14")

def update_dict(d, t):
    d.update({t[0]:t[1]})
    return d

person = {"name": "Andy"}
print(update_dict(person, ('age', 20)))


# Q15
print("------------------------------------------------------------------\nQ15")

def minn(dictt):
    return min(dictt.values())

scores = {"Mathematics": 18, "History": 16, "Physics": 20}
print(minn(scores))


# Q16
print("------------------------------------------------------------------\nQ16")

def generate_dict(n):
    myDict = {x: x*x for x in range(1, n+1)}
    return myDict

print(generate_dict(5))


# Q17
print("------------------------------------------------------------------\nQ17")

def greet(name):
    return f'Hello dear {name}, you are very welcomed.'

# name = input('Enter your name : ')
# print(greet(name))
print(greet('Ali'))


# Q18
print("------------------------------------------------------------------\nQ18")

def isAllowed(age):
    if age < 18:
        print('You are not allowed to have driving licence!')
    else:
        print('You are able to get a driving licence.')

# age = int(input('How old are you ? '))
# print(isAllowed(age))
print(isAllowed(21))


# Q19
print("------------------------------------------------------------------\nQ19")

def create_phone_number(nums):
    string_nums = [str(x) for x in nums]
    part_1 = ''.join(string_nums[:3:])
    part_2 = ''.join(string_nums[3:6:])
    part_3 = ''.join(string_nums[6:10:])
    return f'({part_1}) {part_2}-{part_3}'

st = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(create_phone_number(st))



# Q20
print("------------------------------------------------------------------\nQ20")

from random import randint

x  = randint(1,11)
guesses_left = 4

guess = int(input('Can you guess the number ? '))
while guesses_left != 0:
    if guess == x:
        print('\U00002705 Congratulations, you have won!')
        break
    else:
        guesses_left -= 1
        if guesses_left:
            print(f'\U0000274c wrong answer, you have {guesses_left} guess(es) left')
            guess = int(input('Can you guess the number ? '))
        else:
            print(f'Sorry you lost, the correct answer is {x}')


d1 = {'name': 'Ali', 'city':'tehran', 'location':'makeen'}

