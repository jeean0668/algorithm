import sys
input = sys.stdin.readline

n, m = map(int, input().split())
staffs = list(map(int, input().split()))

max_time = max(staffs) * m
left, right = 0, max_time

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for s in staffs:
        cnt += (mid // s)
    if cnt >= m:
        right = mid - 1
    else:
        left = mid + 1
print(left)