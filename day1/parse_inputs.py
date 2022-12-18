import os
print(os.getcwd())

parsed = [lambda :item.strip() for item in open('inputs.txt').readlines()]
print(parsed)