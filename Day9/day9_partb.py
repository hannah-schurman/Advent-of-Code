with open('input.txt') as file:
    matrix = file.readlines()
    matrix = [list(m.strip()) for m in matrix]
    matrix = [[int(x) for x in l] for l in matrix]


def find_low(map):
    low_points = []
    low_locations = []
    for row in range(len(map)):
        for col in range(len(map[row])):
            x = map[row][col]
            # the following lines test if it is an edge
            if row == 0 and col == 0:
                surr = [x, map[row][col+1], map[row+1][col]]
                surr.sort()
                if x == surr[0] and x != surr[1]:
                    low_points.append(x)
                    low_locations.append([row, col])
            elif row == 0 and col != 0 and col != len(map[0])-1:
                surr = [x, map[row][col+1], map[row+1][col], map[row][col-1]]
                surr.sort()
                if x == surr[0] and x != surr[1]:
                    low_points.append(x)
                    low_locations.append([row, col])
            elif row == len(map)-1 and col == 0:
                surr = [x, map[row][col+1], map[row-1][col]]
                surr.sort()
                if x == surr[0] and x != surr[1]:
                    low_points.append(x)
                    low_locations.append([row, col])
            elif row == len(map)-1 and col != 0 and col != len(map[0])-1:
                surr = [x, map[row][col+1], map[row][col-1], map[row-1][col]]
                surr.sort()
                if x == surr[0] and x != surr[1]:
                    low_points.append(x)
                    low_locations.append([row, col])
            elif col == 0 and row != 0 and row != len(map)-1:
                surr = [x, map[row][col+1], map[row+1][col], map[row-1][col]]
                surr.sort()
                if x == surr[0] and x != surr[1]:
                    low_points.append(x)
                    low_locations.append([row, col])
            elif col == len(map[0])-1 and row == 0:
                surr = [x, map[row][col-1], map[row-1][col]]
                surr.sort()
                if x == surr[0] and x != surr[1]:
                    low_points.append(x)
                    low_locations.append([row, col])
            elif col == len(map[0])-1 and row == len(map)-1:
                surr = [x, map[row][col-1], map[row-1][col]]
                surr.sort()
                if x == surr[0] and x != surr[1]:
                    low_points.append(x)
                    low_locations.append([row, col])
            elif col == len(map[0])-1 and row != len(map)-1 and row != 0:
                surr = [x, map[row][col-1], map[row-1][col], map[row+1][col]]
                surr.sort()
                if x == surr[0] and x != surr[1]:
                    low_points.append(x)
                    low_locations.append([row, col])
            elif col != 0 and row != 0 and row != len(map)-1 and col != len(map[0])-1:
                surr = [x, map[row][col-1], map[row][col+1], map[row+1][col], map[row-1][col]]
                surr.sort()
                if x == surr[0] and x != surr[1]:
                    low_points.append(x)
                    low_locations.append([row, col])
    return low_points, low_locations

def find_basins(locations, map):
    basin_sizes = []
    for row, col in locations:
        basin_sizes.append(basin_point(row, col, map))
    return basin_sizes

def basin_point(x, y, map):
    size = 0
    if (map[x][y] == 9) or (map[x][y] == "*"):
        return size
    map[x][y] = "*"
    size += 1
    if y+1 < len(map[0]):
        size += basin_point(x, y+1, map)
    if y-1 >= 0:
        size += basin_point(x, y-1, map)
    if x+1 < len(map):
        size += basin_point(x+1, y, map)
    if x-1 >= 0:
        size += basin_point(x-1, y, map)
    
    return size

lows = find_low(matrix)
basins = sorted(find_basins(lows[1], matrix))
print(lows)

print(basins)

print(basins[-1] * basins[-2] * basins[-3])