import sys
from collections import defaultdict
from itertools import combinations
input = sys.stdin.readline

T = int(input())
m, n = map(int, input().split())
A = [int(input()) for _ in range(m)]
B = [int(input()) for _ in range(n)]

dictA = defaultdict(int)
dictB = defaultdict(int)
dictA[0] = 1
dictB[0] = 1

for i in range(0, len(A)):
    s = 0
    for j in range(0,len(A)):
        s += A[(i+j)%m]
        if s > T : break
        dictA[s] += 1
        
for i in range(len(B)):
    s = 0
    for j in range(len(B)):
        s += B[(i+j)%n]
        if s > T: break
        dictB[s] += 1

Akeys = sorted(dictA.keys())
Bkeys = sorted(dictB.keys())
dictA[sum(A)] = dictB[sum(B)] = 1

result = 0
for i in range(T + 1):
    result += dictA[i] * dictB[T-i]
print(result)