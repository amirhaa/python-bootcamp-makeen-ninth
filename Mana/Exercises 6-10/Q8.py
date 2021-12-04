# def concatenate(twoDimensionalList):
#     result = []
#     for item in twoDimensionalList:
#         result.extend(item)
#     return sorted(result)


# print(concatenate([[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]))

def flatten(listA):
    res = []
    for num in listA:
        res = [*res, *num]

    return sorted(res)


print(flatten([[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]))
