"""
[i,j]에 물이 도달하는 시간을 기록하고(by bfs), 고슴도치가 [i,j]에 도달하는 시간이 물이 도달하는 시간
보다 작다면 이동한다.(bfs)
세부 구현이 까다로웠다. string과 integer를 왔다갔다 하는 알고리즘을 짜서 시간이 걸렸다.
알고리즘 자체는 어렵지 않았다.
"""

import sys
from collections import deque
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
 
R, C = map(int, input().split())
arr = []
for _ in range(R):
    arr.append(list(input().rstrip()))
visited = [[False]*C for _ in range(R)]
queue = deque()
for i in range(R):
    for j in range(C):
        if arr[i][j] == "D":
            goal = [i, j]
            arr[i][j] = sys.maxsize
        elif arr[i][j] == "S":
            start = [i, j, 0]
            arr[i][j] = "."
        elif arr[i][j] == "*":
            arr[i][j] = 0
            queue.append([i, j, 0])
        elif arr[i][j] == "X":
            visited[i][j] = True
 
# 물 차는 시간 UPDATE
while queue:
    x, y, cnt = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] == ".":
            arr[nx][ny] = cnt+1
            queue.append([nx, ny, cnt+1])
 
# 고슴도치 이동
queue.append(start)
flag = False
visited[start[0]][start[1]] = True
while queue:
    x, y, cnt = queue.popleft()
    if [x, y] == goal:
        flag = True
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
            if arr[nx][ny] == "." or arr[nx][ny] > cnt+1:
                visited[nx][ny] = True
                queue.append([nx, ny, cnt+1])
 
if flag:
    print(cnt)
else:
    print("KAKTUS")