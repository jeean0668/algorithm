import sys
from itertools import combinations
from collections import defaultdict
"""[summary]
1. mid 기준으로 좌우의 모든 부분수열의 경우의 수를 구한다.
2. 부분수열의 합을 구하면, 그 합이 총 몇개 나올 수 있는지 dict[sum] 에 저장한다.
3. 만약 left에서 나온 값과 right에서 나온 값의 합이 s이면
dict[left]에서 나온 총 갯수와 dict[right]에서 나온 총 갯수를 곱한다.
"""
n,s=map(int,sys.stdin.readline().split())
m=list(map(int, sys.stdin.readline().split()))


l=m[:n//2]
r=m[n//2:]

lsum=defaultdict(int)
rsum=defaultdict(int)
lsum[0]=1
rsum[0]=1
for i in range(1,len(l)+1):
    for com in combinations(l,i):
        lsum[sum(com)]+=1

for i in range(1,len(r)+1):
    for com in combinations(r,i):
        rsum[sum(com)]+=1

lkey=sorted(lsum.keys())
rkey=sorted(rsum.keys())

res=0
l=0
r=len(rkey)-1
while l<len(lkey) and r>=0:
    if lkey[l]+rkey[r]==s:
        res+=(lsum[lkey[l]]*rsum[rkey[r]])
        l+=1
        r-=1
    elif lkey[l]+rkey[r]>s:
        r-=1
    else:
        l+=1

if s==0:
    res-=1
print(res)