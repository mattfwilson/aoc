keep_lst = []
bit_lst = []
index = 0

inputs = [line for line in open('inputs.txt').read().strip().split('\n')]

def oxygen_rating(inputs, index):
    for binary in inputs:
        for bit in binary:
            bit_lst.append(bit)
        most_common = max(bit_lst)
    for binary in inputs:
        if binary[index] == most_common:
            keep_lst.append(binary)
    return most_common
while index <= 3:
    res = oxygen_rating(inputs, index)
    print(res)
    index += 1

print(keep_lst)
print(f'Len oxygen_lst: {len(keep_lst)}')
print(f'Len inputs: {len(inputs)}')
