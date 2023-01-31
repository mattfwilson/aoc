input_lst = []
segment_lst = []
counter = 0
increases = 0
current = 157

with open('inputs.txt', 'r') as file:
    depths = file.readlines()

for index, depth in enumerate(depths):
    input_lst.append(int(depth.strip()))
    try:
        total_seg = input_lst[counter] + input_lst[counter + 1] + input_lst[counter + 2]
        segment_lst.append(total_seg)
        counter += 1
    except IndexError:
        print('Hit IndexError (cannot sum next three indexes)')

for index, segment in enumerate(segment_lst):
    if segment > current:
        current = segment
        increases += 1
        print(f'Index: {index} -- Segment {segment} UP')
    if segment <= current:
        current = segment
        print(f'Index: {index} -- Segment {segment} DOWN')

print(f'\nCounter: {counter}')
print(f'Increases: {increases}')
        