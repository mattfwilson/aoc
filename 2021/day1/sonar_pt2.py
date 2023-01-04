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
        segment = 0
        segment = input_lst[count] + input_lst[count+1] + input_lst[count+2]
        print(input_lst.index(depth))
        print(segment)
        count += 1
        segment_lst.append(segment)
    except IndexError:
        pass
    finally:
        if segment > current:
            current = segment
            increases += 1
            print(f'{segment} increased!')
        else:
            current = segment
            decreases += 1
            print(f'{segment} decreased!')

print(f'Increases: {increases}')
print(f'Decreases: {decreases}') 
        




