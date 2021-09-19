"""
1차 시도. 0(바다) 를 기준으로 주변에 0이 아닌 타일이 있으면 하나씩 빼주는 방식으로 접근 했다 -> 빙산으로 둘러쌓인 타일 0에 의한 계산이 불가능했다. 
2차 시도. 0이 아닌 타일을 기준으로, 동서남북으로 0 타일이 있으면 그 갯수 만큼 
타일을 빼준다. -> 답은 맞게 나오는데 recursionError가 뜬다. 
3차 시도 -> DFS는 recursionError가 뜨므로, bfs로 푼다.

"""

import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
graph = []
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]
visited = [[False] * m for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))

def dfs(y, x):
    # 0이 아닌 타일들을 탐색하고, 접해있는 0의 갯수만큼 빼주는 함수
    global visited
    visited[y][x] = True
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<n and 0<=nx<m:
            if graph[ny][nx] == 0:
                if graph[y][x] > 1:
                    graph[y][x] -=1
                else:
                    graph[y][x] = -1
            elif graph[ny][nx] > 0 and not visited[ny][nx]:
                dfs(ny, nx)
def cover():
    # -1로 된 타일을 0으로 바꿔주는 함수
    for i in range(n):
        for j in range(m):
            if graph[i][j] == -1:
                graph[i][j] = 0
def divided(y, x):
    # 그래프가 두 집합 이상으로 분리되었는지 검사하는 함수
    global checked
    checked[y][x] = True
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<n and 0<=nx<m and not checked[ny][nx] and graph[ny][nx] != 0:
            divided(ny,nx)
cnt = 0
while True:
   
    checked = [[False] * m for _ in range(n)]
    temp = 0
    for i in range(1, n):
        for j in range(1, m):
            if not checked[i][j] and graph[i][j] > 0:
                if temp >= 1:
                    temp += 1
                    break
                divided(i, j)
                temp += 1
    #print(graph, cnt, temp)
    if temp > 1:
        print(cnt)
        exit()
    elif temp == 0:
        print(0)
        exit()
        
    visited = [[False] * m for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            if graph[i][j] != 0 and not visited[i][j]:
                dfs(i, j)
    cover()
    cnt += 1
    
    
    
    
        