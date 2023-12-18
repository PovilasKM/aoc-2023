import re
from math import lcm

lines = [x for x in open('data.txt', "r").read().split("\n") if x]
instructions = [0 if x == 'L' else 1 for x in lines[0][::]]
current_nodes = []
rules = {}
for line in lines[1:]:
    parts = re.findall(r'([A-Z1-9]+)', line)
    rules[parts[0]] = (parts[1], parts[2])
    if parts[0][2] == 'A':
        current_nodes.append(parts[0])

counter = 0
limit = len(instructions)
z_indexes = []
while len(current_nodes) > 0:
    for i, current_node in enumerate(current_nodes):
        current_nodes[i] = rules[current_node][instructions[counter % limit]]
        if current_nodes[i][2] == 'Z':
            z_indexes.append(counter + 1)
    current_nodes = list(filter(lambda x: x[2] != 'Z', current_nodes))
    counter += 1

print(lcm(*z_indexes))
