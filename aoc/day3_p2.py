import re

#only most recent do or dont applies... hmmmm maybe search for dont dont pairs and do do pairs.
data = open('input.txt').read()
data = data.split('do()')
data = [seg.split("don't()")[0] for seg in data]
data_str = ''
for str in data:
    data_str += str
result = re.findall(r'mul\((.*?)\)', data_str)
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
