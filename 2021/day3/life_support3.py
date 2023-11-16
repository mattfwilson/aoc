inputs = [line for line in open('inputs.txt').read().strip().split('\n')]
oxygen = []
scrubber = []
bit_lst = []
index = 0
most_common = ''
least_common = ''

def calc_most_common(inputs, index):
    for binary in inputs:
        bit_lst.append(binary[index])
    most_common = max(set(bit_lst), key=bit_lst.count)
    return most_common

def calc_ratings(keep_lst, most_common, least_common, index, oxygen, scrubber):
    for num in keep_lst:
        if num[index] == most_common:
            oxygen.append(num)
        else:
            scrubber.append(num)
    return oxygen, scrubber

#print(type(inputs))
#for i in inputs:
#    print(f'{i} - {type(i)}')

while index <= len(inputs[0]) - 1:
    most_common = calc_most_common(inputs, index)
    ratings = calc_ratings(inputs, most_common, least_common, index, oxygen, scrubber)
    print(f'most common: {most_common}')
    print(f'oxygen: {oxygen} - len: {len(oxygen)}')
    print(f'scrubber: {scrubber} - {len(scrubber)}')
    bit_lst.clear()
    index += 1

print(f'Reached end of script')
