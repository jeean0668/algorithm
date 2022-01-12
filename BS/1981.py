import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n = int(input())
small, big = 201, 0
graph = []
dict = defaultdict(int)
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]
for _ in range(n):
    row = list(map(int, input().split()))
    for r in row:
        dict[r] += 1 
        if r < small : small = r
        elif r > big : big = r
    graph.append(row)

arr = sorted(list(dict.keys()))

def bfs(left, right):
    queue = deque()
    visited = [[False for _ in range(n+1)] for _ in range(n+1)]
    if not(left <= graph[0][0] <= right):
        return
    visited[0][0] = True
    queue.append((0, 0))
    
    while queue:
        y, x = queue.popleft()
        if y == n-1 and x == n-1:
            return True
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not(0<=ny<n and 0<=nx<n):
                continue
            if visited[ny][nx]:
                continue
            if left <= graph[ny][nx] <= right:
                queue.append((ny,nx))
                visited[ny][nx] = True
    return False
left, right = 0, 200


ans = 0
def possible(value):
    for i in range(0, 200):
        if bfs(i, i+value):
            return True
    return False
while left <= right:
    mid = (left + right) // 2
    if possible(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)