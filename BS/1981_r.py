"""
집배원 한상덕 문제와 똑같은 문제
1. 이분 탐색으로 최고, 최저점 차이를 tmp로정해놓는다.
2. for 문으로 (0, 0 + tmp), (1, 1 + tmp) 구간을 통과할 수 있는지 bfs로 탐색한다.
3. 탐색할 수 있으면 True를 반환한다. 
"""

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dy = [-1, 0, 0, 1]
dx = [0, 1, -1, 0]

def bfs(s, e):
    # bfs로 graph를 탐색하여, 최고 높이와 최저 높이의 차가 v 이하면 이동
    if graph[0][0]<s or graph[0][0]>e:
        return False
    queue = deque()
    
    queue.append((0, 0))
    visited = [[False for _ in range(n+1)] for _ in range(n+1)]
    visited[0][0] = True
    
    while queue:
        y, x= queue.popleft()
        if y == n-1 and x == n-1:
            return True
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not(0<=ny<n and 0<=nx<n):
                continue
            if visited[ny][nx]:
                continue
            if s <= graph[ny][nx] <= e:
                visited[ny][nx] = True
                queue.append((ny, nx))
    return False
left, right = 0, 200
ans = 200

def isPossible(v):
    for i in range(200):
        if bfs(i, i+v):
            return True
    return False
while left <= right:
    mid = (left + right) // 2
    if isPossible(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)