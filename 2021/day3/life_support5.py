from collections import Counter

inputs = [line for line in open('inputs.txt').read().strip().split('\n')]
oxygen = []
scrubber = []
index = 0

def find_most_bits(inputs, index):
    print(f'Index count: {index}')


    counter = Counter(inputs[index])
    most_common_item = counter.most_common()[0]
    
    print(most_common_item)

    for line in inputs:
        print(line[index])
        if line[index] == most_common_item:
            oxygen.append(line)
        else:
            scrubber.append(line)

    return oxygen, scrubber

while True:
    if index > 11:
        break
    else:
        oxygen = find_most_bits(inputs, index)
    index += 1
