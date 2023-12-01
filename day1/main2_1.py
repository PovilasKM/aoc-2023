import re

num_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "1": 1,
            "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
pattern = '|'.join(num_dict.keys())
lines = [x for x in open('data.txt', "r").read().split("\n") if x]  # my data file always adds an empty line :(
total = 0
for line in lines:
    first = num_dict[re.search(pattern, line).group()]
    last = num_dict[re.search(pattern[::-1], line[::-1]).group()[::-1]]
    total += first * 10 + last
print(total)
