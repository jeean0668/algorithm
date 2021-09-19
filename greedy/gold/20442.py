import sys

input = sys.stdin.readline

S = list(input().strip())
lk = []
rk = []
cnt = 0
for s in S:
    if s == 'K':
        cnt+=1
    else:
        lk.append(cnt)

cnt = 0
for s in S[::-1]:
    if s == 'K':
        cnt+=1
    else:
        rk.append(cnt)
rk.reverse()
        
left = 0
right = len(rk) - 1

ans = 0
while left <= right:
    ans = max(ans, right - left + 1 + 2*min(lk[left], rk[right]))
    if lk[left] < rk[right]:
        left += 1
    else:
        right -= 1
print(ans)