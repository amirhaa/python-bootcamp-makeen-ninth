dict1 = { 'a': 10, 'b': 20, 'c': 30 }
dict2 = { 'a': 3, 'c': 6, 'd': 3 }

def combine_dict(dictA , dictB):
    newDict = {}
    for keys,values in dictA.items():
        if keys in dictB.keys():
            newDict[keys] = values + dictB[keys]
    dictA.update(newDict)
    dictB.update(dictA)
    return dictB

print(combine_dict(dict1,dict2))