#now need to find every X - MAS. do this by finding every A and sear it's diagonals for an M or S
#m s
# a
#m s
grid = []
with open(r'/Users/tomhanssens/Documents/GitHub/CodeProjects/aoc/input.txt') as file:
    contents = file.read()
    contents = contents.split()
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

def check_neighbor(origin):
    if origin[0] - 1 < 0 or origin[1] - 1 < 0:
        return False
    if origin[0] + 1 >= len(contents[0]) or origin[1] + 1 >= len(contents[0]):
        return False
    diag1 = False
    if contents[origin[0] - 1][origin[1] - 1] == 'M':
        if contents[origin[0] + 1][origin[1] + 1] == 'S':
            diag1 = True
    elif contents[origin[0] - 1][origin[1] - 1] == 'S':
        if contents[origin[0] + 1][origin[1] + 1] == 'M':
            diag1 = True
    diag2 = False
    if contents[origin[0] - 1][origin[1] + 1] == 'M':
        if contents[origin[0] + 1][origin[1] - 1] == 'S':
            diag2 = True
    elif contents[origin[0] - 1][origin[1] + 1] == 'S':
        if contents[origin[0] + 1][origin[1] - 1] == 'M':
            diag2 = True
    
    return diag1 and diag2 == True
    
num = 0
for row in range(len(contents)):
    for col in range(len(contents[0])):
        if contents[row][col] == 'A':
            print(f'found A at position {(row, col)}')
            if check_neighbor((row, col)):
                num += 1


print(num)