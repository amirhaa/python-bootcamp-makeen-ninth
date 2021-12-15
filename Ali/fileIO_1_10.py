# Q1
print('----------------------------------------------------------------\nQ1')

lst1 = ['python', 'c++', 'java', 'Ruby']

with open('newfile.txt', 'w') as f:
    for item in lst1:
        f.write(f'{item}\n')

    print('Done')



# Q2
print('----------------------------------------------------------------\nQ2')

def count_words(file):
    text = f.read().rstrip()
    return len(text.split())

file_name = 'newfile.txt'
with open(file_name) as f:
    print(count_words(file_name))



# Q3
print('----------------------------------------------------------------\nQ3')

def clean(listt):         # removes extra symbols from sides of the word to have a better comparison
    res = [word.strip('.():/\'`\\') for word in listt]
    return res

with open('test2.txt') as f:
    text = f.read()
    lst = text.split()
    lst = clean(lst)
    res = sorted(lst, key=len)
    print(res[:-11:-1])



# Q4
print('----------------------------------------------------------------\nQ4')

res = []
with open('test.txt') as f:
    text = f.read()
    for word in text.split():
        w_count = text.count(word)
        res.append((word, w_count))

    print(res)



# Q5
print('----------------------------------------------------------------\nQ5')

file1 = 'test3.txt'
file2 = 'test4.txt'
with open(file1, 'a') as f1:
    with open(file2) as f2:
        for line in f2:
            f1.write(line)

        print('Done')



# Q6
print('----------------------------------------------------------------\nQ6')

with open('test.txt', 'r+') as f:

    original_text = f.read()
    new_text = original_text.replace('\n', '')
    
    f.truncate(0)
    f.seek(0)

    f.write(new_text)



# Q7
print('----------------------------------------------------------------\nQ7')

pass



# Q8
print('----------------------------------------------------------------\nQ8')

pass



# Q9
print('----------------------------------------------------------------\nQ9')

pass



# Q10
print('----------------------------------------------------------------\nQ10')

pass
