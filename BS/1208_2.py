import sys
from collections import defaultdict
from itertools import combinations

n, s = map(int, input().split())
array = list(map(int, input().split()))

l = array[:n//2]
r = array[n//2:]

lsum = defaultdict(int)
rsum = defaultdict(int)
lsum[0] = 1
rsum[0] = 1

for i in range(1, len(l)+1):
    for comb in combinations(l, i):
        lsum[sum(comb)] += 1
for i in range(1, len(r) + 1):
    for comb in combinations(r, i):
        rsum[sum(comb)] += 1

lkeys = sorted(lsum.keys())
rkeys = sorted(rsum.keys())

left, right = 0, len(rkeys) - 1
result = 0
while left < len(lkeys) and right >= 0:
    if lkeys[left] + rkeys[right] == s:
    
        result += (sum[lkeys[left]] * lsum[rkeys[right]])
        left +=1
        right -=1
    elif lkeys[left] + rkeys[right] > s:
        right -= 1
    else:
        left += 1

if s == 0:
    result -= 1
print(result)
    
    