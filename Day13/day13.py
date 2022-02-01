with open('input.txt') as file:
    inst = file.readlines()

marks = [line.strip().split(',') for line in inst if 'fold' not in line][:-1]
marks = [(int(x), int(y)) for [x, y] in marks]

folds = [(line.strip().split('=')[0][-1], int(line.strip().split('=')[1])) for line in inst if '=' in line]

x_max = max(marks, key = lambda t: t[0])[0]+1
y_max = max(marks, key = lambda t: t[1])[1]+1

grid = [['.'] * x_max for _ in range(y_max)]
for x,y in marks:
    grid[y][x] = '#'


# folds
split = 0
for f, n in folds:

    if f == 'y': 
        grid_split = grid[n+1:][::-1]
        grid = grid[:n]

        if len(grid_split) > len(grid):
            grid = [["."] * len(grid_split[0])] * (len(grid_split) - len(grid)) + grid
        elif len(grid) > len(grid_split):
            grid_split = [["."] * len(grid[0])] * (len(grid) - len(grid_split)) + grid_split

    if f == 'x':           
        grid_split = [x[n+1:][::-1] for x in grid]
        grid = [x[:n] for x in grid]

        if len(grid_split[0]) > len(grid[0]):
            grid = [["."] * len(grid_split[0]) - len(grid[0]) + grid for x in grid]
        elif len(grid) > len(grid_split):
            grid_split = [["."] * len(grid[0]) - len(grid_split[0]) + grid_split for x in grid_split]
    
    for i in range(len(grid)): 
        for j in range(len(grid[0])): 
            if grid_split[i][j] == '#':
                grid[i][j] = '#'
    split += 1
    if split == 1: 
        print(f"Part1: {[sum(line.count('#') for line in grid)][0]}")   


for line in grid:
        print("".join([' ' if x == "." else "#" for x in line]))

