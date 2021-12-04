def bellow_the_limit(listNumbers, value):
    for item in listNumbers:
        if item <= value:
            continue
        else:
            return False
    return True


print(bellow_the_limit([-1, -2, -8], 10))
