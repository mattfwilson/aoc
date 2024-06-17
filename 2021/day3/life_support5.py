from collections import Counter

inputs = [line for line in open('inputs.txt').read().strip().split('\n')]
bit_lst = []
index = 0

def find_most_bits(inputs, index):
    print(f'Index iteration: {index}')

    counter = Counter(inputs[index])
    most_common_item = counter.most_common()[0][0]
    print(most_common_item)
    print(type(most_common_item))

    for line in inputs:
        if line[index] == most_common_item:
            continue
        else:
            inputs.remove(line)
    return inputs

while True:
    if index > 11:
        break
    else:
        inputs = find_most_bits(inputs, index)
    index += 1

