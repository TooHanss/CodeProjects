grid = []
with open(r'/Users/tomhanssens/Documents/GitHub/CodeProjects/aoc/input.txt') as file:
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

def check_neighbor(origin, dir):
    if origin[0] + dir [0] < 0 or origin[1] + dir[1] < 0:
        return None
    if origin[0] + dir [0] >= len(contents[0]) or origin[1] + dir[1] >= len(contents[0]):
        return None
    return contents[origin[0] + dir[0]][origin[1] + dir[1]]
    
num = 0
for row in range(len(contents)):
    for col in range(len(contents[0])):
        if contents[row][col] == 'X':
            print(f'found X at position {(row, col)}')
            for dir in dirs: 
                if check_neighbor((row, col), (dir[0], dir[1])) == 'M':
                    print('found M')
                    if check_neighbor((row + dir[0], col + dir[1]), (dir[0], dir[1])) == 'A':
                        print('found A')
                        if check_neighbor((row + dir[0] + dir[0], col + dir[1] + dir[1]), (dir[0], dir[1])) == 'S':
                            print('Found S')
                            num += 1


print(num)