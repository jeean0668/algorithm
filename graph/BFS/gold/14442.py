"""
(1, 1) 부터 (N, M) 까지의 최단거리 
단 K개까지 벽을 부수면서 갈 수 있다.
이동할 수 있는 칸은 상하좌우로 인접한 칸이고, 불가능하면 -1 출력

bfs로 경로를 탐색한다.
-> queue에 (y, x, cnt) 를 삽입한다. 
-> visited를 삼중 배열로 선언 => visited[k][n][m]
-> 다음 경로가 벽(1) 일때 cnt가 K보다 작으면, queue에 벽으로 가는
경로와 가지 않는 경로 두가지를 삽입한다. 
-> 아니라면 그냥 경로만 삽입한다. 
"""
from collections import deque
import sys
input = sys.stdin.readline
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]
INF = sys.maxsize

def getInput():
    global n, m, k, graph
    n, m, k = map(int, input().split())
    graph = [list(map(str, input().rstrip())) for _ in range(n)]
  
def solve():

    global n, m, k, graph
    sy, sx = 0, 0

    visited = [[[INF for _ in range(m + 1)] for _ in range(n+1)] for _ in range(k + 1)]
    
    queue = deque()
    dist = 0

    queue.append((sy, sx, 0))
    visited[0][0][0] = 1
    while queue:
        y, x, cnt = queue.popleft()
        if y == n-1 and x == m-1:
            return visited[cnt][n-1][m-1]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
            
                if graph[ny][nx] == '1' and cnt < k:
                    if visited[cnt + 1][ny][nx] > visited[cnt][y][x] + 1:
                        visited[cnt + 1][ny][nx] = visited[cnt][y][x] + 1
                        queue.append((ny, nx, cnt + 1))
                elif graph[ny][nx] == '0':
                    if visited[cnt][ny][nx] > visited[cnt][y][x] + 1:
                        visited[cnt][ny][nx] = visited[cnt][y][x] + 1
                        queue.append((ny, nx, cnt))
    return -1 
    
if __name__ == "__main__":
    getInput()
    print(solve())

