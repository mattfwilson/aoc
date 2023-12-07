import re

inputs = [line for line in open('inputs.txt').read().strip().split('\n')]
input_lst = [line for line in inputs]

str_nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
str_digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
combined_digits = { 'zerone': '01',
                    'twone': '21',
                    'threeight': '38',
                    'nineight': '98',
                    'eightwo': '82',
                    'eighthree': '83',
                    'sevenine': '79',
                    'fiveight': '58',
                    'oneight': '18'
                    }

string = '2sktwoclsk5jd4fzerone2s3kthreeight sldkf fw sower kfj sleep kfgdf weroi s wero'

print(re.findall('sk', string))
print(re.search('sk', string))

print(re.findall('three', string))
print(re.findall('\\bs\w+\\b', string))

print(combined_digits)
