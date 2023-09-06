inputs = [line for line in open('inputs.txt').read().strip().split('\n')]
oxygen = []
scrubber = []
bit_lst = []
index = 0
most_common = str()
least_common = str()

def calc_most_common(inputs, index):
    for binary in inputs:
        bit_lst.append(binary[index])
    most_common = max(set(bit_lst), key=bit_lst.count)
    return most_common

def calc_ratings(inputs, most_common, least_common, index):
    for num in inputs:
        if num[index] == most_common:
            oxygen.append(num)
        else:
            scrubber.append(num)
    return oxygen, scrubber

print(len(inputs))
for i in inputs:
    print(f'{i} - {type(i)}')

while index <= len(inputs[0]) - 1:
    most_common = calc_most_common(inputs, index)
    ratings = calc_ratings(inputs, most_common, least_common, index)
    print(f'most common: {most_common}')
    print(f'ratings: {len(ratings[0])} / {len(ratings[1])}')
    bit_lst.clear()
    index += 1

print(f'Reached end of script')
