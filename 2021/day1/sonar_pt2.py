input_lst = []
segment_lst = []
counter = 0
increases = 0
current = 157

with open('inputs.txt', 'r') as file:
    depths = file.readlines()

for depth in depths:
    input_lst.append(int(depth.strip()))
    try:
        total_seg = 0
        total_seg = input_lst[counter] + input_lst[counter + 1] + input_lst[counter + 2]
        counter += 1
        segment_lst.append(total_seg)
    except IndexError:
        print('Hit IndexError (cannot sum next three indexes')

for index, segment in enumerate(segment_lst):
    if segment > current:
        current = segment
        increases += 1
        print(f'Index: {index} - {segment}')
    if segment <= current:
        current = segment
        print(f'Index: {index} - {segment}')

print(f'\nCounter: {counter}')
print(f'Increases: {increases}')
        




