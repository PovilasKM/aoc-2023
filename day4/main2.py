cards = {}  # card1: [winning_count, card_count]
for i, line in enumerate([x for x in open('data.txt', "r").read().split("\n") if x]):
    number_lists = line.split(':')[1]
    winning_numbers = [int(x) for x in number_lists.split('|')[0].strip().split(' ') if x]
    my_numbers = [int(x) for x in number_lists.split('|')[1].strip().split(' ') if x]
    winning_count = len(list(filter(lambda x: x in winning_numbers, my_numbers)))
    cards[i + 1] = [winning_count, 1]

for key, current_card in cards.items():
    winning_count = current_card[0]
    current_card_count = current_card[1]
    for i in range(1, winning_count + 1):
        if key + i in cards.keys():
            cards[key + i][1] += current_card_count

print(sum([x[1] for x in cards.values()]))
