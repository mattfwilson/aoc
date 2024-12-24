inputs = []
int_inputs = []
is_consecutive = []
is_decreasing = []


with open('inputs.txt', 'r') as file:
    for line in file:
        inputs.append(line.strip().split())

for lst in inputs:
    int_inputs.append([int(num) for num in lst])
        
for lst in int_inputs:
    if all(lst[i] < lst[i + 1] for i in range(len(lst) - 1)):
        is_consecutive.append(lst)

print(f'increasing check: {is_consecutive}')
print(len(is_consecutive))

for lst in int_inputs:
    if all(lst[i] > lst[i + 1] for i in range(len(lst) - 1)):
        is_consecutive.append(lst)

print(f'decreasing check: {is_consecutive}')
print(len(is_consecutive))
