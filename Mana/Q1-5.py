# Q1:

def reverse_list(lst):
    return lst[::-1]

# def reverse_list(lst):
#     result = []
#     for item in lst:
#         result.insert(0 , item)
#     return result

# --------------------------------------

# Q2:

def highest_values(lst):
    return sorted(set(lst))[-2:]

# def highest_values(lst):
#     result = []
#     for _ in range(2):
#         num = 0
#         for item in lst:
#             if item > num:
#                 num = item
#         for _ in range(lst.count(num)):
#             lst.remove(num)
#         result.append(num)
#     return result

# def highest_values(lst):
#     result = []
#     lst = set(lst)
#     for _ in range(2):
#         num = max(lst)
#         result.append(num)
#         lst.remove(num)
#     return result

# ----------------------------------------

# Q3:

def invert(lst):
    return [-item for item in lst]

# -----------------------------------------

# Q4:

def num_to_list(num):
    return [int(item) for item in str(num)]

# ------------------------------------------

# Q5:

def filter_list(lst):
    return [item for item in lst if type(item) == int]           

