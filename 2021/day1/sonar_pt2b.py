with open('inputs.txt', 'r') as file:
    depths = [int(item) for item in file.read().strip().split('\n')]

print(depths)

def calc_increases():
    segments = [sum(seg_tup) for seg_tup in zip(depths, depths[1:], depths[2:])]
    result = [sum1 < sum2 for sum1, sum2 in zip(segments, segments[1:])] 
    return sum(result)

print('Segment increases = ', calc_increases())
