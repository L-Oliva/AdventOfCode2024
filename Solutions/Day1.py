# Challenge 1
import heapq
id = open("Day1.txt")
left = []
right = []
sum = 0
for i in id:
    add = i.split("   ")
    left.append(int(add[0]))
    right.append(int(add[1][:5]))
heapq.heapify(left)
heapq.heapify(right)
for i in range(1000):
    sum += abs(heapq.heappop(left)-heapq.heappop(right))
print(sum)


# Challenge 2
from collections import Counter
id = open("Day1.txt")
left = []
right = []
similarity = 0
for i in id:
    add = i.split("   ")
    left.append(int(add[0]))
    right.append(int(add[1][:5]))
count = Counter(right)
for i in left:
    similarity += i*count[i]
print(similarity)