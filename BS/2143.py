import sys
from collections import defaultdict
input = sys.stdin.readline

dictA, dictB = defaultdict(int), defaultdict(int)
T = int(input())
n1, A = int(input()), list(map(int, input().split()))
n2, B = int(input()), list(map(int, input().split()))

for i in range(n1):
    for j in range(i, n1):
        dictA[sum(A[i:j+1])] += 1

for i in range(n2):
    for j in range(i, n2):
        dictB[sum(B[i:j+1])] += 1

ans = 0
for key in dictA.keys():
    ans += dictB[T - key] * dictA[key]
print(ans)

