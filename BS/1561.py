import sys
input = sys.stdin.readline

n, m = map(int, input().split())
waitings = list(map(int, input().split()))

# 이분탐색으로 최소 시간부터 구한다.

left, right = 0, max(waitings) * n
time = 0
if n <= m:
    print(n)
    sys.exit()
while left <= right:
    mid = (left + right) // 2
    cnt = m
    for t in waitings:
        cnt += (mid // t)
    if cnt < n:
        left = mid + 1
    else:
        time = mid
        right = mid - 1
# time - 1까지 탑승한 아이들을 전부 더한다. 

children = m
for t in waitings:
    children += (time-1) // t
# time에 탑승한 아이를 확인한다.
for i in range(m):
    if (time % waitings[i]) == 0:
        children += 1
    if children == n:
        print(i+1)
        break