dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
import sys
sys.setrecursionlimit(10**6) #재귀 깊이 설정 (10만 -> 100만)

def dfs(x, y, _cnt):
    dist[x][y] = _cnt

    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0<=nx<n and 0<=ny<m:
            if a[nx][ny] == 1 and dist[nx][ny] == -1:
                dfs(nx, ny, _cnt)



t = int(input())
for _ in range(t):
    m, n, c = map(int, input().split())
    a = [[0] * m for _ in range(n)]
    dist = [[-1]*m for _ in range(n)]
    cnt = 0

    for _ in range(c):
        i, j = map(int, input().split())
        a[j][i] = 1

    # dfs 탐색
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1 and dist[i][j] == -1:
                cnt += 1
                dfs(i, j, cnt)

    print(cnt)
    