with open('input.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

l = len(lines[0])

gamma = ""
epsilon = ""

###PART 1

for step in range(0, l):
    num_zero = 0
    num_one = 0

    for line in lines:
        if int(line[step]) == 0:
            num_zero += 1
        else:
            num_one += 1
    
    if num_zero >= num_one:
        gamma += str(0)
        epsilon += str(1)

    else:
        gamma += str(1)
        epsilon += str(0)

total = (int(gamma, 2)) * (int(epsilon, 2))
print(total)

### PART 2

oxy_rating = ""
line_oxy = lines
line_co2 = lines
for step in range(0, l):
    num_zero = 0
    num_one = 0

    for line in line_oxy:
        if int(line[step]) == 0:
            num_zero += 1
        else:
            num_one += 1
    
    if len(line_oxy) == 1:
        break

    if num_one > num_zero:
        line_oxy = [x for x in line_oxy if x[step] == "1"]
    elif num_one == num_zero:
        line_oxy = [x for x in line_oxy if x[step] == "1"]
    else:
        line_oxy = [x for x in line_oxy if x[step] == "0"]



for step in range(0, l):
    num_zero = 0
    num_one = 0

    for line in line_co2:
        if int(line[step]) == 0:
            num_zero += 1
        else:
            num_one += 1
    
    if len(line_co2) == 1:
        break

    if num_one > num_zero:
        line_co2 = [x for x in line_co2 if x[step] == "0"]
    elif num_one == num_zero:
        line_co2 = [x for x in line_co2 if x[step] == "0"]
    else:
        line_co2 = [x for x in line_co2 if x[step] == "1"]


# print(line_oxy)
# print(line_co2)


total_2 = (int(line_oxy[0], 2)) * (int(line_co2[0], 2))
print(total_2)