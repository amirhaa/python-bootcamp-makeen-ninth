# Q6:

def odd_or_even_sum(numbers):
    return "even" if sum(numbers) % 2 == 0 else "odd"

# def odd_or_even_sum(numbers):
#     sum = 0
#     for item in numbers:
#         sum += item
#     if sum % 2 == 0:
#         return "even"
#     else:
#         return "odd"

# ----------------------------------------

# Q7:

def sort_strings(list_strings):
    return sorted(list_strings, key=len)

# ----------------------------------------

# Q8:

def flatten(two_dimensional_list):
    result = []
    for item in two_dimensional_list:
        result.extend(item)
    return sorted(result)

# def flatten(listA):
#     res = []
#     for num in listA:
#         res = [*res, *num]

#     return sorted(res)

# --------------------------------------

# Q9:

def bellow_the_limit(numbers, value):
    for item in numbers:
        if item > value:
            False
    return True

# ---------------------------------------

# Q10:

def descending_numbers(number):
    return int("".join(sorted(str(number), reverse=True)))

# ---------------------------------------

# Q+:

def sort_str(listA):
    return sorted(listA, key= lambda i: i[-1].lower())
