import sys

input = sys.stdin.readline

n = int(input())

box = [0] * (1000)
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

array.sort(key = lambda x : -x[1])

for arr in array:
    score = arr[1]
    index = arr[0]-1
    while score <= box[index]:
        index -= 1
        if index < 0:
            break
    if index >= 0:
        box[index] = score
print(sum(box))
