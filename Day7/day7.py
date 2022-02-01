with open('input.txt') as file:
    crab = file.readline()
    crab = crab.split(',')
    crab = list(map(int, crab))


max_h = max(crab)
min_h = min(crab)

min_fuel = 100000000000

#Part 1
# for pos in range(min_h, max_h):
#     total_fuel = 0
#     for c in crab:
#         fuel = abs(c-pos)
#         total_fuel += fuel
#     if total_fuel < min_fuel:
#         min_fuel = total_fuel

#print(min_fuel)



#Part 2
for pos in range(min_h, max_h):
    total_fuel = 0
    for c in crab:
        n = abs(c-pos)
        fuel = (n*(n+1))/2
        total_fuel += fuel
    if total_fuel < min_fuel:
        min_fuel = total_fuel


print(min_fuel)