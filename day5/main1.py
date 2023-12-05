lines = [x for x in open('data.txt', "r").read().split("\n")]
seeds = [int(x) for x in lines[0].split(':')[1].split(' ') if x]

temp_seeds = []
i = 3
while i < len(lines):  # should be + 1 but last line is empty
    nums = [int(x) for x in lines[i].split(' ')]
    distance = nums[2]
    source_start = nums[1]
    destination_start = nums[0]

    for seed_i, seed in enumerate(seeds):
        if source_start <= seed <= (source_start + distance - 1):
            temp_seeds.append(seed + destination_start - source_start)
            seeds[seed_i] = 0

    seeds = list(filter(lambda x: x != 0, seeds))

    i += 1
    if not lines[i]:
        i += 2
        for seed in seeds:
            if seed != 0:
                temp_seeds.append(seed)
        seeds = temp_seeds.copy()
        temp_seeds = []

print(min(seeds))
