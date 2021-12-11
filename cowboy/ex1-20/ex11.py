list_guys = ["abedini" , "sabet" , "mana" ,]
def count_v(name):
    vowels = ("a", "e", "i","o", "u")
    num = 0
    for char in name :
        for items in vowels :
            if char == items :
             num += 1
    return print(num)
        
count_v(list_guys)
