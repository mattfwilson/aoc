counter = 0
segment = 0
groups = []

with open('inputs.txt', 'r') as file:
    depths = file.readlines()

while True:
    for depth in depths:
        num_depth = int(depth.strip())
        if counter < 3:
            segment += num_depth
            print(f'{num_depth}')
            counter = counter + 1
        else:
            groups.append(segment)
            counter = 0
    break

print(groups)
print(segment)
