def my_list(num) :
    my_list_1 = list(set(num))
    list_2 = sorted(my_list_1)
    list_3 = list_2[-2:]
    return print(list_3)


def highest_values(myList):
    result = []

    for time in range(2) :
        num = 0
        for item in myList:
            if item > num:
                num =item
        for count in range(myList.count(num)):
            myList.remove(num)
        result.append(num)
    return result


