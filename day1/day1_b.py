
with open('input.txt') as file:
    lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]

prev_sum = 0
count = 0
for num in range(0, len(lines) - 2):
    sum_three = sum(lines[num:num+3])
    if sum_three > prev_sum:
        count += 1
    
    prev_sum = sum_three

print(count-1)
