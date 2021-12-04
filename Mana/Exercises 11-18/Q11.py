def count_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for item in string:
        if item in vowels:
            count += 1
    return count


print(count_vowels("this is a test"))

list_A = ["abedini", "khashayar", "mana", "sabet"]

def count_vowels_list(listA):
    count = 0
    for item in list_A:
        count += count_vowels(item)
    return count

print(count_vowels_list(list_A))






