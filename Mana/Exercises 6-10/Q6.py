# def odd_or_even_sum(listNumbers):
#     sum = 0
#     for item in listNumbers:
#         sum += item
#     if sum % 2 == 0:
#         return "even"
#     else:
#         return "odd"


# print(odd_or_even_sum([2, 10]))

# ----------------------------------------


def odd_or_even_sum(listNumbers):
    return "even" if sum(listNumbers) % 2 == 0 else "odd"

print(odd_or_even_sum([2, 4, 3]))
