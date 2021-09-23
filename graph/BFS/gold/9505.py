
"""
bfs -> 시간초과 발생( 시간복잡도 : O(N^2))
heapq를 활용한 다익스트라로 해결 ( 시간복잡도 : O(NlogN))
다익스트라로 해결하는것도 문제가 있었다
가장 먼저 가장자리에 도달하는점 -> 최솟값을 갖는다! -> 시간복잡도를 줄인다. 
"""

import sys
from collections import deque
import heapq
input = sys.stdin.readline
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

def bfs(s_point, classes, graph):
    
    c = [[sys.maxsize for _ in range(W+1)] for _ in range(H+1)]
    queue = []
    heapq.heappush(queue, [0, s_point])
    
    while queue:
        length, now = heapq.heappop(queue)
        y, x = now[0], now[1]
        if y == 0 or y == H-1 or x == 0 or x == W-1:
            print(y,x)
            return c[y][x]
        if c[y][x] < length:
            continue
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny<0 or ny>=H or nx<0 or nx>=W:
                continue
            dist = length + classes[graph[ny][nx]]
            if c[ny][nx] > dist:
                c[ny][nx] = dist
                heapq.heappush(queue, [dist, [ny, nx]])

T = int(input())

for _ in range(T):
    K, W, H = map(int, input().split())
    classes = {}
    for _ in range(K):
        c, value = input().split()
        classes[c] = int(value)
    classes['E'] = 0
    graph = []
    start = []
    for i in range(H):
        row = list(input().rstrip())
        graph.append(row)
    for i in range(H):
        for j in range(W):
            if graph[i][j] == "E":
                result = bfs([i,j], classes, graph)
                break
    print(result)

