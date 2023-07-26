with open('inputs.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
    stripped = [item.replace('\n', '') for item in lines]
    print(stripped)
    data_dict = {key_value.split(' ')[0]: key_value.split(' ')[1] for key_value in stripped}
    print(data_dict)
