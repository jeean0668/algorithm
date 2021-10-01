# -*- coding: utf-8 -*-
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
        row = map(int, input().split())
        graph.append(row)
def getInput():
    global n
    n = int(input())
    makeGraph(n)
def changeMap(sy, sx, cnt):
    # 연결된 모든 지역의 숫자를 cnt로 바꿔준다.
    global visited, n
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
            if not visited[ny][nx] and not graph[ny][nx] != 0:
                graph[ny][nx] = cnt
                queue.append([ny,nx])
                visited[ny][nx] = True

def solve():
    # 맵을 1, 2, 3.. 번호를 붙인다.
    global visited
    visited = [[False for _ in range(n+1)] for _ in range(n+1)]
    cnt = 1
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 and not visited[i][j]:
                changeMap(i, j, cnt)
                cnt += 1
    print(changeMap)