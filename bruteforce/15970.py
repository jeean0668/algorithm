import sys
from collections import defaultdict
input = sys.stdin.readline

spots = defaultdict(list)
n = int(input())
for _ in range(n):
    pos, col = map(int, input().split())
    spots[col].append(pos)

keys = list(spots.keys())

length = 0
for key in keys:
    arr = spots[key]
    arr.sort()
    for i in range(len(arr)):
        if i == 0:
            length += (arr[1] - arr[0])
        elif i == len(arr) - 1:
            length += (arr[i] - arr[i-1])
        else:
            if arr[i] - arr[i-1] > arr[i+1] - arr[i]:
                length += arr[i+1] - arr[i]
            else:
                length += arr[i] - arr[i-1]

print(length)
        