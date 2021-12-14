
list_1 = ["Java", "Python", "Go", "Js"]
list_2 = []


def sort_list(listA):
    listB = []
    number = 1
    while len(listA) != len(listB) :
        for items in list_1 :
            if len(items) == number :
             listB.append(items)
        number += 1
    return listB

d