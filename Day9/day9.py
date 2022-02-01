with open('test.txt') as file:
    map = file.readlines()
    map = [list(m.strip()) for m in map]
    map = [[int(x) for x in l] for l in map]


low_points = []
for row in range(len(map)):
    for col in range(len(map[row])):
        x = map[row][col]
        # the following lines test if it is an edge
        if row == 0 and col == 0:
            surr = [x, map[row][col+1], map[row+1][col]]
            surr.sort()
            if x == surr[0] and x != surr[1]:
                low_points.append(x)
        elif row == 0 and col != 0 and col != len(map[0])-1:
            surr = [x, map[row][col+1], map[row+1][col], map[row][col-1]]
            surr.sort()
            if x == surr[0] and x != surr[1]:
                low_points.append(x)
        elif row == len(map)-1 and col == 0:
            surr = [x, map[row][col+1], map[row-1][col]]
            surr.sort()
            if x == surr[0] and x != surr[1]:
                low_points.append(x)
        elif row == len(map)-1 and col != 0 and col != len(map[0])-1:
            surr = [x, map[row][col+1], map[row][col-1], map[row-1][col]]
            surr.sort()
            if x == surr[0] and x != surr[1]:
                low_points.append(x)
        elif col == 0 and row != 0 and row != len(map)-1:
            surr = [x, map[row][col+1], map[row+1][col], map[row-1][col]]
            surr.sort()
            if x == surr[0] and x != surr[1]:
                low_points.append(x)
        elif col == len(map[0])-1 and row == 0:
            surr = [x, map[row][col-1], map[row-1][col]]
            surr.sort()
            if x == surr[0] and x != surr[1]:
                low_points.append(x)
        elif col == len(map[0])-1 and row == len(map)-1:
            surr = [x, map[row][col-1], map[row-1][col]]
            surr.sort()
            if x == surr[0] and x != surr[1]:
                low_points.append(x)
        elif col == len(map[0])-1 and row != len(map)-1 and row != 0:
            surr = [x, map[row][col-1], map[row-1][col], map[row+1][col]]
            surr.sort()
            if x == surr[0] and x != surr[1]:
                low_points.append(x)
        elif col != 0 and row != 0 and row != len(map)-1 and col != len(map[0])-1:
            surr = [x, map[row][col-1], map[row][col+1], map[row+1][col], map[row-1][col]]
            surr.sort()
            if x == surr[0] and x != surr[1]:
                low_points.append(x)

print(sum(low_points)+len(low_points))


print(low_points)