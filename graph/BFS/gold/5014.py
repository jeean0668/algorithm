"""
간단한 bfs문제였는데, 목표 지점에 도달했을때 distance 값을 반환해야 한다는
점을 놓치고 말았다. 
아직은 bfs 알고리즘에 익숙하지 않다. gold 문제를 더 풀어서 익숙하게 만들어야겠다.

"""

import sys
from collections import deque
input = sys.stdin.readline
F, S, G, U, D = map(int, input().split())
INF = sys.maxsize
dist = [INF for _ in range(F+1)]
visited = [False for _ in range(F+1)]
def bfs(start):
    q = deque()
    q.append(start)
    dist[start] = 0
    visited[start] = True
    while q:
        now = q.popleft()
        up = now + U
        down = now - D
        if now == G:
            return dist[now]
        if 0 < up <= F and not visited[up]:
            dist[up] = dist[now] + 1
            visited[up] = True
            q.append(up)
        if 0 < down <= F and not visited[down]:
            dist[down] = dist[now] + 1
            visited[down] = True
            q.append(down)
    return -1
            
result = bfs(S)
if result == -1:
    print("use the stairs")
else:
    print(result)