import numpy as np

inputs = []
segments = []
counter = 0
increases = 0
current = 157

with open('inputs.txt', 'r') as file:
    depths = file.readlines()

sliding_windows = np.convolve(depths, np.depths(3), 'valid')
print(sliding_windows)
