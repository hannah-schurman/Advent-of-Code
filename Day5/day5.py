import numpy as np

#read in input and store in list of list of tuples
with open('input.txt') as file:
    lines = file.readlines()
    lines = [l.rstrip() for l in lines]
    lines = [l.split(' -> ') for l in lines]

for x in range(len(lines)):
    for y in range(2):
            lines[x][y] = tuple(map(int, lines[x][y].split(",")))
            
smallest_x = smallest_y = 10000
largest_x = largest_y = 0

#find boundary for grid
for l in lines:
    for tuple in l:
        largest_x = max(tuple[0], largest_x)
        largest_y = max(tuple[1], largest_y)
        smallest_x = min(tuple[0], smallest_x)
        smallest_y = min(tuple[1], smallest_y)

grid = np.zeros((largest_x+2, largest_y+2))

#iterate through tuples and add lines between the two points
for l in lines:
    start_x = l[0][0]
    start_y = l[0][1]
    finish_x = l[1][0]
    finish_y = l[1][1]

    diff_x = np.abs(start_x - finish_x)
    diff_y = np.abs(start_y - finish_y)

    #part 1
    if diff_x == 0: #add y values
        m = min(start_y, finish_y)
        for n in range(diff_y-1):
            l.append((start_x,m+(n+1)))
    elif diff_y == 0: #add x values
        m = min(start_x, finish_x)
        for n in range(diff_x-1):
            l.append((m+(n+1), start_y))
    
    #part 2
    elif diff_x == diff_y: #part2
        min_tup = min(l)
        max_tup = max(l)
        min_x = min_tup[0]
        min_y = min_tup[1]

        max_x = max_tup[0]
        max_y = max_tup[1]

        if min_x < max_x and min_y < max_y:
            for n in range(diff_x-1):
                l.append((min_x+(n+1), min_y+(n+1)))
        elif min_x < max_x and min_y > max_y:
            for n in range(diff_x-1):
                l.append((min_x+(n+1), min_y-(n+1)))
        elif min_x > max_x and min_y < max_y:
            for n in range(diff_x-1):
                l.append((min_x-(n+1), min_y+(n+1)))

#update grid
for l in lines:
    if len(l) > 2:
        for t in l:
            r = t[1]
            c = t[0]
            grid[r][c] += 1

#count number of grids 2 or more
count = 0
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] >= 2:
            count += 1

print(count+1)