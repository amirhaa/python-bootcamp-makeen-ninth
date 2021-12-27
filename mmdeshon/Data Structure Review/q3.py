main_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

len_slice = len(main_list) / 3
if len_slice.is_integer():
    len_slice = int(len_slice)
    slice1 = main_list[:len_slice:]
    slice2 = main_list[len_slice:len_slice*2:]
    slice3 = main_list[len_slice*2:len_slice*3:]
    result = [*slice1[::-1], *slice2[::-1], *slice3[::-1]]
    print(result)
else:
    print('Better luck next time')
