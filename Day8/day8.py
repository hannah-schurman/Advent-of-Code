with open('input.txt') as file:
    output = file.readlines()

output = [[["".join(sorted(z)) for z in y.split()] for y in x.split(" | ")] for x in output]


def find_digits(key):
    four = [x for x in key if len(x) == 4][0]
    one = [x for x in key if len(x) == 2][0]
    seven = [x for x in key if len(x) == 3][0]
    eight = [x for x in key if len(x) == 7][0]
    nine = [x for x in key if len(x) == 6 and all(y in x for y in four)][0]
    three = [x for x in key if len(x) == 5 and all(y in x for y in seven)][0]
    zero = [x for x in key if len(x) == 6 and all(y in x for y in seven) and not all(y in x for y in four)][0]
    six = [x for x in key if len(x) == 6 and not all(y in x for y in nine) and not all(y in x for y in zero)][0]
    five = [x for x in key if len(x) == 5 and all(y in six for y in x)][0]
    two = [x for x in key if len(x) == 5 and not all(y in x for y in five) and not all(y in x for y in three)][0]
    return list((zero, one, two, three, four, five, six, seven, eight, nine))


digit_list = []

for key, dig in output:
    numbers = find_digits(key)
    num_list = []
    for d in dig:
        digit = str(numbers.index(d))
        num_list.append(digit)
    digit_list.append(int("".join(num_list)))

print(sum(digit_list))


