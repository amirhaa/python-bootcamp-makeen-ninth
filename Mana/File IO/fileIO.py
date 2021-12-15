# Q1:

countries = ["Iran", "Canada", "Rwanda", "Georgia", "Italy"]

with open("list_file.txt", "w") as f:
    
    for country in countries:
        f.write(f"{country}\n")

# ---------------------------------

# Q2:

with open("little_prince.txt") as f:
    count = 0
    for line in f.readlines():
        count += len(line.split())

    print(count)

# ---------------------------------

# Q3:

with open("little_prince.txt") as f:

    words= []

    for line in f.readlines():
        words.extend(line.split())
    print(sorted(words, key=len, reverse=True)[:11])

# ---------------------------------

# Q4:

with open("little_prince.txt") as f:

    words= []
    lst_words = []

    for line in f.readlines():
        words.extend(line.split())
    
    for word in words:
        result_tuple = (word.lower(), words.count(word) + words.count(word.lower()))

        if result_tuple in lst_words: continue
        else:
            lst_words.append(result_tuple)

    print(lst_words)

# ---------------------------------

# Q5:

with open("fileA.txt") as fileA:
    with open("fileB.txt") as fileB:
        with open("fileCombine.txt", "w") as fileC:
            for lineB in fileB.readlines():
                lineB = lineB.rstrip("\n") + fileA.readline()
                fileC.write(lineB)

# ------------------------------------

# Q6:

with open("nlineignore.txt", "r") as file:
    res = [line.rstrip("\n") for line in file.readlines()]
    with open("nlineignore.txt", "w") as f:
        f.writelines(res)


# --------------------------------------

# Q7:

with open("file.md", "a+") as file:
    notes = []
    while True:
        cmd = input("Enter your notes. [type display if you wanna end it]")
        if cmd == "display":
            print("Your notes are: ".format('\n'.join(notes)))
            break
        else:
            file.write(cmd + "\n")
            notes.append(cmd)

# --------------------------------------

# Q8:

from time import time

class Catchtime:
    # def __init__(self, description):
    #     self.description = description
    
    def __enter__(self):
        self.start = time()      
    
    def __exit__(self, *args):
        self.end = time()
        print(f"Time: {self.end - self.start}")
        

with Catchtime() as t:
    count = 10
    for i in range(0, 10000000):
        count += 5


# ---------------------------------------

# Q9:

try:
    file = open("file33.txt", "r")
except FileNotFoundError as exc:
    print(exc)
    ans = input("Do you wanna create this file?[y/n]")
    if ans == "y":
        file = open("file33.txt", "w")
        pass
        file.close()

except Exception:
    print("Erorr")   

finally:
    print("bye")


# --------------------------------------

# Q10:

import datetime

with open("time_file.txt", "w") as f:
    today = datetime.datetime.today().replace(microsecond=0)

    yesterday = today - datetime.timedelta(days = 1)

    tomorrow = today + datetime.timedelta(days= 1)

    f.write(f"Yesterday: {yesterday} \nToday: {today} \nTomorrow: {tomorrow}")




