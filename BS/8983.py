import sys
input = sys.stdin.readline

m, n, l = map(int, input().split())
x = list(map(int, input().split()))
preys = [list(map(int, input().split())) for _ in range(n)]
x.sort()

memory = []
cnt = 0
for p in preys:
    left, right = 0, m-1
    while left <= right:
        mid = (left + right) // 2
        if abs(p[0] - x[mid]) + p[1] <= l:
            cnt += 1
            break
        if p[0] > x[mid]:
            left = mid + 1
        else :
            right = mid - 1

print(cnt)