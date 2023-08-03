digits = []
oxygen_lst = []
co2_lst = []
index = 0

inputs = [line for line in open('inputs.txt').read().strip().split('\n')]

def oxygen_rating(inputs, index):
    for bit in inputs[index]:
        oxygen_lst.append(bit)
    most_common = max(oxygen_lst)
    ones = oxygen_lst.count('0')
    zeroes = oxygen_lst.count('1')
    index += 1
    return most_common, ones, zeroes

#while index < len(inputs[0]):
res = oxygen_rating(inputs, index)
print(res)
