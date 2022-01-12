import sys
import math
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
pos = [[0,0]] + [list(map(int, input().split())) for _ in range(n)]

left, right = 0, 15000

ans = sys.maxsize
def distance(y, x, ny, nx):
    dis = math.ceil(math.sqrt((ny - y) ** 2 + (nx - x) ** 2) / 10)
    return dis 
def count(value):
    # value만큼의 연료로 몇개의 중간지점을 거쳐가야 하는지 반환
    
    queue = deque()
    visited = [False] * (n+1)
    visited[0] = True
    queue.append((0, 0, 0))
    while queue:
        y, x, cnt= queue.popleft()
        if distance(y, x, 10000, 10000) <= value:
            return True
        if cnt == k+1:
            continue
        for i in range(len(pos)):
            if visited[i]: continue
            ny, nx = pos[i][0], pos[i][1]
            if distance(y, x, ny, nx) <= value:
                visited[i] = True
                queue.append((ny, nx, cnt + 1))
    return False
            
while left <= right:
    mid = (left + right) // 2

    if count(mid):
        ans = min(ans, mid)
        right = mid - 1
    else:
        left = mid + 1
print(ans)