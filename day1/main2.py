num_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
lines = open('data.txt', "r").read().split("\n")
total = 0
for line in [x for x in lines if x]:
    first = 0
    last = 0
    acc = ''
    for letter in line:
        acc += letter
        if letter.isdigit():
            first = int(letter)
            break
        for key in num_dict.keys():
            if key in acc:
                first = num_dict[key]
                break
        else:
            continue
        break

    acc = ''
    for letter in line[::-1]:
        acc = letter + acc
        if letter.isdigit():
            last = int(letter)
            break
        for key in num_dict.keys():
            if key in acc:
                last = num_dict[key]
                break
        else:
            continue
        break

    total += first * 10 + last

print(total)
