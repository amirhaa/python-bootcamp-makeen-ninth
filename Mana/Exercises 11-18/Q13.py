def unique_items(list1, list2):
    result = []
    for i in list1:
        if i not in list2 and i not in result:
            result.append(i)
    return result


print(unique_items([1, 2, 3, 3, 4], [1, 4, 5]))
