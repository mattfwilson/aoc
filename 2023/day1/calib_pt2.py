inputs = [line for line in open('inputs.txt').read().strip().split('\n')]
inputs_lst = [line for line in inputs]

calibration_lst = []
str_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
spelled_digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def replace_spelled_digits(inputs_lst, calibration_lst, spelled_lst, str_digits):
    for line in inputs_lst:
        for i, word in enumerate(spelled_digits):
            if word in line:
                calibration_lst.append(line.replace(word, str_digits[i]))
            else:
                continue

replace_spelled_digits(inputs_lst, calibration_lst, spelled_digits, str_digits)

print(calibration_lst)
