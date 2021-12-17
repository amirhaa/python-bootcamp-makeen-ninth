# 1
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l3 = list()

odd_number = l1[1::2]
print('is odd number from list one')
print(odd_number)

even_number = l2[0::2]
print('is even number from list two')
print(even_number)

l1.extend(odd_number)
l2.extend(even_number)
print(l3)

print('---------------------------------------')
# 2
lst = [2, 1, 3, 5, 4, 3, 8]

del lst[2 : 5]

print('list elements after deleting are :' ,end = " ")
for i in range(0, len(lst)):
    print(lst[i], end = " ")

print('---------------------------------------')
# 3
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

n = 4

final = [my_list[i * n:(i+1) * n]for i in range((len(my_list) + n - 1)//n)]
print(final)

print('------------------------------------------')
# 4
def countX(lst, x):
    count = 0
    for num in lst:
        if num == x:
            count += 1
    return count

lst = [8, 6, 10, 8, 20, 8, 4, 8]

x = 8

# print()

print('---------------------------------------------------')
# 5
l1 = [10, 20, 30, 40]
l2 = [40, 50, 60]

output = [{a, b} for a in l1 
           for b in l2 if a != b]

print(output)

print('---------------------------------------------------')
# 6
# sn1 = [1, 2, 3, 4, 5]
# sn2 = [4, 5, 6, 7, 8]

# for num in sn1,sn2:
#     sn1.remove(num)
#     sn2.remove(num)
    
# print('sn1:' , sn1)
# print('sn2:' , sn2)

print('--------------------------------------------------')
# 7
# roll_number = [47, 64, 69, 37, 76, 97, 45]
# sample_dict = {'mack': 47, 'mobin':69 , 'dnya': 76 , 'atin' : 97}

# for item in roll_number:
#     if not item in sample_dict.values():
#         roll_number.remove(item)

# print(roll_number)

print('--------------------------------------------------')
# 8

lst = [{'mobin' : 1}, {'mack' : 2}, {'atin': 3}, {'mobin' : 4}, {'mack': 5}, {'mobin', 6}]

print('orginal list : ' + str (lst))

res_list = []

for i in range(len(lst)):
    if lst [i] not in lst[i + 1:]:
        res_list.append(lst[i])

print('resultant list is : ' + str(res_list))

print('--------------------------------------------------')
# 9
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print('the orginal list is : ' + str(test_list))

res = []
for i in lst:
    if i not in res:
        res.append(i)

print('the list after removing duplicates: ' + str(res))

print(max(test_list))
print(min(test_list))

print('--------------------------------------------------')
# 10

str_1 = 'masih'
print('orginal string is :', str_1)

res = str_1[0]

l = len(str_1)

middle = int(l /2)

res += str_1[middle]

res += str_1[l - 1]
print('new string: ', res)

print('--------------------------------------------------')
# 11
str_1 = 'MAsIhmaCK'
print('orginal string: , str_1')

less = []
top = []

for char in str_1:
    if char.islower():
        less.append(char)
    else:
        top.append(char)

sorted_str = ''.join(less + top)
print('result' , sorted_str)

print('--------------------------------------------------')
# 12

string = 'gabrymobin'

alphabets = digits = special = 0

for i in range(len(string)):
    if string[i].isalpha():
        alphabets += 1

print('total number of alphabets in this string: ', alphabets)

print('--------------------------------------------------')
# 13
string_1 = 'welcome to iran'
sub_string= 'iran'

temp_str = string_1.lower()

count = temp_str.count(sub_string.lower())
print('the iran count is: ', count)

print('--------------------------------------------------')
# 14
def find_sum(str):
    sum = 0
    count = 0
    for ch in str:
        if ch.isdigit():
            sum +=int(ch)
            count += 1
    return sum / count

given_str= input('enter a string : ')
print(find_sum(given_str))

print('--------------------------------------------------')
# 15
str1 = 'apple'

char_dict = dict()

for char in str1:
    count = str1.count(char)
    char_dict[char] = count

print('result: ', char_dict)

print('--------------------------------------------------')
# 16
str = '''!()-[]{};:'\,<>&*#$%!'''

my_str = 'hello !!!, he said ---and went.'

no_punct = ' '
for char in my_str:
    if char not in str:
        no_punct += char
print(no_punct)

print('--------------------------------------------------')
# 17
str_1 = 'mack30 is data scientist60 and AI expert '
print('the orginal string is: ' + str_1)

res = []
temp = str_1.split()

for item in temp: 
    if any (char.isalpha( ) for char in item )and any (char.isdigit() for char in item):
        res.append(item)

print('displaing words with alphabets and numbers')
for i in res :
    print(i)