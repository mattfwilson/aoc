inputs = [line for line in open('inputs.txt').read().strip().split('\n')]
oxygen = []
scrubber = []
bit_lst = []
most_least = []
index = 0
most_common = ''
least_common = ''

def calc_most_common(inputs, index):
    for binary in inputs:
        bit_lst.append(binary[index])
    most_common = max(set(bit_lst), key=bit_lst.count)
    return most_common

def calc_oxygen(inputs, oxygen, scrubber, most_common, index):
    while len(oxygen) > 1:
        for num in inputs:
            if num[index] == most_common:
                oxygen.append(num)
            else:
                scrubber.append(num)
        index += 1
    return oxygen, scrubber

while index < len(inputs[0]):
    most_least.append(calc_most_common(inputs, index))
#    oxygen = calc_oxygen(inputs, oxygen, scrubber, most_common, index)
    print(f'Most common in index {index}: {most_least[index]}')
    index += 1

print(most_least)
print(f'Reached end of script')
