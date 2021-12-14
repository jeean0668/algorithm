import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dy = [0,-1, 0, 0, 1]
dx = [0,0, -1, 1, 0]
visited = [[False] * (n+1) for _ in range(n+1)]

def checked(y, x):
    for i in range(5):
        ny, nx = y + dy[i], x + dx[i]
        if not(0<=ny<n and 0<=nx<n):return False
        if visited[ny][nx] : return False
    return True

def cal(y, x):
    result = 0
    for i in range(5):
        ny, nx = y + dy[i], x + dx[i]
        result += graph[ny][nx]
    return result

answer = sys.maxsize
def dfs(y, cnt, value):
    global answer
    if cnt == 3:
        answer = min(answer, value)
        return 
    for i in range(y, n):
        for j in range(1, n):
            if not checked(i, j): continue
            visited[i][j] = True
            for k in range(5):
                ny, nx = i + dy[k], j + dx[k]
                visited[ny][nx] = True
            dfs(i, cnt + 1, value + cal(i, j))
            visited[i][j] = False
            for k in range(5):
                ny, nx = i + dy[k], j + dx[k]
                visited[ny][nx] = False

dfs(1, 0, 0)
print(answer)