import sys
input = sys.stdin.readline

n, k = map(int, input().split())
T = [int(input()) for _ in range(n)]
left, right = min(T), max(T) + k 

ans = 0
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for t in T:
        if t < mid:
            cnt += (mid - t)
    if cnt > k:
        right = mid - 1
    else:
        ans = mid
        left = mid + 1
print(ans)
