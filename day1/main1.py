lines = open('data.txt', "r").read().split("\n")
total = 0
for line in [x for x in lines if x]:
    nums = [int(x) for x in line if x.isdigit()]
    total += nums[0] * 10 + nums[-1]
print(total)
