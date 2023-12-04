total = 0
for line in [x for x in open('data.txt', "r").read().split("\n") if x]:
    number_lists = line.split(':')[1]
    winning_numbers = [int(x) for x in number_lists.split('|')[0].strip().split(' ') if x]
    my_numbers = [int(x) for x in number_lists.split('|')[1].strip().split(' ') if x]
    winning_count = len(list(filter(lambda x: x in winning_numbers, my_numbers))) - 1
    if winning_count >= 0:
        total += pow(2, winning_count)
print(total)
