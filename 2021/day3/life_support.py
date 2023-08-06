keep_lst = []
bit_lst = []
index = 0

inputs = [line for line in open('inputs.txt').read().strip().split('\n')]

def oxygen_rating(inputs, bit_lst, keep_lst, index):
    for binary in inputs:
        bit_lst.append(binary[index])
    most_common = max(bit_lst)

    for binary in inputs:
        if binary[index] == most_common:
            keep_lst.append(binary)
    return keep_lst

while index <= len(inputs[0]) - 1:
    res = oxygen_rating(inputs, bit_lst, keep_lst, index)
    print(f'keep_lst: {res}')
    print(f'Len oxygen_lst: {len(keep_lst)}')
    print(f'Len inputs: {len(inputs)}')
    index += 1
