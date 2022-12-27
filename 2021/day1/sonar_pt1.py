increases = 0
decreases = 0
current = 157
counter = 0

with open('inputs.txt', 'r') as file:
    depths = file.readlines()

for depth in depths:
    num_depth = int(depth.strip())
    print(f'{num_depth} - {type(num_depth)}') 
    if num_depth > current:
        current = num_depth
        increases += 1
        print(f'{num_depth} increased!')
    else:
        current = num_depth
        decreases += 1
        print(f'{num_depth} decreased!')

print(f'Increases: {increases}')
print(f'Decreases: {decreases}')
