
# Challenge 1
txt = open("Inputs/Day2.txt")
reports = []
safe = 0
for i in txt:
    reports.append(list(map(int,i.split(" "))))
for i in reports:
    if i[0] - i[1] > 0:
        increasing = False
    elif i[0]-i[1] == 0:
        continue
    else:
        increasing = True
    for x in range(len(i)-1):
        if increasing == True:
            diff = i[x+1]-i[x]
        else:
            diff = i[x] - i[x+1]
    
        if diff < 1 or diff > 3:
            break
        elif x == len(i)-2:
            safe += 1
print(safe)

# Challenge 2
txt = open("Inputs/Day2.txt")
reports = []
safe = 0
for i in txt:
    reports.append(list(map(int,i.split(" "))))
   
def check(i):
    if i[0] - i[1] > 0:
        increasing = False
    elif i[0]-i[1] == 0:
        return False
    else:
        increasing = True
    for x in range(len(i)-1):
        if increasing == True:
            diff = i[x+1]-i[x]
        else:
            diff = i[x] - i[x+1]
   
        if diff < 1 or diff > 3:
            break
        elif x == len(i)-2:
            return True
    return False
for i in reports:
    if check(i) == False:
        for x in range(len(i)):
            new = []
            for t in i:
                new.append(t)
            new.pop(x)
            if check(new) == True:
                safe += 1
                break
    elif check(i) == True:
        safe +=1
print(safe)
