input_lst = []
grouped_lst = []

with open('inputs.txt', 'r') as file:
    depths = file.readlines()

while True:
    count = 1
    segment = 0
    for depth in depths:
        int_depth = int(depth.strip())
        input_lst.append(int_depth)
        segment = int_depth[count-1] + int_depth[count] + int_depth[count+1]
        grouped_lst.append(segment)
        count += 1
    break

print(grouped_lst)