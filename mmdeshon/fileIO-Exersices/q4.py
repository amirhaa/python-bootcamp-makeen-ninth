# from collections import Counter

with open('q4_file') as f4:
    sm_list = f4.read().strip().split()

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

frequency_dict = {}
# frequency_dict = dict(Counter(sm_list))
for statement in sm_list:
    if statement not in frequency_dict:
        frequency_dict[statement] = 1
    else:
        frequency_dict[statement] += 1

# Method 1
result_tuple = tuple(list(frequency_dict.items()))
print(result_tuple)

# Method 2
final_result = []
for key, val in frequency_dict.items():
    final_result.append(key)
    final_result.append(val)
print(tuple(final_result))
