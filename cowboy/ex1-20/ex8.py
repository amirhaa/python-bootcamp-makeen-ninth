list_1 = [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]
list_2= []
list_3= []

def asdf(listA):
    result = []
    for item in listA:
        result.extend(item)
    return sorted(result)

print(asdf(list_1))




def flatten(lis_mana):
    list_abedini = []
    for items in lis_mana:
        list_abedini = [*list_abedini , *items]
    return sorted(list_abedini)
print(flatten(list_1))
    

        
    
        
         




    

