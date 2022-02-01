with open('input.txt') as file:
    fish = file.readline()
    fish = fish.split(',')
    fish = list(map(int, fish))

# for x in range(1,81):
#     for f in range(len(fish)):
#         if fish[f] == 0:
#             fish[f] = 6
#             fish.append(8)
#         else:
#             fish[f] -= 1
    #print('After {} days: {}'.format(x, fish))


#part 2

data = [fish.count(i) for i in range(0, 9)]

data.append(0)

for day in range(256):
    for index in range(len(data)):
        if index == 0 and data[index] != 0:
            data[7] += data[index]
            data[9] += data[index]
            data[0] = 0
        elif index != 0:
            if data[index] != 0:
                data[index - 1] += data[index]
                data[index] = 0 
        else:
            continue

print(sum(data))

