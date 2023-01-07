split_lst = []
count = 0 
with open('inputs.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    split_lst.append(line.strip().split(' '))

for item in split_lst:
    print(item)
    count += 1

print(count)
    # for char in split_lst:
    #     if char == 'A' or char == 'X':
    #         split_lst.replace(char, 1)
    #     if char == 'B' or char == 'Y':
    #         split_lst.replace(char, 2)
    #     if char == 'C' or char == 'Z':
    #         split_lst.replace(char, 3)