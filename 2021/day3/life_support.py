inputs = [line for line in open('inputs.txt').read().strip().split('\n')]
keep_lst = inputs.copy()
bit_lst = []
index = 0

def oxygen_rating(inputs, bit_lst, keep_lst, index):
    for binary in inputs:
        bit_lst.append(binary[index])
    most_common = max(bit_lst)
    least_common = min(bit_lst)

    for binary in inputs:
        if binary[index] == most_common:
            keep_lst.append(binary)
    return most_common, keep_lst

while index <= len(inputs[0]) - 1:
    res = oxygen_rating(inputs, bit_lst, keep_lst, index)
    print(f'most common: {res[0]} - keep_lst total: {len(res[1])}')
    keep_lst.clear()
    index += 1
