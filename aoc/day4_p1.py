grid = []
with open('test.txt') as file:
    contents = file.read()
    contents = contents.split()
    # print(len(contents.split()[1]))
    # for row in range(len(contents.split())):
    #     grid.append([])
    #     for col in range(len(contents.split()[1])):
    #         grid[row].append(contents[row + col])

dirs = [
    [-1, 0],
    [-1, +1],
    [0, +1],
    [+1, +1],
    [+1, 0],
    [-1, -1],
    [0, -1],
    [+1, -1],
]

print(contents[2][3])