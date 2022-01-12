from bisect import bisect_left
import sys
input = sys.stdin.readline
"""
LIS 알고리즘 문제였다. LIS 알고리즘에 대해 처음 알게 된 문제
다만 마지막에 굳이 idx.append(i+1)을 하는지는 이해하지 못했다. 
"""
N = int(input().rstrip())
left = list(map(int, input().rstrip().split(' ')))
right = list(map(int, input().rstrip().split(' ')))

line = dict()
for i, r in enumerate(right):
    line[r] = i
print(line)
array = [line[x] for x in left]
LIS = [array[0]]
idx = []
print(array)
for a in array:
    if LIS[-1] < a:
        LIS.append(a)
        idx.append(len(LIS))
    else:
        i = bisect_left(LIS, a)
        LIS[i] = a
        idx.append(i + 1)
print(idx, LIS)
M = len(LIS)
i = N - 1
print(M)
ans_idx = []
while M > 0:
    if M == idx[i]:
        M -= 1
        ans_idx.append(i)
    i -= 1
print(*sorted([left[x] for x in ans_idx]))