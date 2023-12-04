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

def replace_digits(input_lst, output_lst, digits_dict):
    for line in input_lst:
        for key, val in digits_dict.items():
            while key in line:
                line = line.replace(key, digits_dict[key])
        output_lst.append(line)

replace_digits(input_lst, output_lst, digits_dict)

for line in output_lst:
    stripped_digits.append([char for char in line if char in digits_dict.values()])

for line in stripped_digits:
    calibration.append(int(line[0] + line[-1]))

print(calibration)
print(f'Sum: {sum(calibration)}')
