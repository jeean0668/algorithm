import sys

input = sys.stdin.readline

n, c = map(int, input().split())
m = int(input())

array = []
for _ in range(m):
    array.append(list(map(int, input().split())))
    
array.sort(key = lambda x : x[1])

box = [c] * (n+1)
answer = 0
for i in range(m):
    start, end, cap = array[i][0], array[i][1], array[i][2]
    _min = c
    for j in range(start, end):
        _min = min(_min, box[j])
    _min = min(_min, cap)
    
    for j in range(start, end):
        box[j] -= _min
    answer += _min

print(answer)