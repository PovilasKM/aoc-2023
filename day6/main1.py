from functools import reduce

lines = [x for x in open('data.txt', "r").read().split("\n") if x]
times = [int(x) for x in lines[0].split(':')[1].split(' ') if x.isdigit()]
distances = [int(x) for x in lines[1].split(':')[1].split(' ') if x.isdigit()]
races = list(zip(times, distances))
ways_to_bear_the_record = [0 for x in times]

for i, race in enumerate(races):
    for time_waited in range(1, race[0]):
        speed = time_waited
        remaining_time = race[0] - time_waited
        target_distance = race[1]
        if speed * remaining_time > target_distance:
            ways_to_bear_the_record[i] += 1

print(reduce(lambda x, y: x*y, ways_to_bear_the_record))
