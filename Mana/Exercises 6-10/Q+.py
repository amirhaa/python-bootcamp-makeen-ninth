def sort_str(list1):
    return sorted(list1, key= lambda i: i[-1].lower())

print(sort_str(["a", "abc", "cab", "dabD"]))


# def sort_str(list1):
#     new_list = sorted([item[::-1].lower() for item in list1])
#     res =[item[::-1].lower() for item in new_list]

#     return res


# print(sort_str(["a", "abc", "cad", "dabb"]))