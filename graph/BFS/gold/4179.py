"""
3055번이랑 비슷한 문제인데, 각 모서리들이 도착지점이 될 수 있다는 것이 다른점이다.
"""

import sys
from collections import deque
input = sys.stdin.readline
graph = []
dy = [-1, 0, 0, 1]
dx = [0, 1, -1, 0]

def getInput():
    global s_p, f_p, n, m
    f_p= []
    n, m = map(int, input().split())
    for i in range(n):
        row = list(input().rstrip())
        graph.append(row)
        for j in range(len(row)):
            s = row[j]
            if s == 'J':
                s_p = [i, j]
                graph[i][j] = '.'
            elif s == 'F':
                f_p.append([i, j])
                graph[i][j] = 0
def solve():
    global s_p, f_p, graph, n, m
    visited = [[False for _ in range(m+1)] for _ in range(n+1)]
    queue1 = deque()
    while len(f_p) > 0:
        pos = f_p.pop()
        pos_y, pos_x = pos[0], pos[1]
        visited[pos_y][pos_x] = True
        queue1.append([pos_y, pos_x, 1])
    
    # 불이 지나가는 시간으로 초기화
    while queue1:
        y, x, cnt = queue1.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<m and graph[ny][nx] == '.':
                graph[ny][nx] = cnt + 1
                queue1.append([ny, nx, cnt + 1])
                
    # 불이 지나가기 전에 갈 수 있는 경로를 탐색한다.
    visited = [[False for _ in range(m+1)] for _ in range(n+1)] 
    queue2 = deque()
    queue2.append([s_p[0], s_p[1], 1])
    visited[s_p[0]][s_p[1]] = True
    result = 0
    while queue2:
        y, x, cnt = queue2.popleft()
        if y <= 0 or y >= n-1 or x <= 0 or x >=m-1:
            result = cnt
            return result
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if visited[ny][nx]:
                continue
            if graph[ny][nx] == "#":
                continue
            if graph[ny][nx] == '.' or graph[ny][nx] > cnt+1:
                visited[ny][nx] = True
                queue2.append([ny, nx, cnt+1])
    return result



if __name__ == "__main__":
    getInput()
    result = solve()
    if not result:
        print("IMPOSSIBLE")
    else:
        print(result)