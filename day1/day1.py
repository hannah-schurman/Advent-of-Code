with open('file.txt') as file:
    lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]

def find_num(lst):
    prev_num = lst[0]
    count = 0
    for next_num in lst[1:]:
        if next_num > prev_num:
            count += 1
        prev_num = next_num
    return count

    
cnt = find_num(lines) 
print(cnt)