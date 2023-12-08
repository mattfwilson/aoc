import re

strings = ['soweocltwone', '2sktwoclsk5jd4fzerone2s3kthreeight sldkf soup', 'nineightweroi s wero']

for i in strings:
    print(re.findall('sk', i))
    print(re.search('sk', i))

    print(re.findall('three', i))
    print(re.findall('\\bs\w+\\b', i))
    print(re.findall('\\bs\w*\\b', i))
