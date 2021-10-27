import sys
input = sys.stdin.readline

n = int(input())
server = [list(map(int, input().split())) for _ in range(n)]
total = 0
_sum = 0
for i in range(n):
    for j in range(n):
        total = max(total, server[i][j])
        _sum += server[i][j]

def search(left, right):
    if _sum == 0:
        print(0)
        return
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for i in range(n):
            for j in range(n):
                cnt += min(server[i][j], mid)
        if cnt / _sum >= 0.5:
            right = mid - 1
        else:
            left = mid + 1
    print(left)
        
search(0, total)

