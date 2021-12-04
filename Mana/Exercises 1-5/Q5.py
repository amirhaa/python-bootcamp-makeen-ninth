def filter_list(myList):
    result = [item for item in myList if type(item) == int]           
    return result


print(filter_list([2,8,9,"gg", True, 7, "8", 0]))
