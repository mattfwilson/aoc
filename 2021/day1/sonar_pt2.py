inputs = []
segments = []
counter = 0
increases = 0
current = 157

with open('inputs.txt', 'r') as file:
    depths = file.readlines()

for index, depth in enumerate(depths):
    inputs.append(int(depth.strip()))
    try:
        total_seg = inputs[counter] + inputs[counter + 1] + inputs[counter + 2]
        segments.append(total_seg)
        counter += 1
    except IndexError:
        print('Except statement reached (IndexError: cannot sum next three indexes)')
    finally:
        print('Finally statement reached.')

for index, segment in enumerate(segments):
    if segment > current:
        current = segment
        increases += 1
        print(f'Index: {index} -- Segment {segment} UP')
    elif segment <= current:
        current = segment
        print(f'Index: {index} -- Segment {segment} DOWN')

print(f'\nList length: {len(inputs)}')
print(f'Counter: {counter}')
print(f'Increases: {increases}')
