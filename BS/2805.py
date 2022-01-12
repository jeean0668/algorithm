import sys
input = sys.stdin.readline

n, m = map(int, input().split())
woods = list(map(int, input().split()))
max_len = max(woods)

left, right = 0, max_len

while left <= right:
    mid = (left + right)//2
    cnt = 0
    for wood in woods:
        if wood > mid:
            cnt += (wood - mid)
    if cnt < m:
        right = mid - 1
    else:
        left = mid + 1
print(right)