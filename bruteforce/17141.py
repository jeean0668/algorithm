import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
points = []
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    
for i in range(n):
    for j in range(len(graph[i])):
        if graph[i][j] == 2:points.append((i, j))

def bfs(s_point):
    
    queue = deque()
    visited = [[False for _ in range(n+1)] for _ in range(n+1)]
    for s in s_point:
        queue.append((s[0], s[1], 0))
        visited[s[0]][s[1]] = True
    while queue:
        y, x, cnt = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not(0<=ny<n and 0<=nx<n): continue
            if graph[ny][nx] == 1 : continue
            if visited[ny][nx]: continue
            queue.append((ny, nx, cnt + 1))
            visited[ny][nx] = True
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 : continue
            if not visited[i][j] : return sys.maxsize
    return cnt
     
point_combinations = combinations(points, m)
ans = sys.maxsize
for comb in point_combinations:
    result = bfs(comb)
    ans = min(ans, result)

if ans == sys.maxsize:print(-1)
else: print(ans)
