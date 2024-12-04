# Challenge 1
xmas = []
res = 0
lookingfor = "XMAS"
search = open("Inputs/Day4.txt")
for i in range(140):
    xmas.append(search.readline())
for i in xmas:
    length = len(i)
    temp = i.replace("XMAS","")
    res += (length-len(temp))//4
for i in xmas:
    length = len(i)
    temp = i.replace("SAMX","")
    res += (length-len(temp))//4
for i in range(len(xmas)):
    for x in range(len(xmas[i])):
        if xmas[i][x] == "X":
            if i >=3:
                if xmas[i-1][x] == "M":
                    correct = True
                    for t in range(2,4):
                        if xmas[i-t][x] != lookingfor[t]:
                            correct = False
                            break
                    if correct == True:
                        res += 1
                if x >=3 and xmas[i-1][x-1] == "M":
                    correct = True
                    for t in range(2,4):
                        if xmas[i-t][x-t] != lookingfor[t]:
                            correct = False
                            break
                    if correct == True:
                        res += 1
                if x <= len(xmas[i])-4 and xmas[i-1][x+1] == "M":
                    correct = True
                    for t in range(2,4):
                        if xmas[i-t][x+t] != lookingfor[t]:
                            correct = False
                            break
                    if correct == True:
                        res += 1
            if i <= len(xmas)-4:
                if xmas[i+1][x] == "M":
                        correct = True
                        for t in range(2,4):
                            if xmas[i+t][x] != lookingfor[t]:
                                correct = False
                                break
                        if correct == True:
                            res += 1
                if x >=3 and xmas[i+1][x-1] == "M":
                        correct = True
                        for t in range(2,4):
                            if xmas[i+t][x-t] != lookingfor[t]:
                                correct = False
                                break
                        if correct == True:
                            res += 1
                if x <= len(xmas[i])-4 and xmas[i+1][x+1] == "M":
                    correct = True
                    for t in range(2,4):
                        if xmas[i+t][x+t] != lookingfor[t]:
                            correct = False
                            break
                    if correct == True:
                        res += 1
print(res)

# Challenge 2
xmas = []
res = 0
search = open("Inputs/Day4.txt")
for i in range(140):
    xmas.append(search.readline())
for i in range(1,len(xmas)-1):
    for x in range(len(xmas[i])):
        if xmas[i][x] == "A":
            if (xmas[i-1][x-1] == "M" and xmas[i+1][x+1] == "S") or (xmas[i-1][x-1] == "S" and xmas[i+1][x+1] == "M"):
                correct = True
            else:
                correct = False
            if correct == True:
                if (xmas[i+1][x-1] == "M" and xmas[i-1][x+1] == "S") or (xmas[i+1][x-1] == "S" and xmas[i-1][x+1] == "M"):
                    correct = True
                else:
                    correct = False
            if correct == True:
                res += 1
print(res)
