from functools import reduce

lines = [x for x in open('data.txt', "r").read().split("\n") if x]
time = int(lines[0].split(':')[1].replace(' ', ''))
distance = int(lines[1].split(':')[1].replace(' ', ''))
ways_to_bear_the_record = 0

for time_waited in range(1, time):
    speed = time_waited
    remaining_time = time - time_waited
    if speed * remaining_time > distance:
        ways_to_bear_the_record += 1

print(ways_to_bear_the_record)
