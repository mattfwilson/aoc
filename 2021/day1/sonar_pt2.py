input_lst = []
segment_lst = []
count = 0
increases = 0
decreases = 0
current = 157

with open('inputs.txt', 'r') as file:
    depths = file.readlines()

for line in depths:
    input_lst.append(int(line.strip()))
print(input_lst)

for depth in input_lst:
    try:
        total_seg = 0
        total_seg = input_lst[count] + input_lst[count + 1] + input_lst[count + 2]
        count += 1
        segment_lst.append(total_seg)
    except IndexError:
        print('Hit an IndexError')
    finally:
        pass

for segment in segment_lst:
    if segment > current:
        current = segment
        increases += 1
        print(f'{segment} INCREASED!')
    if segment <= current:
        current = segment
        decreases += 1
        print(f'{segment} decreased!')

print(f'Increases: {increases}')
print(f'Decreases: {decreases}') 
        




