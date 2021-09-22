"""
1. 몇분 후에 물이 도달하는지 bfs로 지도에 기록한다. 
2. S부터 D까지 bfs로 탐색하면서, 돌이 있거나, depth가 map에 기록된 값 이상이라면 
pass한다.
"""

import sys
from collections import deque
from copy import deepcopy
from types import WrapperDescriptorType
input = sys.stdin.readline
graph = []
water_graph = []
dy = [-1, 0, 0, 1]
dx = [0, 1, -1, 0]
INF = sys.maxsize

def record_change():
    # 물이 도달하는 시간을 기록한 map
    global start_p, end_p, water_p, r, c
    queue = deque()
    queue.append([water_p, 0])
    visited = [[False for _ in range(c+1)] for _ in range(r+1)]
    # 시작점 초기화 
    visited[water_p[0]][water_p[1]] = True
    water_graph[water_p[0]][water_p[1]] = 0
    # bfs 시작
    while queue:
        now_water, arrival = queue.popleft()
        y, x = now_water[0], now_water[1]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<r and 0<=nx<c:
                
                if visited[ny][nx]:
                    continue
                if graph[ny][nx] == "X" or graph[ny][nx] == "D":
                    continue
                water_graph[ny][nx] = arrival + 1
                visited[ny][nx] = True
                queue.append([[ny, nx], arrival + 1])

def makeGraph(row_num):
    global water_graph, start_p, end_p, water_p
    for i in range(row_num):
        row = list(input().rstrip())
        for j in range(len(row)):
            s = row[j]
            if s == "S":
                start_p = [i, j]
            elif s == "D":
                end_p = [i, j]
            elif s == "*":
                water_p = [i, j]
        graph.append(row)
    water_graph = deepcopy(graph)
    water_graph[end_p[0]][end_p[1]] = INF
    for i in range(row_num):
        for j in range(len(graph[i])):
            if water_graph[i][j] == "X":
                water_graph[i][j] = -1

def getInput():
    global r, c, water_graph
    r, c = map(int, input().split())
    makeGraph(r)
    record_change()
    print(water_graph)

def solve():
    #water graph 값보다 작으면 이동한다.
    global graph, water_graph, start_p, r, c
    queue = deque()
    visited = [[False for _ in range(c+1)] for _ in range(r+1)]
    visited[start_p[0]][start_p[1]] = True
    queue.append([start_p, 0])
    result = 0
    while queue:
        now_pos, now_time = queue.popleft()
        y, x = now_pos[0], now_pos[1]
        if water_graph[y][x] >= INF:
            result = now_time
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<r and 0<=nx<c:
                if visited[ny][nx]:
                    continue
                if water_graph[ny][nx] == -1:
                    continue
                if water_graph[ny][nx] <= now_time+1:
                    continue
                visited[ny][nx] = True
                queue.append([[ny, nx], now_time + 1])
    if result:
        print(result)
    else:
        print("KAKTUS")
                
#main
if __name__ == "__main__":
    getInput()
    solve()