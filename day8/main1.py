import re

lines = [x for x in open('data.txt', "r").read().split("\n") if x]
instructions = [0 if x == 'L' else 1 for x in lines[0][::]]

rules = {}
for line in lines[1:]:
    parts = re.findall(r'([A-Z]+)', line)
    rules[parts[0]] = (parts[1], parts[2])

counter = 0
current_node = 'AAA'
limit = len(instructions)
while True:
    current_node = rules[current_node][instructions[counter % limit]]
    if current_node == 'ZZZ':
        break
    counter += 1

print(counter + 1)
