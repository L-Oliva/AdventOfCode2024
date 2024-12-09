# Challenge 1
input_ = open("Inputs/Day9.txt")
input_ = input_.readline()
files = []
count = 0
for i in range(len(input_)):
    if i % 2 == 0:
        for i in range(int(input_[i])):
            files.append(count)
        count += 1
    else:
        for i in range(int(input_[i])):
            files.append(".")
l,r = 0,len(files)-1
while l < r:
    while files[l] != ".":
        l +=1 
    while files[r] == ".":
        r -= 1
    if l < r:
        files[l] = files.pop(r)
        l +=1
        r-=1
res = 0
for i in range(len(files)):
    if files[i] != ".":
        res += files[i]*i
print(res)

# Challenge 2
input_ = open("Inputs/Day9.txt")
input_ = input_.readline()
files = []
count = 0
for i in range(len(input_)):
    if i % 2 == 0:
        for i in range(int(input_[i])):
            files.append(count)
        count += 1
    else:
        for i in range(int(input_[i])):
            files.append(".")
l,lr,r,rl = 0,1,len(files)-1,len(files)-2
space = []
leftSpace, rightSpace = 0,1
while rightSpace < len(files) and leftSpace < len(files):
    while leftSpace < len(files)-1 and files[leftSpace] != "." :
        leftSpace += 1
    if files[leftSpace] != ".":
        break
    rightSpace = leftSpace +1 
    while files[rightSpace] == ".":
        rightSpace += 1
    
    space.append([rightSpace-leftSpace,leftSpace,rightSpace])
    leftSpace = rightSpace +1
while r >= 0:
    while files[r] == ".":
        r -= 1
    rl = r-1
    while files[rl] == files[r]:
        rl -= 1
    if l < r:
        length = r-rl
        change = False
        for i in range(len(space)):
            if space[i][0] == length and space[i][1] < r:
                change = True
                for x in range(length):
                    files[space[i][1]+x] = files[r]
                    files[r] = "."
                    r -=1
                space.pop(i)
                break
            elif space[i][0] > length and space[i][1] < r:
                change = True
                for x in range(length):
                    files[space[i][1]+x] = files[r]
                    files[r] = "."
                    r -=1
                space[i][0] -= length
                space[i][1] += length
                break
    if change == False:
        r -= length
res = 0
for i in range(len(files)):
    if files[i] != ".":
        res += files[i]*i
print(res)
