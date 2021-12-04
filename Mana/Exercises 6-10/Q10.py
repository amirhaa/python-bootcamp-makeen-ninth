# def descending_numbers(number):
#     result = []
#     for item in str(number):
#         result.append(item)
#     print(result)
#     result = sorted(result, reverse=True)
#     return "".join(result)

def descending_numbers(number):
    return int("".join(sorted(str(number), reverse=True)))


print(descending_numbers(9845))
