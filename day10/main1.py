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

next_steps_coords = []
# find the initial starting tiles around S
# up
if lines[starting_tile[1] - 1][starting_tile[0]][0] in '|7F':
    next_steps_coords.append((starting_tile[0], starting_tile[1] - 1))
# down
if lines[starting_tile[1] + 1][starting_tile[0]][0] in '|LJ':
    next_steps_coords.append((starting_tile[0], starting_tile[1] + 1))
# left
if lines[starting_tile[1]][starting_tile[0] - 1][0] in '-LF':
    next_steps_coords.append((starting_tile[0] - 1, starting_tile[1]))
# right
if lines[starting_tile[1]][starting_tile[0] + 1][0] in '-J7':
    next_steps_coords.append((starting_tile[0] + 1, starting_tile[1]))


# do the thing
step = 0
while len(next_steps_coords) > 0:
    new_coords = []
    step += 1
    for next_step_coord in next_steps_coords:
        next_step = lines[next_step_coord[1]][next_step_coord[0]]
        if next_step[1] != 0 or next_step[0] == '.' or next_step[0] == 'S':
            continue

        new_directions = directions[next_step[0]]
        lines[next_step_coord[1]][next_step_coord[0]][1] = step
        for new_direction in new_directions:
            new_coords.append((next_step_coord[0] + new_direction[0], next_step_coord[1] + new_direction[1]))

    next_steps_coords = new_coords

print(max([tile[1] for line in lines for tile in line[:]]))
# for line in lines:
#     print([x[0] for x in line], end='\n')
# for line in lines:
#     print([x[1] for x in line], end='\n')
