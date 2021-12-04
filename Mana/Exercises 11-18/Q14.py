def update_dict(myDict, myTuple):
    myDict[myTuple[0]] = myTuple[1]
    return myDict


person = {"name": "Andy"}
print(update_dict(person, ("age", 20)))
