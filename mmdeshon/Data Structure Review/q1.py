l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l3 = []
for index, item in enumerate(l1[::2]):
    l3.append(item)
    if index == 5:
        break
    l3.append(l2[index*2 + 1])
print(l3)
