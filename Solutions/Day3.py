
# Challenge 1
input_ = open("Inputs/Day3.txt")
code = []
check = {"1","2","3","4","5","6","7","8","9","0","(",")",","}
res = 0 
correct = True
for i in input_:
    code.append(i.split("mul"))
for i in range(len(code)):
    for x in range(len(code[i])):
        for t in range(len(code[i][x])):
            if code[i][x][t] == ")":
                code[i][x] = code[i][x][:t+1]
                break
for i in code:
    for x in i:
        correct = True
        for t in x:
            if t not in check:
                correct = False
                break
        if correct == True:
            x = x.replace("(","")
            x = x.replace(")","")
            nums = x.split(",")
            if len(nums) > 1:
                res += int(nums[0])*int(nums[1])
print(res)

# Challenge 2
input_ = open("Inputs/Day3.txt")
code = []
check = {"1","2","3","4","5","6","7","8","9","0","(",")",",","o","'","n","t"}
res = 0 
correct = True
for i in input_:
    curr = []
    curr = i.split("mul")
    for x in range(len(curr)):
        curr[x] = curr[x].split("d")
    code.append(curr)
for i in range(len(code)):
    for x in range(len(code[i])):
        for t in range(len(code[i][x])):
            for l in range(len(code[i][x][t])):
                if code[i][x][t][l] == ")":
                    code[i][x][t] = code[i][x][t][:l+1]
                    break
allowed = True
for i in code:
    for x in i:
        for l in x:
            correct = True
            if l == "o()":
                allowed = True
                correct = False
            elif l == "on't()":
                allowed = False
                correct = False
            else:
                for t in l:
                    if t not in check:
                        correct = False
                        break
            if correct == True and allowed == True:
                l = l.replace("(","")
                l = l.replace(")","")
                nums = l.split(",")
                if len(nums) > 1:
                    res += int(nums[0])*int(nums[1])
print(res)