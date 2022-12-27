counter = 0
groups = []

with open('inputs.txt', 'r') as file:
    depths = file.readlines()

while True:
    for depth in depths:
        three = 0
        num_depth = int(depth.strip())
        three += num_depth
        print(f'{num_depth} - {type(num_depth)}')
        counter += 1
        if counter == 3:
            groups.append(three)
            counter = 0
            threes = 0
    break
print(groups)
