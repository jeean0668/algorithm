import sys

N = int(input())
array = []
for i in range(N):
    S, T = map(int, sys.stdin.readline().split())
    array.append([T, S])
    
array.sort(reverse = True)

cur = sys.maxsize
for l in array:
    cur = min([cur, l[0]])
    cur -= l[1]

print(cur)