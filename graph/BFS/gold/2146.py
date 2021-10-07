# -*- coding: utf-8 -*-
"""
type error 이유가 뭐냐 대체 -> 병신같이 input에 list를 안붙여줘서 2시간이나 헤맸다
시발 진짜 뭐하는짓이지? 
"""
import sys
input = sys.stdin.readline
from collections import deque
dy = [-1, 0 ,0, 1]
dx = [0, -1, 1, 0]

def makeGraph(n):
    global graph
    graph = []
    # n x n 맵 생성
    for _ in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

def getInput():
    global n
    n = int(input())
    makeGraph(n)

def changeMap(sy, sx):
    # 연결된 모든 지역의 숫자를 cnt로 바꿔준다.
    global visited, n, cnt
    queue = deque()
    queue.append([sy, sx])
    graph[sy][sx] = cnt
    visited[sy][sx] = True

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not(0<=ny<n and 0<=nx<n):
                continue
            if graph[ny][nx] != 1:
                continue
            if not visited[ny][nx] :
                graph[ny][nx] = cnt
                queue.append([ny,nx])
                visited[ny][nx] = True
def findShortest(num):
    # num 번째 island에서 다른 섬을 잇는 가장 짧은 길이의 다리를 반환한다.
    global n, result
    distance = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    queue = deque()

    for i in range(n):
        for j in range(n):
            # 연결된 모든 지역들을 queue에 넣는다. 
            if graph[i][j] == num:
                queue.append([i, j])
                distance[i][j] = 0

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not(0<=ny<n and 0<=nx<n):
                continue
            if graph[ny][nx] > 0 and graph[ny][nx] != num:
                result = min(result, distance[y][x])
                return 
            if graph[ny][nx] == 0 and distance[ny][nx] == -1:
                distance[ny][nx] = distance[y][x] + 1
                queue.append([ny, nx])


def solve():
   
    global visited, result, cnt
    visited = [[False for _ in range(n+1)] for _ in range(n+1)]
    cnt = 1

     # 맵을 1, 2, 3.. 번호를 붙인다.
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 and not visited[i][j]:
                changeMap(i, j)
                cnt += 1
   
     # 특정 섬과 다른 섬, 두 섬 사이의 최단 거리를 구한다.
    # 모든 섬에서 다른 섬들을 잇는 가장 짧은 다리의 길이를 구한다. 
    result = sys.maxsize
    for i in range(1, cnt):
        findShortest(i)
    print(result)
    
if __name__ == "__main__":
    getInput()
    solve()