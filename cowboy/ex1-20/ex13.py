list1 = [1, 2, 3, 3, 4]
list2 = [1, 4, 5]

def list1uniqe(listA,listB):
    set1 = set(listA)
    set2 = set(listB)
    result = list(set1 - set2)
    return print(result)

def listuniqe(listA,listB):
    new_list = []
    for x in listA:
        if x not in listB and x not in new_list:
            new_list.append(x)
    return print(new_list)
    
listuniqe(list1,list2)


    


    
    
 

                
    
list1uniqe(list1,list2)