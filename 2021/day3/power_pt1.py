digits = []
gamma_lst = []
epsilon_lst = []
counter = 0

inputs = [line for line in open('inputs.txt').read().strip().split('\n')]

def to_decimal(binary_string):
    decimal = 0
    power = len(binary_string) - 1

    for digit in binary_string:
        if digit == '1':
            decimal += 2 ** power
        power -= 1

    return decimal

while counter < len(inputs[0]):
    for binary in inputs:
        digits.append(binary[counter])
    zeroes = digits.count('0')
    ones = digits.count('1')
    print(f'Zeroes: {zeroes} | Ones: {ones}')
    
    if zeroes > ones:
        gamma_lst.append('0')
        epsilon_lst.append('1')
    else:
        gamma_lst.append('1')
        epsilon_lst.append('0')
    counter += 1

gamma_binary = ''.join(gamma_lst)
print(f'Gamma binary: {gamma_binary} | Length: {len(gamma_binary)} {type(gamma_binary)}')

epsilon_binary = ''.join(epsilon_lst)
print(f'Epsilon binary: {epsilon_binary} | Length: {len(epsilon_binary)} {type(epsilon_binary)}')

gamma_decimal = to_decimal(gamma_binary)
epsilon_decimal = to_decimal(epsilon_binary)
print(f'Gamma rate: {gamma_decimal}')
print(f'Epsilon rate: {epsilon_decimal}')

power = gamma_decimal * epsilon_decimal
print(f'Power: {power}')

