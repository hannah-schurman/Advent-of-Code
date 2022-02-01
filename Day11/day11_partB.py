with open('input.txt') as file:
    cavern = file.readlines()
    cavern = [line.strip() for line in cavern]

cave = []
for s in cavern:
    cave.append([int(x) for x in s])

total_octos = len(cave)*len(cave[0])

flashes = 0

def energy_gain(grid):
    flashed = []
    updated = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            updated = check_power(row, col, grid, flashed)
    return updated, flashed

def check_power(x, y, grid, flashed):
    global flashes
    if grid[x][y] != 0 or (x,y) not in flashed:
       grid[x][y] += 1

    if grid[x][y] > 9:
        flashes += 1
        grid[x][y] = 0
        flashed.append((x,y))
        if x+1 < len(grid[0]):
            check_power(x+1, y, grid, flashed)
        if x+1 < len(grid[0]) and y-1 >= 0:
            check_power(x+1, y-1, grid, flashed)
        if x+1 < len(grid[0]) and y+1 < len(grid):
            check_power(x+1, y+1, grid, flashed)

        if x-1 >= 0:
            check_power(x-1, y, grid, flashed)
        if x-1 >= 0 and y-1 >= 0:
            check_power(x-1, y-1, grid, flashed)
        if x-1 >= 0 and y+1 < len(grid):
            check_power(x-1, y+1, grid, flashed)

        if y+1 < len(grid):
            check_power(x, y+1, grid, flashed)
        if y-1 >= 0:
            check_power(x, y-1, grid, flashed)
    return grid


full = False
step = 0
while full != True:
    step += 1
    cave, flashed = energy_gain(cave)
    if len(flashed) == 100:
        full = True

for x in cave:
    print(x)

print(flashes)
print(step)