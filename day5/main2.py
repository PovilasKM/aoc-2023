lines = [x for x in open('data.txt', "r").read().split("\n")]
seeds = [int(x) for x in lines[0].split(':')[1].split(' ') if x]

seed_intervals = []
minimums = []
for i in range(0, len(seeds), 2):
    seed_intervals.append([seeds[i], seeds[i] + seeds[i + 1] - 1, 0])
    # [from, to, change] all including
    # change: -1: used, 0: unused, 1: new

for seed_interval in seed_intervals:
    intervals = [seed_interval]
    i = 3
    while i < len(lines):
        # print('intervals: ', intervals)
        nums = [int(x) for x in lines[i].split(' ')]
        distance = nums[2] - 1
        source_start = nums[1]
        source_end = source_start + distance
        destination_start = nums[0]
        destination_end = destination_start + distance
        change = destination_start - source_start

        for interval in [x for x in intervals if x[2] == 0]:  # only use intervals that are marked as unused (0)
            #     source(map/rule) covers the interval
            if interval[0] >= source_start and interval[1] <= source_end:
                intervals.append([interval[0] + change, interval[1] + change, 1])
                interval[2] = -1  # mark interval as used and up for removal

            #     source(map/rule) is covered by the interval
            elif interval[0] < source_start and interval[1] > source_end:
                intervals.append([interval[0], source_start - 1, 0])
                intervals.append([source_start + change, source_end + change, 1])
                intervals.append([source_end + 1, interval[1], 0])
                interval[2] = -1  # mark interval as used and up for removal

            #    sources(map/rule) covers the interval from the left
            elif (source_start < interval[0] <= source_end) and interval[1] > source_end:
                intervals.append([interval[0] + change, source_end + change, 1])
                intervals.append([source_end + 1, interval[1], 0])
                interval[2] = -1  # mark interval as used and up for removal

            #    source(map/rule) covers the interval from the right
            elif (interval[0] <= source_start < interval[1]) and interval[1] < source_end:
                intervals.append([interval[0], source_start - 1, 0])
                intervals.append([source_start + change, interval[1] + change, 1])
                interval[2] = -1  # mark interval as used and up for removal

            #     source(map/rule) is covered by the interval, end matches
            elif interval[0] < source_start and interval[1] == source_end:
                intervals.append([interval[0], source_start - 1, 0])
                intervals.append([source_start + change, source_end + change, 1])
                interval[2] = -1  # mark interval as used and up for removal

            # source(map/rule) is covered by the interval, start matches
            elif interval[0] == source_start and interval[1] > source_end:
                intervals.append([source_start + change, source_end + change, 1])
                intervals.append([source_end + 1, interval[1], 0])
                interval[2] = -1  # mark interval as used and up for removal

        i += 1
        if not lines[i]:  # empty line -> next rules/maps block is starting, perform a cleanup
            i += 2
            intervals = list(filter(lambda x: x[2] != -1, intervals))  # remove intervals that have been used
            for interval in intervals:
                interval[2] = 0

    minimums.append(min([x[0] for x in intervals]))
print(min(minimums))
