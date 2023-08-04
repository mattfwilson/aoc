digits = []
oxygen_lst = []
co2_lst = []
res_lst = []
keep_lst = []
index = 0

inputs = [line for line in open('inputs.txt').read().strip().split('\n')]

def oxygen_rating(inputs, index):
    for binary in inputs:
        for bit in binary:
            oxygen_lst.append(bit)
        most_common = max(oxygen_lst)
        ones = oxygen_lst.count('0')
        zeroes = oxygen_lst.count('1')
    for binary in inputs:
        if binary[index] == most_common:
            keep_lst.append(binary)
    return most_common, ones, zeroes

res_lst.append(oxygen_rating(inputs, index))
print(res_lst)
print(keep_lst)
print(len(keep_lst))
index += 1
