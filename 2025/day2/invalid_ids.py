cleaned = []

with open('inputs.txt', 'r') as id_nums:
    for line in id_nums:
        split_lst = line.strip().split(',')
        for item in split_lst:
            cleaned.append(item.split('-'))

    print(cleaned)

