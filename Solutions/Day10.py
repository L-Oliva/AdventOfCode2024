from collections import deque
input_ = open("Inputs/Day10.txt")
tmap = []
for i in input_:
    tmap.append(list(map(int,list(i[:-1]))))
queue = deque()
for i in range(len(tmap)):
    for x in range(len(tmap[i])):
        if tmap[i][x] == 0:
            queue.append((i,x))
while len(queue) > 0:
    curr = queue.popleft()

