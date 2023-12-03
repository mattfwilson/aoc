inputs = [line for line in open('inputs.txt').read().strip().split('\n')]
inputs_lst = [line for line in inputs]

str_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
stripped_digits = []
calibration_lst = []

for line in inputs_lst:
    stripped_digits.append([char for char in line if char in str_digits])

for line in stripped_digits:
    if len(line) > 1:
        calibration_lst.append(int(line[0] + line[-1]))
    else:
        continue # do we add single digit inputs to the sum?

print(calibration_lst)
print(sum(calibration_lst))
