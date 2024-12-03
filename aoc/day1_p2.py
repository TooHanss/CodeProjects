import os
input = 'input.txt'
with open(input, 'r') as file:
    contents = file.read() 
    contents = contents.split(None)
    list1 = []
    list2 = []
    for i, item in enumerate(contents):
        if ((i+1)%2) == 0:
            list2.append(int(item))
        else:
            list1.append(int(item))
    sim = 0
    for num in list1:
        sim += (list2.count(num) * num)


