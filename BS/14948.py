import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
left, right = 0, 0
dy = [-1, 0, 0, 1]
dx = [0, 1, -1, 0]
graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    right = max(max(row), right)
    graph.append(row)

def isPossible(v):
    # bfs로 탐색하여 v 이하로 (0,0) -> (n-1,m-1)까지 갈수 있으면 True
    
    queue = deque()
    queue.append((0,0,1))
    visited = [[False for _ in range(m+1)] for _ in range(n+1)]
    if graph[0][0] <= v:
        visited[0][0] = True
    else:
        return False
    while queue:
        y, x, chance = queue.popleft()
        
        if y == n-1 and x == m-1: return True
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
           
            if not(0<=ny<n and 0<=nx<m): continue
            if visited[ny][nx] : continue
            if y == 7 and x == 9:
                print(chance, ny, nx, visited[ny][nx], graph[ny][nx], v)
            if graph[ny][nx] > v:
                if y == 7 and x == 9:
                    print(chance, ny, nx, visited[ny][nx])
                if chance == 0 : continue
                ny, nx = ny + dy[i], nx + dx[i]
                if y == 7 and x == 9:
                    print(chance, ny, nx, visited[ny][nx])
                if not(0<=ny<n and 0<=nx<m) : continue
                if graph[ny][nx] > v: continue
                queue.append((ny, nx, chance - 1))
                visited[ny][nx] = True
            else:
                queue.append((ny, nx, chance))
                visited[ny][nx] = True
    return False
    
ans = right
while left <= right:
    mid = (left + right) // 2
    if isPossible(mid):
        ans = min(ans, mid)
        
        right = mid - 1
    else:
        left = mid + 1
print(ans)
