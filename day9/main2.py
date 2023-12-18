def get_diffs(numbers):
    new_numbers = [current - previous for previous, current in zip(numbers, numbers[1:])]
    if set(numbers) == {0}:
        return numbers[0] - new_numbers[0]
    else:
        return numbers[0] - get_diffs(new_numbers)


lines = [x for x in open('data.txt', "r").read().split("\n") if x]
total = 0

for line in lines:
    numbers = [int(x) for x in line.split(' ')]
    total += get_diffs(numbers)
print(total)
