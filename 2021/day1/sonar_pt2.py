counter = 1
segment = 0
groups = []

with open('inputs.txt', 'r') as file:
    depths = file.readlines()

while True:
    for depth in depths:
        num_depth = int(depth.strip())
        segment = num_depth[counter-1] + num_depth + num_depth[counter+1]
        groups.append(segment)
        counter += 1
    break

print(groups)