with open('q3_file') as f3:
    sm_list = f3.read().strip().split()
not_accepted_prefix = [',', '(', '.', '"', "'"]
not_accepted_suffix = [',', ')', '.', '"', "'"]
for index, statement in enumerate(sm_list):
    if statement[0] in not_accepted_prefix:
        sm_list[index] = statement[1::]
    if statement[-1] in not_accepted_suffix:
        sm_list[index] = statement[:-1:]

for index, statement in enumerate(sm_list):
    if statement[0] in not_accepted_prefix:
        sm_list[index] = statement[1::]
    if statement[-1] in not_accepted_suffix:
        sm_list[index] = statement[:-1:]

for index, statement in enumerate(sm_list):
    if statement in sm_list[index+1::]:
        sm_list.pop(index)

sm_list.sort(key=len, reverse=True)
# print(sm_list)
print(sm_list[:10])
# (salam,)