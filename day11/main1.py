lines = [x for x in open('data.txt', "r").read().split("\n") if x]

empty_rows = []
for i in range(0, len(lines)):
    if set([x for x in lines[i][:]]) == {'.'}:
        empty_rows.append(i)

empty_columns = []
for i in range(0, len(lines[0])):
    if set([x[i] for x in lines]) == {'.'}:
        empty_columns.append(i)

galaxies = []
for y in range(0, len(lines)):
    for x in range(0, len(lines[0])):
        if lines[y][x] == '#':
            galaxies.append((x, y))

total = 0
for i, start_galaxy in enumerate(galaxies[:-1]):
    for destination_galaxy in galaxies[i+1:]:
        x_base = abs(start_galaxy[0] - destination_galaxy[0])
        y_base = abs(start_galaxy[1] - destination_galaxy[1])
        base_distance = max(x_base + y_base, 1)
        x_empty_galaxies = len([x for x in empty_columns if min(start_galaxy[0], destination_galaxy[0]) < x < max(start_galaxy[0], destination_galaxy[0])])
        y_empty_galaxies = len([y for y in empty_rows if min(start_galaxy[1], destination_galaxy[1]) < y < max(start_galaxy[1], destination_galaxy[1])])
        total += base_distance + x_empty_galaxies + y_empty_galaxies

print(total)
