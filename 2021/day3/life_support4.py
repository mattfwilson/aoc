from collections import Counter

inputs = [line for line in open('inputs.txt').read().strip().split('\n')]
oxygen = []
scrubber = []
index = 0

def find_most_bits(inputs, index):
    print(f'Index count: {index}')

    for line in inputs:
        if line[index] == '0':
            oxygen.append(line)
        else:
            scrubber.append(line)

    index += 1

    if len(oxygen) > len(scrubber):
        print(f'Oxygen has more: {oxygen}')
        return oxygen
    else:
        print(f'Scrubber has more: {scrubber}')
        return scrubber


counter = Counter(inputs[0])
most_common_item, most_common_count = counter.most_common(1)[0]
print(most_common_item)
#for _ in range(11):
#    inputs = [find_most_bits(x, index) for x in inputs]
