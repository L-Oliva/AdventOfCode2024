# Challenge 1
from collections import defaultdict
from math import ceil
input_ = open("Inputs/Day5.txt")
orderings = defaultdict(list)
manuals = []
for i in range(1176):
    curr = list(map(int,input_.readline().split("|")))
    orderings[curr[0]].append(curr[1])
for i in range(1177,1378):
    curr = input_.readline().split(",")
    curr[-1] = curr[-1][:len(curr[-1])-1]
    manuals.append(list(map(int,curr)))
res = 0
for i in manuals:
    sofar = []
    correct = True
    for x in range(len(i)):
        for t in range(len(sofar)):
            if sofar[t] in orderings[i[x]]:
                correct = False
                break
        if correct == False:
            break
        else:
            sofar.append(i[x])
    if correct == True and len(i) > 0:
        res += i[len(i)//2]
print(res)

# Challenge 2
from collections import defaultdict
from math import ceil
input_ = open("Inputs/Day5.txt")
orderings = defaultdict(list)
manuals = []
for i in range(1176):
    curr = list(map(int,input_.readline().split("|")))
    orderings[curr[0]].append(curr[1])
for i in range(1177,1379):
    curr = input_.readline().split(",")
    curr[-1] = curr[-1][:len(curr[-1])-1]
    manuals.append(list(map(int,curr)))
res = 0
wrong = []
for i in manuals:
    sofar = []
    correct = True
    for x in range(len(i)):
        for t in range(len(sofar)):
            if sofar[t] in orderings[i[x]]:
                correct = False
                break
        if correct == False:
            break
        else:
            sofar.append(i[x])
    if correct==False:
        wrong.append(i)
for i in wrong:
    while True:
        correct = True
        sofar = []
        for x in range(len(i)):
            for t in range(len(sofar)):
                if sofar[t] in orderings[i[x]]:
                    correct = False
                    i.insert(t,i.pop(x))
                    continue
            sofar.append(i[x])
        if correct == True:
            res += i[len(i)//2]
            break
print(res)

