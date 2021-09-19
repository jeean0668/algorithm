import sys

# DP 활용 문제 
# 특정한 점에서 갈 수 있는 모든 경로의 수를 더하여 저장한다. 
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
dy = [1, 0, 0, -1]
dx = [0, 1, -1, 0]
c = [[-1] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

def dfs(y, x):
    if y == n-1 and x == m-1:
        return 1
    if c[y][x] != -1: 
        return c[y][x]
    c[y][x] = 0 # c[y][x] 에 graph[y][x]에서 갈 수 있는 모든 경로 저장
    for i in range(4):
        yy = y + dy[i]
        xx = x + dx[i]
        
        if 0 <= yy < n and 0 <= xx < m :
            if graph[y][x] <= graph[yy][xx]:
                continue
            c[y][x] += dfs(yy,xx)
    return c[y][x]
print(c)
print(dfs(0, 0))
