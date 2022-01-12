import sys
input = sys.stdin.readline

n, c = map(int,input().split())
machine = [int(input()) for _ in range(n)]
machine.sort()

left, right = 1, max(machine) - min(machine)

def func(value):
    # 최대 거리가 value일때 고를 수 있는 최대 갯수
    now = machine[0]
    cnt = 1
    for i in range(1, n ):
        if machine[i] - now >= value:
            now = machine[i]
            cnt += 1
    if cnt >= c:
        return True
    else:
        return False
ans = 0
while left <= right:
    mid = (left + right) // 2
    if func(mid):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1
print(ans)
