def combine_dict(dictA, dictB):
    newDict = {}
    for keyA, valueA in dictA.items():
        if keyA in dictB.keys():
            newDict[keyA] = valueA + dictB[keyA]
    dictA.update(newDict)
    dictB.update(dictA)
    return dictB




print(combine_dict({ 'a': 10, 'b': 20, 'c': 30 }, { 'a': 3, 'c': 6, 'd': 3 }))