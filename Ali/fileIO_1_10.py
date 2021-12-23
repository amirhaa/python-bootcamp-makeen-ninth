from datetime import datetime, timedelta
from time import time


# Q1
print('----------------------------------------------------------------\nQ1')

lst1 = ['python', 'c++', 'java', 'Ruby']

with open('text_files/test0.txt', 'w') as f:
    for item in lst1:
        f.write(f'{item}\n')

    print('Done')



# Q2
print('----------------------------------------------------------------\nQ2')

def count_words(file):
    text = f.read().rstrip()
    return len(text.split())

file_name = 'text_files/test0.txt'
with open(file_name) as f:
    print(count_words(file_name))



# Q3
print('----------------------------------------------------------------\nQ3')

def clean(listt):         # removes extra symbols from sides of the word to have a better comparison
    res = [word.strip('.():/\'`\\') for word in listt]
    return res

with open('text_files/test2.txt') as f:
    text = f.read()
    lst = text.split()
    lst = set(clean(lst))
    res = sorted(lst, key=lambda x: (len(x), x))
    print(res[:-11:-1])



# Q4
print('----------------------------------------------------------------\nQ4')

res = []
with open('text_files/test1.txt') as f:
    text = f.read()
    for word in text.split():
        w_count = text.count(word)
        res.append((word, w_count))

    print(set(res))



# Q5
print('----------------------------------------------------------------\nQ5')

file1 = 'text_files/test3.txt'
file2 = 'text_files/test4.txt'
with open(file1, 'a') as f1:
    with open(file2) as f2:
        for line in f2:
            f1.write(line)

        print('Done')



# Q6
print('----------------------------------------------------------------\nQ6')

with open('text_files/test6.txt', 'r+') as f:

    original_text = f.read()
    new_text = original_text.replace('\n', '')
    
    f.truncate(0)
    f.seek(0)

    f.write(new_text)

    print('Done')



# Q7
print('----------------------------------------------------------------\nQ7')

print('What would you like to add to your note (Enter "0" to leave or enter "display" to see the note) ?')
while True:
    line = input()             # Enter 0 to exit
    if line.lower() == 'display':
        with open('test5.md') as f:
            print(f'\nYour note :\n{f.read()}\n\n')
    elif str(line) == '0':
        break
    else:
        with open('test5.md', 'a') as f:
            f.write(f'{line}\n')



# Q8
print('----------------------------------------------------------------\nQ8')

class Catchtime:
    def __enter__(self):
        self.start = time()      
    
    def __exit__(self, *args):
        self.end = time()
        print(f'Total time: {self.end - self.start}')
        

with Catchtime() as t:
    count = 10
    for i in range(0, 10000000):
        count += 5


# Q9
print('----------------------------------------------------------------\nQ9')

try:
    file = open('test8.txt', 'r')
except FileNotFoundError as exc:
    print(exc)
    answer = input('Do you want to create this file [y/n] ? ')
    if answer.lower().strip() == 'y' or answer.lower().strip() == 'yes':
        file = open('text_files/test8.txt', 'w')
        file.close()
except Exception:
    print('Error')   
finally:
    print('Done, Bye-bye...')



# Q10
print('----------------------------------------------------------------\nQ10')

def del_milisec(time):
    lst = str(time).split('.')
    return lst[0]
  

with open('text_files/test7.txt', 'w+') as f:
    dikt = {
        'yesterday': datetime.now() - timedelta(1),
        'today': datetime.now(),
        'tomorrow':  datetime.now() + timedelta(1)
    }

    for k, v in dikt.items():
        f.write(f'{k}: {del_milisec(v)}\n')
    
    print('Done')
