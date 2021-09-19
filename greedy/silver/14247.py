import sys

N = int(input())

initial = list(map(int, sys.stdin.readline().split()))
growth = list(map(int, sys.stdin.readline().split()))

array = sorted([[growth[i], initial[i]] for i in range(N)])

_sum = 0

for i in range(N):
    
    _sum += array[i][1] + array[i][0] * i

print(_sum)
