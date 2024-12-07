# Challenge 1
from itertools import product
input_ = open("Inputs/Day7.txt")
finding= []
nums = []
for i in input_:
    l,r = i.split(":")
    finding.append(int(l))
    nums.append(list(map(int,r[:-1].strip().split(" "))))

res = 0
for i in range(len(finding)):
    operators = list(product("+*",repeat=len(nums[i])-1))
    correct = False
    time = 0
    for curr in operators:
        total = nums[i][0]
        for x in range(len(nums[i])-1):
            if curr[x] == "+":
                total += nums[i][x+1]
            else:
                total*=nums[i][x+1]
        if total == finding[i]:
            correct = True
            res += total
            break
print(res)

# Challenge 2
from itertools import product
input_ = open("Inputs/Day7.txt")
finding= []
nums = []
for i in input_:
    l,r = i.split(":")
    finding.append(int(l))
    nums.append(list(map(int,r[:-1].strip().split(" "))))

res = 0
for i in range(len(finding)):
    operators = list(product("+*|",repeat=len(nums[i])-1))
    correct = False
    time = 0
    for curr in operators:
        total = nums[i][0]
        for x in range(len(nums[i])-1):
            if curr[x] == "+":
                total += nums[i][x+1]
            elif curr[x] == "|":
                total = int(str(total)+str(nums[i][x+1]))
            else:
                total*=nums[i][x+1]
        if total == finding[i]:
            correct = True
            res += total
            break
print(res)

