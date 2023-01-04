input_lst = []
grouped_lst = []

with open('inputs.txt', 'r') as file:
    depths = file.readlines()

while True:
    counter = 1
    segment = 0
    for depth in depths:
        num_depth = int(depth.strip())
        input_lst.append(num_depth)
        segment = input_lst[counter-1] + input_lst[counter] + input_lst[counter+1]
        grouped_lst.append(segment)
        counter += 1
    break

print(grouped_lst)