from collections import Counter

inputs = [line for line in open('inputs.txt').read().strip().split('\n')]
oxygen = []
scrubber = []
bit_lst = []
index = 0

def find_most_bits(inputs, index):
    print(f'Index iteration: {index}')

    counter = Counter(inputs[index])
    most_common_item = counter.most_common()[0]
    
    print(most_common_item)

    for line in inputs:
        if line[index] == most_common_item:
            pass
        else:
            inputs.remove(line)
    return inputs

print(inputs)
while True:
    if index > 11:
        break
    else:
        bit_lst = find_most_bits(inputs, index)
    index += 1

