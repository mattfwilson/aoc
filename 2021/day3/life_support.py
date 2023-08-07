inputs = [line for line in open('inputs.txt').read().strip().split('\n')]
oxygen = inputs.copy()
scrubber = inputs.copy()
bit_lst = []
index = 0

def calc_ratings(inputs, bit_lst, oxygen, scrubber, index):
    for binary in inputs:
        bit_lst.append(binary[index])
    most_common = max(bit_lst)
    least_common = min(bit_lst)

    for binary in inputs:
        if binary[index] == most_common:
            oxygen.append(binary)
        elif binary[index] == least_common:
            scrubber.append(binary)
    return most_common, oxygen, scrubber

while index <= len(inputs[0]) - 1:
    res = calc_ratings(inputs, bit_lst, oxygen, scrubber, index)
    print(f'most common: {res[0]} - oxygen total: {len(res[1])} - scrubber total: {len(res[2])}')
    oxygen.clear()
    scrubber.clear()
    index += 1
