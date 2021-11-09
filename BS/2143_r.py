import sys, bisect
input = sys.stdin.readline

t = int(input())
n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

A = []
for i in range(n):
    tmp = 0
    for j in range(i,n):
        tmp += a[j]
        A.append(tmp)

B = []
for i in range(m):
    tmp = 0
    for j in range(i,m):
        tmp += b[j]
        B.append(tmp)
print(B)
B.sort()

print(A, B)
cnt = 0
for i in A:
    diff = t-i
    left, right = 0, len(B) - 1
    
    # diff와 크기가 같은 B의 원소들을 찾는다. 
    idx = bisect.bisect_left(B,diff) # -> diff 이상 값을 갖는 B의 index
    if idx >= len(B):
        continue
        
    idx_right = bisect.bisect_right(B,diff) # -> diff를 초과하는 B의 index
    # idx_right-idx -> diff 크기를 갖는 원소의 갯수
    if B[idx] == diff:
        # 
        print(diff, idx_right, idx)
        cnt+=idx_right-idx
print(cnt)