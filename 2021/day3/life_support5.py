from collections import Counter

inputs = [line for line in open('inputs.txt').read().strip().split('\n')]

def remove_bits(inputs, index, end):
    while True:
        if index > end:
            return inputs
        else:
            counter = Counter(inputs[index])
            most_common_item = counter.most_common()[0][0]

            print(f'Index iteration: {index}')
            print(most_common_item)

            for line in inputs:
                if line[index] == most_common_item:
                    pass
                else:
                    inputs.remove(line)
        index += 1
    
    if len(inputs) == 1:
        return inputs
    else:
        remove_bits(inputs, index, end)

remove_bits(inputs, 0, 11)
print(inputs)
