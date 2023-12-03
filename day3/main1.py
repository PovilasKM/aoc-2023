def do_surroundings_contain_symbol(lines, x, y):
    symbols = [lines[y - 1][x - 1], lines[y - 1][x], lines[y - 1][x + 1],
               lines[y][x - 1], lines[y][x + 1],
               lines[y + 1][x - 1], lines[y + 1][x], lines[y + 1][x + 1]]
    non_num_symbols = list(filter(lambda a: (not a.isdigit()) and (a != '.'), symbols))
    return len(non_num_symbols) > 0


total = 0
lines = [x for x in open('data.txt', "r").read().split("\n") if x]

# append the array
for x in range(len(lines)):
    lines[x] = '.' + lines[x] + '.'
lines.insert(0, '.' * len(lines[0]))
lines.append('.' * len(lines[0]))

for y, line in enumerate(lines[1:len(lines) - 1]):
    num = ''
    is_part_number = False
    for x in range(1, len(line)):
        symbol = line[x]
        if symbol.isdigit():
            num += symbol
            if do_surroundings_contain_symbol(lines, x, y+1):
                is_part_number = True
        else:  # not a number
            if num.isdigit() and is_part_number:  # if previous symbol was a number and the whole thing touched a symbol
                # print(num)
                total += int(num)
            num = ''
            is_part_number = False

print(total)
