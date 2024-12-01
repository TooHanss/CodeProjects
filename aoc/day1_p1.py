import os
input = 'input.txt'
with open(input, 'r') as file:
    contents = file.read() 
    contents = contents.split(None)
    list1 = []
    list2 = []
    for i, item in enumerate(contents):
        if ((i+1)%2) == 0:
            list2.append(item)
        else:
            list1.append(item)
    list1.sort()
    list2.sort()
    dist = 0
    for i, item in enumerate(list1):
        dist += abs(int(item) - int(list2[i]))
    print(dist)

