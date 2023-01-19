import emoji

input_lst = []
segment_lst = []
count = 0
increases = 0
current = 157

with open('inputs.txt', 'r') as file:
    depths = file.readlines()

for depth in depths:
    input_lst.append(int(depth.strip()))
    try:
        total_seg = 0
        total_seg = input_lst[count] + input_lst[count + 1] + input_lst[count + 2]
        count += 1
        segment_lst.append(total_seg)
    except IndexError:
        print('Hit IndexError (cannot sum indexes further')

for index, segment in enumerate(segment_lst):
    if segment > current:
        current = segment
        increases += 1
        print(emoji.emojize(f'Index: {index} - {segment} :chart_increasing:'))
    if segment <= current:
        current = segment
        print(emoji.emojize(f'Index: {index} - {segment} :chart_decreasing:'))

print(f'\nCounter: {count}')
print(f'Increases: {increases}')
        




