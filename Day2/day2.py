horizontal = 0
depth = 0
aim = 0

with open('input.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip('\n') for line in lines]

for l in lines:
    num = int(l[-1])
    if 'forward' in l:
        horizontal += num
        depth += (aim*num)
    elif 'down' in l:
        aim += num
    else:
        aim -= num

#print(horizontal)
#print(depth)
print(horizontal*depth)
