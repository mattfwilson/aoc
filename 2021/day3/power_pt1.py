digits = []
gamma_lst = []
epsilon_lst = []
index = 0

inputs = [line for line in open('inputs.txt').read().strip().split('\n')]

def to_decimal(binary_string):
    decimal = 0
    power = len(binary_string) - 1

    for digit in binary_string:
        if digit == '1':
            decimal += 2 ** power
        power -= 1

    return decimal

while index < len(inputs[0]):
    for binary in inputs:
        digits.append(binary[index])
    zeroes = digits.count('0')
    ones = digits.count('1')
