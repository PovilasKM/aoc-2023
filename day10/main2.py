directions = {'|': [(0, -1), (0, 1)], '-': [(-1, 0), (1, 0)], 'L': [(0, -1), (1, 0)], 'J': [(-1, 0), (0, -1)],
              '7': [(0, 1), (-1, 0)], 'F': [(1, 0), (0, 1)]}
lines = [x for x in open('data.txt', "r").read().split("\n") if x]

# append the array
for x in range(len(lines)):
    lines[x] = '.' + lines[x] + '.'
lines.insert(0, '.' * len(lines[0]))
lines.append('.' * len(lines[0]))

# transform to [symbol, distance], e.g. ['S', 0], ['-', 1]
lines = [line[::] for line in lines]
for i, line in enumerate(lines):
    lines[i] = [[x, 0] for x in line]

# find S
starting_tile = ()
for y, line in enumerate(lines):
    for x, symbol in enumerate(line):
        if symbol[0] == 'S':
            starting_tile = (x, y)
            lines[y][x][1] = -1

next_step_coord = ()
# select the first tile after starting tile
# up
if lines[starting_tile[1] - 1][starting_tile[0]][0] in '|7F':
    next_step_coord = (starting_tile[0], starting_tile[1] - 1)
# down
elif lines[starting_tile[1] + 1][starting_tile[0]][0] in '|LJ':
    next_step_coord = (starting_tile[0], starting_tile[1] + 1)
# left
elif lines[starting_tile[1]][starting_tile[0] - 1][0] in '-LF':
    next_step_coord = (starting_tile[0] - 1, starting_tile[1])
# right
elif lines[starting_tile[1]][starting_tile[0] + 1][0] in '-J7':
    next_step_coord = (starting_tile[0] + 1, starting_tile[1])

# do the thing
steps = [starting_tile]
while True:
    # mark tile as passed
    lines[next_step_coord[1]][next_step_coord[0]][1] = -1
    next_step_symbol = lines[next_step_coord[1]][next_step_coord[0]][0]
    steps.append((next_step_coord[0], next_step_coord[1]))

    new_directions = directions[next_step_symbol]
    should_brake = True
    for new_direction in new_directions:
        next_tile = lines[next_step_coord[1] + new_direction[1]][next_step_coord[0] + new_direction[0]]
        if next_tile[1] == -1 or next_tile[0] == '.':
            continue
        next_step_coord = (next_step_coord[0] + new_direction[0], next_step_coord[1] + new_direction[1])
        should_brake = False
        break
    if should_brake:
        break

step_count = len(steps)
# https://en.wikipedia.org/wiki/Shoelace_formula surask plota
area = 0
steps.append(steps[0])
for i in range(0, len(steps) - 1):
    area += (steps[i][1] + steps[i + 1][1]) * (steps[i][0] - steps[i + 1][0]) * 0.5

area = abs(area)
# https://en.wikipedia.org/wiki/Pick%27s_theorem pagal plota ir taskus surask vidinius taskus
number_of_inner_points = area + 1 - (step_count / 2)
print(number_of_inner_points)

