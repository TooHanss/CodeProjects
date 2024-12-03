import os
input = 'test.txt'

# map runs a function on an iterable
# in this case it is turning each item into an int
# the * is unpacking the map into a list. otherwise we just get a map object
data = [*map(int, open(input).read().split())]
print(data)

# Rather than doing modulus, we define A by getting every :: second 2 item in the list.
# We get B by doing the same but this time starting from index 1
A, B = (sorted(data[::2]), sorted(data[1::2]))

print(sum(map(lambda a, b: abs(a-b), A, B)))
print(sum(map(lambda a: a * B.count(a), A)))
# with open(input, 'r') as file:
#     contents = file.read() 
#     contents = contents.split(None)
#     list1 = []
#     list2 = []
#     for i, item in enumerate(contents):
#         if ((i+1)%2) == 0:
#             list2.append(item)
#         else:
#             list1.append(item)
#     list1.sort()
#     list2.sort()
#     dist = 0
#     for i, item in enumerate(list1):
#         dist += abs(int(item) - int(list2[i]))
#     print(dist)

