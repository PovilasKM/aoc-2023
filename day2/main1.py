import re

red_limit = 12
green_limit = 13
blue_limit = 14
total = 0
for line in [x for x in open('data.txt', "r").read().split("\n") if x]:
    game_id = int(line.split(':')[0].split('Game ')[1])
    possible = True
    for part in line.split(':')[1].split(';'):
        colors = {'red': 0, 'green': 0, 'blue': 0}
        for num_col in part.split(','):
            groups = re.search('([0-9]+)\\s(red|blue|green)', num_col)
            colors[groups[2]] = colors[groups[2]] + int(groups[1])
            if colors['red'] > red_limit or colors['blue'] > blue_limit or colors['green'] > green_limit:
                possible = False
                break
    if possible:
        total += game_id
print(total)
