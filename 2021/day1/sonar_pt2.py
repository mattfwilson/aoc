counter = 0
groups = []
segment = 0

with open('inputs.txt', 'r') as file:
    depths = file.readlines()

while True:
    for depth in depths:
        num_depth = int(depth.strip())
        if counter == 3:
            groups.append(segment)
            counter = 0
            threes = 0
        else:
            segment += num_depth # first segment should be 482
            print(f'{num_depth} - {type(num_depth)}')
            counter += 1
    break
print(groups)
