
with open('inputs.txt', 'r') as file:
    depths = file.readlines()

for depth in depths:
    print(depth.strip())