list_1 = [[4, 7, 10, 20, 18], 20]
def bellow_limit(listA):
    listB =listA[0]
    listC = [*listB , listA[1]]
    for items in listA:
     if items <= listC[-1] :
         return True
    
    return False


        
def bellow_limit_2(A,B):
    for items in A :
        if items <= B :
         return print(True)
    
    return print(False)

 


    
bellow_limit_2([4, 7, 10, 20, 18], 20)