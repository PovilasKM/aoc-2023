from functools import cmp_to_key

powers = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 1, 'Q': 12, 'K': 13, 'A': 14}


def is_foak(hand):
    letters = set(hand)
    for letter in letters:
        if hand.count(letter) == 4:
            return True
    return False


def is_fh(hand):
    letters = set(hand)
    if len(letters) != 2:
        return False
    if {hand.count(letters.pop()), hand.count(letters.pop())} == {2, 3}:
        return True
    return False


def is_toak(hand):
    letters = set(hand)
    if len(letters) != 3:
        return False
    if {hand.count(letters.pop()), hand.count(letters.pop()), hand.count(letters.pop())} == {1, 3}:
        return True
    return False


def is_tp(hand):
    letters = set(hand)
    lens = []
    for letter in letters:
        lens.append(hand.count(letter))
    if lens == [1, 2, 2] or lens == [2, 1, 2] or lens == [2, 2, 1]:
        return True
    return False


def is_op(hand):
    letters = set(hand)
    if len(letters) != 4:
        return False
    lens = []
    for letter in letters:
        lens.append(hand.count(letter))
    if set(lens) == {1, 2}:
        return True
    return False


def power_hand(hand):
    # five of a kind
    if hand == len(hand) * hand[0]:
        return 7
    elif is_foak(hand):
        return 6
    elif is_fh(hand):
        return 5
    elif is_toak(hand):
        return 4
    elif is_tp(hand):
        return 3
    elif is_op(hand):
        return 2
    return 1


def power_sort(x, y):
    for i in range(0, len(x)):
        power_x = powers[x[i]]
        power_y = powers[y[i]]
        if power_x > power_y:
            return 1
        if power_x < power_y:
            return -1
    return 0


def strongest_power_hand(hand):
    if 'J' not in hand:
        return power_hand(hand)
    biggest = power_hand(hand)
    for key in powers.keys():
        power_with_replaced_J = power_hand(hand.replace('J', key))
        if power_with_replaced_J > biggest:
            biggest = power_with_replaced_J
    return biggest


def hand_sort(x, y):
    power_x = strongest_power_hand(x[0])
    power_y = strongest_power_hand(y[0])
    if power_x > power_y:
        return 1
    if power_x == power_y:
        return power_sort(x[0], y[0])
    return -1


hands = []
for line in [x for x in open('data.txt', "r").read().split("\n") if x]:
    hands.append((line.split(' ')[0], int(line.split(' ')[1])))

hands.sort(key=cmp_to_key(hand_sort))
total = 0
for i in range(0, len(hands)):
    total += (i + 1) * hands[i][1]
print(total)
