with open('q6_file', 'r+') as f6:
    file_content = f6.read().strip()
    f6.seek(0)
    print(f6.readlines())
    print(file_content)
#     used_range = len(file_content)
# base_lst = []
# for item in file_content:
#     item.strip()
#     base_lst += item
# print(base_lst)
