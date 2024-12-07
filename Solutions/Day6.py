# Challenge 1
input_ = open("Inputs/Day6.txt")
layout = []
for i in input_:
    layout.append(list(i[:-1]))
for i in range(len(layout)):
    for x in range(len(layout[i])):
        if layout[i][x] == "^":
            gaurd = [i,x]
directions = [(-1,0),(0,1),(1,0),(0,-1)]
direction = 0
while True:
    layout[gaurd[0]][gaurd[1]] = "X"
    nextLocation = [gaurd[0]+directions[direction][0],gaurd[1]+directions[direction][1]]
    if nextLocation[0] >= len(layout) or nextLocation[1] >= len(layout[nextLocation[0]]) or nextLocation[0]<0 or nextLocation[1]<0:
        break

    elif layout[nextLocation[0]][nextLocation[1]] == "#":
        direction = (direction +1)%4
        nextLocation = [gaurd[0]+directions[direction][0],gaurd[1]+directions[direction][1]]
    gaurd = nextLocation
res =0
for i in layout:
    for x in i:
        if x == "X":
            res += 1
print(res)

# Challenge 2
# Could not Get Working


# from copy import deepcopy
# input_ = open("Inputs/Day6.txt")
# layout = []
# res = 0
# for i in input_:
#     layout.append(list(i[:-1]))
# for i in range(len(layout)):
#     for x in range(len(layout[i])):
#         if layout[i][x] == "^":
#             gaurd = [i,x]

# def test(layout,gaurd):
#     directions = [(-1,0),(0,1),(1,0),(0,-1)]
#     direction = 0
#     i = 0 
#     while True:
#         nextLocation = [gaurd[0]+directions[direction][0],gaurd[1]+directions[direction][1]]
#         if nextLocation[0] >= len(layout) or nextLocation[1] >= len(layout[nextLocation[0]]) or nextLocation[0]<0 or nextLocation[1]<0:
#             return False
#         elif i >= 130**2:
#             return True
#         elif layout[nextLocation[0]][nextLocation[1]] == "#":
#             direction = (direction +1)%4
#             nextLocation = [gaurd[0]+directions[direction][0],gaurd[1]+directions[direction][1]]
#         layout[gaurd[0]][gaurd[1]] = "X"
#         gaurd = deepcopy(nextLocation)
        # i += 1
# x = deepcopy(gaurd)
# directions = [(-1,0),(0,1),(1,0),(0,-1)]
# direction = 0
# counter = 0
# found = set()
# for i in range(130**2):
#     counter += 1
#     passIn = deepcopy(layout)
#     nextLocation = [gaurd[0]+directions[direction][0],gaurd[1]+directions[direction][1]]
#     if nextLocation[0] >= len(layout) or nextLocation[1] >= len(layout[nextLocation[0]]) or nextLocation[0]<0 or nextLocation[1]<0:
#         break
#     elif layout[nextLocation[0]][nextLocation[1]] == "#":
#         direction = (direction +1)%4
#         nextLocation = [gaurd[0]+directions[direction][0],gaurd[1]+directions[direction][1]]
#     passIn[nextLocation[0]][nextLocation[1]] = "#"
#     if test(passIn,x) == True and tuple(gaurd) not in found:
#         found.add(tuple(gaurd))
#         res += 1
#     gaurd = nextLocation
# print(res,counter)

# from copy import deepcopy
# input_ = open("Inputs/Day6.txt")
# layout = []
# res = 0
# counter = 0
# found2 = set()
# for i in input_:
#     layout.append(list(i[:-1]))
# for i in range(len(layout)):
#     for x in range(len(layout[i])):
#         if layout[i][x] == "^":
#             gaurd = [i,x]

# def test(layout,gaurd):
#     directions = [(-1,0),(0,1),(1,0),(0,-1)]
#     direction = 0
#     i = 0 
#     while True:
#         nextLocation = [gaurd[0]+directions[direction][0],gaurd[1]+directions[direction][1]]
#         if nextLocation[0] >= len(layout) or nextLocation[1] >= len(layout[nextLocation[0]]) or nextLocation[0]<0 or nextLocation[1]<0:
#             return False
#         elif i >= 180**2:
#             return True
#         elif layout[nextLocation[0]][nextLocation[1]] == "#":
#             direction = (direction +1)%4
#             nextLocation = [gaurd[0]+directions[direction][0],gaurd[1]+directions[direction][1]]
#         layout[gaurd[0]][gaurd[1]] = "X"
#         gaurd = deepcopy(nextLocation)
#         i += 1
# location = deepcopy(gaurd)
# directions = [(-1,0),(0,1),(1,0),(0,-1)]
# direction = 0
# for i in range(len(layout)):
#     for x in range(len(layout[i])):
#         counter +=1 
#         if layout[i][x] == "^" or layout[i][x] == "#":
#             continue
#         if i == 67 and x == 59:
#             print("test")
#         passIn = deepcopy(layout)
#         passIn[i][x] = "#"
#         if test(passIn,location) == True:
#             found2.add((i,x))
#             res += 1
# print(res,counter)
# print(found.difference(found2))
