"""
말로 이동할 수 있는 횟수가 넘지 않았다 -> queue에 말로 이동했을 때와 원숭이로 이동했을 때를 추가한다.
이동할 수 있는 횟수가 소진되었다 -> 원숭이로 이동한다.
3d array로 특정 좌표에 도달하기 까지 말을 몇번 탔는지 기록하는 것이 포인트다. 
"""


import sys
from collections import deque
input = sys.stdin.readline
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]
horse = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

k = int(input())
W, H = map(int, input().split())
graph = []
for _ in range(H):
    row = list(map(int, input().split()))
    graph.append(row)
start, end = [0,0], [H-1, W-1]
distance = [[[0 for _ in range(k+2)] for _ in range(W+1)] for _ in range(H+1)]

def bfs(start, end):
    q = deque()
    q.append([start, 0])
    distance[start[0]][start[1]][0] = 1
    flag = True
    while q:
        now, count = q.popleft()
        y, x = now[0], now[1]
        
        if y == end[0] and x == end[1]:
            return distance[y][x][count] - 1
           
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if not(0<=ny<H and 0<=nx<W):
                continue
            if graph[ny][nx] == 0 and distance[ny][nx][count] == 0:
                distance[ny][nx][count] = distance[y][x][count] + 1
                q.append([[ny, nx], count])
        if count < k:
            for mv in horse:
                ny = y + mv[0]
                nx = x + mv[1]
            
                if not(0<=ny<H and 0<=nx<W) or graph[ny][nx] == 1:
                    continue
                if distance[ny][nx][count+1] == 0 and graph[ny][nx] == 0:
                    distance[ny][nx][count + 1] = distance[y][x][count] + 1
                    q.append([[ny, nx], count + 1])
            
    return -1

result = bfs(start, end)
print(result) 

