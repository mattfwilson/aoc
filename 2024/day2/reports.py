inputs = []
int_inputs = []
valid_diffs = []
is_increasing = []
res_lst = []


with open('inputs.txt', 'r') as file:
    for line in file:
        inputs.append(line.strip().split())

# convert list to ints
for lst in inputs:
    int_inputs.append([int(num) for num in lst])


# filter differences equaling 1-3
for lst in int_inputs:
    if all(lst[i] - lst[i + 1] for i in range(len(lst) - 1)) > 0 and all(lst[i] - lst[i + 1] for i in range(len(lst) - 1)) < 4:
        valid_diffs.append(lst)

print(f'good_diffs: {valid_diffs}')
print(len(valid_diffs))

# filter strictly increasing
for lst in valid_diffs:
    if all(lst[i] < lst[i + 1] for i in range(len(lst) - 1)):
        is_increasing.append(lst)

print(f'is_increasing: {is_increasing}')
print(len(is_increasing))

# filter strictly decreasing
for lst in valid_diffs:
    if all(lst[i] > lst[i + 1] for i in range(len(lst) - 1)):
        res_lst.append(lst)

print(f'res_lst: {res_lst}')
print(len(res_lst))

