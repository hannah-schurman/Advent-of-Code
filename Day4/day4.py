import math

with open('input.txt') as file:
    call_nums = file.readline()
    lines = file.readlines()
    lines = lines[1:]

    call_nums = call_nums.split(",")
    call_nums = [c.rstrip("\n'") for c in call_nums]

    lines = [l.rstrip("\n") for l in lines]
    lines = [l for l in lines if l != ""]
    lines = [l.split() for l in lines]


num = 0
win_line = 0
win_num = 0
broken = False

for n in range(0, len(call_nums)-1):
    num = call_nums[n]
    for row in range(0, len(lines)):
        marked = 0
        for col in range(0, len(lines[row])):
            if lines[row][col] == num:
                lines[row][col] += "*"
            elif lines[row][col][-1] == "*":
                marked += 1
            if marked == 5:
                win_line = row
                broken = True
                win_num = call_nums[n-1]
                break
    if broken == True:
        break

# print(win_line) #the winning row
# print(win_num) #the winning num in call)_lines

win_board = win_line/5

place = win_line%5

matrix = []
if place == 4:
     matrix = lines[win_line-4:win_line+1]

s = 0
for m in matrix:
    for n in m:
        if n[-1] != "*":
            s+=int(n)

print(s*int(win_num))

