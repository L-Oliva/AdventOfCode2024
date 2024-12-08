# Challenge 1
from collections import defaultdict
input_= open("Inputs/Day8.txt")
grid = []
for i in input_:
    grid.append(list(i[:-1]))
dict = defaultdict(list)
for i in range(len(grid)):
    for x in range(len(grid[i])):
        if grid[i][x] != ".":
            dict[grid[i][x]].append([i,x])
values = dict.values()
res = set()
for l,i in dict.items():
    for x in range(len(i)):
        for t in range(len(i)):
            if x == t:
                continue
            else:
                antinode = (i[x][0]+(i[x][0]-i[t][0]),i[x][1]+(i[x][1]-i[t][1]))
                if antinode[0] < 0 or antinode[1] < 0 or antinode[0] >= len(grid) or antinode[1] >= len(grid[0]):
                    continue
                else:
                    res.add(antinode)
print(len(res))

# Challenge 2
from collections import defaultdict
input_= open("Inputs/Day8.txt")
grid = []
for i in input_:
    grid.append(list(i[:-1]))
dict = defaultdict(list)
for i in range(len(grid)):
    for x in range(len(grid[i])):
        if grid[i][x] != ".":
            dict[grid[i][x]].append([i,x])
values = dict.values()
res = set()
for l,i in dict.items():
    for x in range(len(i)):
        res.add((i[x][0],i[x][1]))
        for t in range(len(i)):
            if x == t:
                continue
            else:
                subtract = ((i[x][0]-i[t][0]),(i[x][1]-i[t][1]))
                antinode = (i[x][0],i[x][1])
                while antinode[0] >= 0 and antinode[1] >= 0 and antinode[0] < len(grid) and antinode[1] < len(grid[0]):
                    antinode = (antinode[0]+subtract[0],antinode[1]+subtract[1])
                    if antinode[0] < 0 or antinode[1] < 0 or antinode[0] >= len(grid) or antinode[1] >= len(grid[0]):
                        break
                    else:
                        res.add(antinode)
print(len(res))