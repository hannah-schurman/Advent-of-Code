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

boards = [lines[l:l+5] for l in range(0, len(lines), 5)]



call = 0
win_boards = {}
called = set()
for ball in range(0, len(call_nums)): #0-100
    num = call_nums[ball] #get number on ball 
    for board in range(0,len(boards)): #0-100
        if board in win_boards: #if board has already won, skip board
            continue
        called.add(num)
        board_won = False #initiate board winning 
        last_board = board
        #iterate through rows
        for row in range(len(boards[board])): 
            marked = 0 #initiate marked
            for col in range(len(boards[board][row])): #go through columns
                if boards[board][row][col] == num: #if not and matches num, mark it
                    boards[board][row][col] = 'X'
                if boards[board][row][col] == 'X': #if item is marked add 1 to marked
                    marked += 1
                if marked == 5: #if row is full of X's
                    #board is marked as winner
                    win_boards[board] = 'X'
                    board_won = True
                    break
            if board_won:
                break
        
        if board_won:
            continue

        #iterate through vertically
        for col in range(len(boards[board])): #if not already won, go through rows
            marked = 0 #initiate marked
            for row in range(len(boards[board][col])): #go through columns
                if boards[board][row][col] == 'X': #if row/col is marked add 1 to marked
                    marked += 1
                if marked == 5: #if row is full of X's
                    #board is marked as winner
                    win_boards[board] = 'X'
                    board_won = True
                    break
            if board_won:
                break
                


sum_left = 0
for r in range(0, len(boards[last_board])):
    for c in range(0, len(boards[last_board][r])):
        if boards[last_board][r][c] != "X":
            sum_left += int(boards[last_board][r][c])

unmarked = int(call_nums[len(called)-1])

print(sum_left* unmarked)


