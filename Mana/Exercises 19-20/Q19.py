def create_phone_number(numList):

    return f"({''.join(str(item) for item in numList[0:3])}) {''.join(str(item) for item in numList[3:6])}-{''.join(str(item) for item in numList[6::])}"


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
