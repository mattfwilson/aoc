inputs = [line for line in open('inputs.txt').read().strip().split('\n')]
input_lst = [line for line in inputs]
output_lst = []
stripped_digits = []
calibration = []

digits_dict = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

def first_last(inputs, digit_dict):
    for line in inputs:
        for key, val in digits_dict.items():
            if val in line:
                line = line.replace(key, digits_dict[key])
                StopIteration
    
    for line in reversed(inputs):
        for key, val in digits_dict.items():
            if val in line:
                line = line.replace(key, digits_dict[key])
                StopIteration
    
    return inputs

output_lst = first_last(input_lst, digits_dict)

for line in output_lst:
    stripped_digits.append([char for char in line if char in digits_dict.values()])

for line in stripped_digits:
    calibration.append(int(line[0] + line[-1]))

print(calibration)
print(f'Calibraton Sum: {sum(calibration)}')
