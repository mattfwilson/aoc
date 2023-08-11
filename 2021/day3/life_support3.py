inputs = [line for line in open('inputs.txt').read().strip().split('\n')]
oxygen = inputs.copy()
scrubber = inputs.copy()
bit_lst = []
index = 0
most_common = 0
least_common = 0

def calc_most_common(inputs, scrubber, bit_lst, index):
    for binary in inputs:
        bit_lst.append(int(binary[index]))
    most = max(set(bit_lst), key=bit_lst.count)
    return most

def calc_ratings(keep_lst, most_common, least_common, index):
    for num in keep_lst:
        if num[index] == most_common:
            oxygen.append(num)
        elif num[index] == least_common:
            scrubber.append(num)
    return oxygen, scrubber

while index <= len(inputs[0]) - 1:
    most_common = calc_most_common(oxygen, scrubber, bit_lst, index)
    ratings = calc_ratings(oxygen, most_common, least_common, index)
    print(f'most common: {most_common}')
    print(f'ratings: {len(ratings[0])} / {len(ratings[1])}')
    bit_lst.clear()
    index += 1

print(f'Reached end of script')
