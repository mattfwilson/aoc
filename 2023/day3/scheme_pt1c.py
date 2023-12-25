grid = []
symbols = []
grid_lines = []
my_list = []
inputs = [grid.append(line) for line in open('inputs.txt').read().split('\n')]

for line in grid:
    grid_lines.append(line)

for i in range(len(grid_lines)):
    value = i
    my_list.append(value)
    print(f"Iteration {i}: {value}")

index_choice = 33

if index_choice < len(my_list):
    print(f"Value at iteration {index_choice}: {my_list[index_choice]}")
else:
    print(f"Invalid iteration number: {index_choice}")
