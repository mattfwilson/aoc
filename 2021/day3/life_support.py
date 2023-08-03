digits = []
oxygen_lst = []
co2_lst = []
res_lst = []
index = 0

inputs = [line for line in open('inputs.txt').read().strip().split('\n')]

def oxygen_rating(inputs, index):
    for binary in inputs:
        for bit in binary:
            oxygen_lst.append(bit)
        most_common = max(oxygen_lst)
        ones = oxygen_lst.count('0')
        zeroes = oxygen_lst.count('1')
    return most_common, ones, zeroes

while index < len(inputs[0]):
    res_lst.append(oxygen_rating(inputs, index))
    print(res_lst)
    index += 1
