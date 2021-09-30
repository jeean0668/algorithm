import sys
from collections import deque
input = sys.stdin.readline
dy = [-1, 0, 0, 1, 1, -1, 1, -1, 0]
dx = [ 0, -1, 1, 0, 1, -1, -1, 1, 0]

graph = []
for _ in range(8):
    row = list(map(str, input().rstrip()))
    graph.append(row)


#print(new_graph[0][5], new_graph[0][6]. new_graph[0][7])
#print(new_graph[1][5], new_graph[1][6], new_graph[1][7])
def bfs():
    queue = deque()
    queue.append([7, 0, 0]) # y, x, seconds
    visited = [[[False for _ in range(9)] for _ in range(9)] for _ in range(9)]
    while queue:
        y, x, sec = queue.popleft()
        if y == 0 and x == 7:
            return 1
        for i in range(9):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<8 and 0<=nx<8:
                if visited[sec][ny][nx]:
                    continue
                # 벽으로 못갈때
                if ny - sec >= 0:
                    if graph[ny - sec][nx] == "#" and ny - sec >= 0:
                        continue
                # 내가 갈 곳이 바로 다음에 벽이 내려올 곳일 때
                if ny - sec - 1 >= 0:
                    if graph[ny - sec - 1][nx] == "#" and ny - sec - 1 >= 0:
                        continue
               
                queue.append([ny, nx, min(8, sec + 1)])
                visited[sec][ny][nx] = True

    return 0

result = bfs()
print(result)