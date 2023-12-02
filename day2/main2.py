import re

total = 0
for line in [x for x in open('data.txt', "r").read().split("\n") if x]:
    game_id = int(line.split(':')[0].split('Game ')[1])
    colors_max = {'red': 0, 'green': 0, 'blue': 0}
    for part in line.split(':')[1].split(';'):
        colors = {'red': 0, 'green': 0, 'blue': 0}
        for num_col in part.split(','):
            groups = re.search('([0-9]+)\\s(red|blue|green)', num_col)
            colors[groups[2]] = colors[groups[2]] + int(groups[1])
        if colors['red'] > colors_max['red']:
            colors_max['red'] = colors['red']
        if colors['green'] > colors_max['green']:
            colors_max['green'] = colors['green']
        if colors['blue'] > colors_max['blue']:
            colors_max['blue'] = colors['blue']
    total += colors_max['red'] * colors_max['blue'] * colors_max['green']
print(total)
