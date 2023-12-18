lines = [x for x in open('data.txt', "r").read().split("\n") if x]
total = 0
for line in lines:
    numbers = [int(x) for x in line.split(' ')]
    next_num = 0
    while set(numbers) != {0}:
        next_num += numbers[-1]
        numbers = [current - previous for previous, current in zip(numbers, numbers[1:])]
    total += next_num
print(total)
