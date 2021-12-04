# def highest_values(myList):
#     result = []
#     for _ in range(2):
#         num = 0
#         for item in myList:
#             if item > num:
#                 num = item
#         for _ in range(myList.count(num)):
#             myList.remove(num)
#         result.append(num)
#     return result

# print(highest_values([4, 8, 2, 9, 9]))

# ---------------------------------------

# def highest_values(myList):
#     result = []
#     myList = set(myList)
#     for _ in range(2):
#         num = max(myList)
#         result.append(num)
#         myList.remove(num)
#     return result


# print(highest_values([4, 8, 2, 9, 9]))

# ---------------------------------------

def highest_values(myList):
    return sorted(set(myList))[-2:]
        
        
print(highest_values([4, 8, 2, 9, 9]))





