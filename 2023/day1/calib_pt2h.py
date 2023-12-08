import re

inputs = [line for line in open('inputs.txt').read().strip().split('\n')]
input_lst = [line for line in inputs]

str_nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
str_digits = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
replace_dict = {'twone': '21', 'threeight': '38', 'nineight': '98', 'eightwo': '82', 'eighthree': '83', 'sevenine': '79', 'fiveight': '58', 'oneight': '18'}

string = ['2sktwoclsk5jd4fzerone2s3kthreeight', 'oneight']
output_lst = []
output_lst2 = []
pair_lst = []
calibration_lst = []

def replace_multiple_strs(string, replacements, append_lst):
    for i in string:
        pattern = re.compile('|'.join(re.escape(key) for key in replacements.keys()))
        append_lst.append(pattern.sub(lambda x: replacements[x.group()], i))

output_lst.append(replace_multiple_strs(input_lst, replace_dict, output_lst))
output_lst.pop(-1)

output_lst2.append(replace_multiple_strs(output_lst, str_digits, output_lst2))
output_lst2.pop(-1)
print(output_lst2)

for line in output_lst2:
    pair_lst.append([char for char in line if char in str_nums])
print(pair_lst)

for line in pair_lst:
    calibration_lst.append(int(line[0] + line[-1]))
print(calibration_lst)

print(sum(calibration_lst))
