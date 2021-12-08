def e6():
    elements = int(input("How many elements are you going to add? \n"))
    num_list = []
    for i in range(0, elements):   
        user_value = int(input(f'enter the value number {i + 1} \n'))
        num_list.append(user_value)
    num_sum = 0
    for num in num_list:
        num_sum += num 
    if num_sum % 2 == 0:
        print (f"the sum is {num_sum}, so it's ((even))")
    else:
        print(f"the sum is {num_sum}, so it's ((odd))")
e6()
