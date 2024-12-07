# Challenge 1
# input_ = open("Inputs/Day6.txt")
# layout = []
# for i in input_:
#     layout.append(list(i[:-1]))
# for i in range(len(layout)):
#     for x in range(len(layout[i])):
#         if layout[i][x] == "^":
#             gaurd = [i,x]
# directions = [(-1,0),(0,1),(1,0),(0,-1)]
# direction = 0
# while True:
#     layout[gaurd[0]][gaurd[1]] = "X"
#     nextLocation = [gaurd[0]+directions[direction][0],gaurd[1]+directions[direction][1]]
#     if nextLocation[0] >= len(layout) or nextLocation[1] >= len(layout[nextLocation[0]]) or nextLocation[0]<0 or nextLocation[1]<0:
#         break

#     elif layout[nextLocation[0]][nextLocation[1]] == "#":
#         direction = (direction +1)%4
#         nextLocation = [gaurd[0]+directions[direction][0],gaurd[1]+directions[direction][1]]
#     gaurd = nextLocation
# res =0
# for i in layout:
#     for x in i:
#         if x == "X":
#             res += 1
# print(res)

# Challenge 2
# Could not Get Working


from copy import deepcopy
input_ = open("Inputs/Day6.txt")
layout = []
res = 0
for i in input_:
    layout.append(list(i[:-1]))
for i in range(len(layout)):
    for x in range(len(layout[i])):
        if layout[i][x] == "^":
            gaurd = [i,x]

def test(grid,gaurd):
    directions = [(-1,0),(0,1),(1,0),(0,-1)]
    direction = 0
    i = 0 
    while True:
        nextLocation = [gaurd[0]+directions[direction][0],gaurd[1]+directions[direction][1]]
        if nextLocation[0] >= len(grid) or nextLocation[1] >= len(grid[nextLocation[0]]) or nextLocation[0]<0 or nextLocation[1]<0:
            return False
        elif i >= 130**2:
            return True
        elif grid[nextLocation[0]][nextLocation[1]] == "#":
            while grid[nextLocation[0]][nextLocation[1]] == "#":
                direction = (direction +1)%4
                nextLocation = [gaurd[0]+directions[direction][0],gaurd[1]+directions[direction][1]]
        gaurd = deepcopy(nextLocation)
        i += 1
x = deepcopy(gaurd)
pointer = deepcopy(gaurd)
directions = [(-1,0),(0,1),(1,0),(0,-1)]
direction = 0
counter = 0
found = set()
for i in range(130**2):
    counter += 1
    passIn = deepcopy(layout)
    next = [pointer[0]+directions[direction][0],pointer[1]+directions[direction][1]]
    if next[0] >= len(layout) or next[1] >= len(layout[next[0]]) or next[0]<0 or next[1]<0:
        break
    elif layout[next[0]][next[1]] == "#":
        direction = (direction +1)%4
        next = [pointer[0]+directions[direction][0],pointer[1]+directions[direction][1]]
    passIn[next[0]][next[1]] = "#"
    if test(passIn,x) == True and tuple(next) not in found:
        found.add(tuple(next))
        res += 1
    pointer = deepcopy(next)
print(res)
