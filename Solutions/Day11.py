# Challenge 1
from collections import defaultdict
input_ = open("Inputs/Day11.txt")
stones = input_.readline().split(" ")
for _ in range(25):
    temp = defaultdict(list)
    for i in range(len(stones)):
        if stones[i] == "0":
            stones[i] = "1"
        elif len(stones[i])%2 == 0:
            l,r = stones[i][:len(stones[i])//2],stones[i][len(stones[i])//2:]
            for x in range(len(r)):
                if r[x] != "0":
                    r = r[x:]
                    break
                if r == len(r)*"0":
                    r = "0"
                    break
            temp[i].append(l)
            temp[i].append(r)
        else:
            stones[i] = str(int(stones[i])*2024)
    changes = 0 
    for i,x in temp.items():
        stones.insert(i+changes,x[0])
        changes += 1
        stones[i+changes] = x[1]
print(len(stones))

# Challenge 2
from collections import defaultdict
from functools import cache
input_ = open("Inputs/Day11.txt")
stones = list(map(int,input_.readline().split(" ")))

@cache
def howmany(val,blinks):
    if blinks == 0:
        return 1
    elif val == 0:
        return howmany(1,blinks-1)
    elif len(str(val))%2 == 0:
        l = str(val)[:len(str(val))//2]
        r = str(val)[len(str(val))//2:]
        for x in range(len(r)):
            if r[x] != "0":
                r = r[x:]
                break
            if r == len(r)*"0":
                r = "0"
                break
        return howmany(int(l),blinks-1) + howmany(int(r),blinks-1)
    else:
        return howmany(val*2024,blinks-1)    
res = 0
for i in stones:
    res += howmany(i,75)
print(res)