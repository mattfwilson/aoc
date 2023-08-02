digits = []
oxygen_lst = []
co2_lst = []
index = 0

inputs = [line for line in open('inputs.txt').read().strip().split('\n')]

while index < len(inputs[0]):
    for binary in inputs:
        digits.append(binary[index])
    zeroes = digits.count('0')
    ones = digits.count('1')

    greater_val = 0
    if zeroes > ones:
        greater_val = 0
    else:
        greater_val = 1

    for binary in inputs:
        if binary[index] == greater_val:
            oxygen_lst.append(binary[index])

print(len(oxygen_lst))
print(oxygen_lst)
            
