inputs = []
int_inputs = []
valid_diffs = []
no_dupes = []
invalid_diffs = []
is_increasing = []
res_lst = []


with open('inputs.txt', 'r') as file:
    for line in file:
        inputs.append(line.strip().split())

def has_dupes(lst):
    return len(lst) != len(set(lst))

# convert list to ints
for lst in inputs:
    int_inputs.append([int(num) for num in lst])


# filter differences equaling 1-3
for lst in int_inputs:
    dupe = has_dupes(lst)

    if dupe == True:
        int_inputs.remove(lst)
for lst in no_dupes:
    valid_range = all(abs(lst[i] - lst[i + 1]) for i in range(len(lst) - 1))

    if valid_range > 0 and valid_range < 4:
        valid_diffs.append(lst)
    else:
        invalid_diffs.append(lst)

for lst in no_dupes:
    print(lst)

print(f'len of valid_diffs: {len(valid_diffs)}')
print(f'len of invalid_diffs: {len(invalid_diffs)}')

test1 = has_dupes(int_inputs[0])
test2 = has_dupes(int_inputs[3])
print(test1)
print(test2)

## filter strictly increasing
#for lst in valid_diffs:
#    if all(lst[i] < lst[i + 1] for i in range(len(lst) - 1)):
#        res_lst.append(lst)
#
#print(f'is_increasing: {is_increasing}')
#print(len(is_increasing))
#
## filter strictly decreasing
#for lst in valid_diffs:
#    if all(lst[i] > lst[i + 1] for i in range(len(lst) - 1)):
#        res_lst.append(lst)
#
#print(f'res_lst: {res_lst}')
#print(len(res_lst))

