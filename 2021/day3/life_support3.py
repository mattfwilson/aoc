inputs = [line for line in open('inputs.txt').read().strip().split('\n')]
oxygen = inputs.copy()
scrubber = inputs.copy()
bit_lst = []
index = 0

def calc_ratings(inputs, bit_lst, oxygen, scrubber, index):
    for binary in inputs:
        if binary[index] == most_common:
            oxygen.append(binary)
        elif binary[index] == least_common:
            scrubber.append(binary)
    return most_common, least_common, oxygen, scrubber

def calc_min_max(oxygen, scrubber, index):
    for binary in inputs:
        bit_lst.append(binary[index])
    most_common = max(bit_lst)
    least_common = min(bit_lst)
    return most_common, least_common

def calc_oxygen(keep_lst, index):
    if most_common == least_common:
        for binary in keep_lst:
            if binary[index] == 1:
                oxygen.append(binary)

def calc_scrubber(keep_lst, index):
    if most_common == least_common:
        for binary in keep_lst:
            if binary[index] == 1:
                scrubber.append(binary)

while index <= len(inputs[0]) - 1:
    calc_most_common(oxygen, scrubber, index)
    oyxgen_res = calc_oxygen(oxygen, index)
    scrubber_res = calc_scrubber(scrubber, index)
    print()
#    oxygen.clear()
#    scrubber.clear()
    index += 1
