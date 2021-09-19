

import sys
from collections import deque
input = sys.stdin.readline
dy = [0, 0, 1, -1, 0, 0]
dx = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
INF = sys.maxsize

def getInput():
    global L,R,C,graph
    graph = []
    s_pos = []
    L, R, C = map(int ,input().split())
    if L == 0 and R == 0 and C == 0:
        return -1
    for i in range(L):
        row = []
        for j in range(R):
            string = list(input().rstrip())
            for k in range(len(string)):
                s = string[k]
                if s == "S":
                    s_pos = [i, j, k]
            row.append(string)
        graph.append(row)

        print()
    return s_pos
def bfs(start):
    global L, R, C, graph
    q = deque()
    visited = [[[False] * (C+1)] * (R+1)] * (L+1)
    dist =  [[[INF] * (C+1)] * (R+1)] * (L+1)
    
    q.append(start)
    dist[start[0]][start[1]][start[2]] = 0
    visited[start[0]][start[1]][start[2]] = True
    while q:
        now_h, now_y, now_x = q.popleft()

        if graph[now_h][now_y][now_x] == "E":
            return dist[now_h][now_y][now_x]
        for i in range(6):
            nh = now_h + dz[i]
            ny = now_y + dy[i]
            nx = now_x + dx[i]
            if 0<=nh<L and 0<=ny<R and 0<=nx<C:
                if visited[nh][ny][nx]:
                    continue
                if graph[nh][ny][nx] == '#':
                    continue
                visited[nh][ny][nx] = True
                print(nh, ny, nx)
                if dist[nh][ny][nx] > dist[now_h][now_y][now_x] + 1:
                    dist[nh][ny][nx] = dist[now_h][now_y][now_x] + 1
                q.append([nh, ny, nx])
    return -1            
    
if __name__ == "__main__":
    while True:
        start = getInput()
        print(start)
        if start == -1:
            break
        result = bfs(start)
        if result == -1:
            print("Trapped!")
        else:
            print("Excaped in {} minutes(s)".format(result))