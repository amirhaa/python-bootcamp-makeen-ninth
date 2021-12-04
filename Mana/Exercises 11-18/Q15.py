def mean(myDict):
    sum = 0
    for value in myDict.values():
        sum += value
    return sum / len(scores)


scores = {"Mathematics": 18, "History": 16, "Physics": 20}
print(mean(scores))
