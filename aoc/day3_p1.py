import re
data = open('test.txt').read()
result = re.findall(r'mul\((.*?)\)', data)
pairs = []
for pair in result:
    if 'mul(' in pair:
        pair = pair.split('mul(')[1]
    if ',' not in pair:
        continue
    try:
        pairs.append([*map(int, pair.split(','))])
    except:
        continue
for pair in pairs:
    print(pair)    
print(sum([pair[0] * pair[1] for pair in pairs]))


