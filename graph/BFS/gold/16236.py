# -*- coding: utf-8 -*-

import sys
from collections import deque
input = sys.stdin.readline
dy = [-1, 0, 0, 1]
dx = [0, 1, -1, 0]

def makeGraph(n):
    global graph, start
    graph = []
    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(len(row)):
            if row[j] == 9:
                start = [i,j]
                row[j] = 0 
        graph.append(row)

def bfs(start):
    # start에서 출발하여 먹을 수 있는 물고기들을 찾는다. 
    global n, fishes, size
    queue = deque()
    queue.append([0, start[0], start[1]])
    visited = [[False for _ in range(n+1)] for _ in range(n+1)]

    flag = sys.maxsize
    
    while queue:
       
        cnt, y, x = queue.popleft()
        if cnt > flag:
            break
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not(0<=ny<n and 0<=nx<n):
                continue
            if visited[ny][nx] or graph[ny][nx] > size:
                continue
            if 0 < graph[ny][nx] < size:
                fishes.append([cnt + 1, ny, nx])
                flag = cnt
            queue.append([cnt + 1, ny, nx])
            visited[ny][nx] =  True

def findShortest(start, size):
    # bfs로 가장 가까우면서 먹을 수 있는 물고기를 찾는다.
    global fishes
    fishes = []
    bfs(start)
    if len(fishes) == 0:
        return -1
   
    fishes.sort() # 오름차순 정렬하면 거리 순, 행 순, 열 순으로 오름차순 정렬된다.
    

    return fishes[0]


def solve():
    global start, size
    size = 2
    cnt = 0
    total_move = 0
    _next = []
    while True:
        _next = findShortest(start, size)
       
        if _next == -1:
            break
        total_move += _next[0]
        graph[_next[1]][_next[2]] = 0
        start = [_next[1], _next[2]]
        cnt += 1
        if cnt == size:
            size += 1
            cnt = 0
    print(total_move)

if __name__ == "__main__":
    n = int(input())
    makeGraph(n)
    solve()
        
