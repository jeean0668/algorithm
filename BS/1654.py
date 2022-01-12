import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]
left, right = 1, max(lan)

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for l in lan:
        cnt += l//mid
    if cnt >= n: left = mid + 1
    else: right = mid - 1
print(right)