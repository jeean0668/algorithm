"""
dynamic 프로그래밍으로 추정된다.
1. c[y][x] = max(c[y][x], dfs(ny,nx)+1)
2. 처음에 INF값을 너무 작게 줘서 틀렸다. INF값만 키워주니까 맞았다.
3. cycle을 판단할때, 1) 이미 방문한 점인데, 2) 탐색이 끝나지 않았던 점이면 
cycle로 판단했다. 
"""

# 전역변수 선언
import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)
graph = []
INF = 100000
def makeGraph(n):
    for _ in range(n):
        row = list(input().strip())
        # H 를 -1로 바꾼다
        new_row = []
        for r in row:
            if r == "H":
                new_row.append(-1)
            else:
                new_row.append(int(r))
        graph.append(new_row)
        
def dfs(y, x):
    global c
    global visited
    
    if c[y][x] != 0:
        return c[y][x]
   
    dy = [graph[y][x], 0, 0, -graph[y][x]]
    dx = [0, graph[y][x], -graph[y][x], 0]
   
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if 0<=ny<n and 0<=nx<m:
            
            if graph[ny][nx] == -1:
                # 다음 타일이 H 타일일 경우 
                continue
            if visited[ny][nx] and not finished[ny][nx]:
                # cycle이 존재할 경우 
                return INF
            visited[y][x] = True
            c[y][x] = max(c[y][x], dfs(ny, nx) + 1) 
            visited[y][x] = False
    finished[y][x] = True
           
    return c[y][x]

if __name__ == "__main__":
    n, m = map(int, input().split())
    makeGraph(n)
    c = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m+1)] for _ in range(n+1)]
    finished = [[False for _ in range(m+1)] for _ in range(n+1)]
    visited[0][0] = True
    temp = dfs(0, 0)
    if temp >=INF:
        print(-1)
    else:
        print(temp + 1)
        