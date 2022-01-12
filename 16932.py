import sys
input = sys.stdin.readline
sys.setrecursionlimit(222222)
n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

#1 타일들의 영역을 그룹화한다.

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]
visited = [[False for _ in range(m+1)] for _ in range(n+1)]

group = [0 for _ in range(1000001)]
def dfs(y, x, num):

    graph[y][x] = num
    ret = 1
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if not(0<=ny<n and 0<=nx<m):continue
        if visited[ny][nx] or graph[ny][nx] == 0: continue
        visited[ny][nx] = True
        ret += dfs(ny, nx, num)
    return ret
            
num = 2
for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 1:
            visited[i][j] = True
            size = dfs(i, j, num)
            group[num] = size
            num += 1

# 0 타일을 기준으로 탐색한다.

def search(y, x):
    ret = 1
    used = set()
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if not(0<=ny<n and 0<=nx<m): continue
        if graph[ny][nx] != 0 and graph[ny][nx] not in used:
            ret += group[graph[ny][nx]]
            used.add(graph[ny][nx])
    return ret

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            tmp = search(i, j)
            result = max(result, tmp)

print(result)

