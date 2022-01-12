import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
dy, dx = [-1, 0, 0, 1], [0, 1, -1, 0]
answer = 0

def bfs(sy, sx):
    global answer
    visited = [[False for _ in range(m+1)] for _ in range(n+1)]
    visited[sy][sx] = True
    queue = deque()
    queue.append((sy, sx, 0))
    mem = 0
    while queue:
        y, x, cnt = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0<=ny<n and 0<=nx<m:
                if visited[ny][nx]:
                    continue
                if graph[ny][nx] == 'W':
                    continue
                visited[ny][nx] = True
                queue.append((ny, nx, cnt + 1))
        mem = max(mem, cnt)
    answer = max(answer, mem)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            bfs(i, j)
            
print(answer)