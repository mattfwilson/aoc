grid = []
symbols = []
grid_lines = []
my_list = []
inputs = [grid.append(line) for line in open('inputs.txt').read().split('\n')]

for line in grid:
    grid_lines.append(line)

for i, value in enumerate(grid_lines):
    index = i
    my_list.append(value)
    print(f"Iteration {index}: {value}")

