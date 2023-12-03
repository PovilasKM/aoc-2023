def get_surrounding_gears(lines, x, y):
    surrounding_points = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                          (x - 1, y), (x + 1, y),
                          (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]
    return list(filter(lambda a: lines[a[1]][a[0]] == '*', surrounding_points))


total = 0
lines = [x for x in open('data.txt', "r").read().split("\n") if x]

# append the array
for x in range(len(lines)):
    lines[x] = '.' + lines[x] + '.'
lines.insert(0, '.' * len(lines[0]))
lines.append('.' * len(lines[0]))

gears = {}
for y, line in enumerate(lines[1:len(lines) - 1]):
    num = ''
    temp_gears = set()
    for x in range(1, len(line)):
        symbol = line[x]
        if symbol.isdigit():
            num += symbol
            temp_gears.update(get_surrounding_gears(lines, x, y + 1))
        elif num.isdigit():  # not a number
            for temp_gear in temp_gears:
                if temp_gear not in gears.keys():
                    gears[temp_gear] = []
                gears[temp_gear].append(int(num))
            num = ''
            temp_gears = set()

for value in gears.values():
    if len(value) == 2:
        total += value[0] * value[1]

print(total)
