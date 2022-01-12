import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

result = 0

def dfs(y, x, h):
    
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0<=ny<n and 0<=nx<n:
            if visited[ny][nx]: continue
            if graph[ny][nx] > h:
                visited[ny][nx] = True
                dfs(ny, nx, h)

max_area = 1
for i in range(min(map(min, graph)), max(map(max, graph)) + 1):
    cnt = 0
    visited = [[False for _ in range(n+1)] for _ in range(n+1)]
    for y in range(n):
        for x in range(n):
            if graph[y][x] > i and not visited[y][x]:
                visited[y][x] = True
                dfs(y, x, i)
                cnt += 1
    if max_area < cnt:
        max_area = cnt

print(max_area)