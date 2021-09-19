import sys

input = sys.stdin.readline
dy = [1,0,0,-1]
dx = [0,1,-1,0]
n, m, k = map(int,input().split())
graph = [[0] * m for _ in range(n)] 
visited = [[False for _ in range(m)] for _ in range(n)]
for _ in range(k):
    y, x = map(int, input().split())
    graph[y-1][x-1] = 1

def dfs(start):
    y, x = start[0], start[1]
    stack = [[y, x]]
    count = 0 
    while stack:
        now = stack.pop()
        for i in range(4):
            yy = now[0] + dy[i]
            xx = now[1] + dx[i]
            if 0 <= yy < n and 0 <= xx < m and graph[yy][xx]:
                if not visited[yy][xx]:
                    #print("yy is {}, xx is {}".format(yy, xx))
                    visited[yy][xx] = True
                    stack.append([yy, xx])
                    count += 1
    return count
                    
result = 0
for i in range(n):
    for j in range(m):
        now = graph[i][j]
        if now and not visited[i][j]:
           
            result = max(result, dfs([i, j]))
           
print(result)