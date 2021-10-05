"""
타일 기준으로 대각선, 동서남북으로 8방향에 물인 타일의 갯수가 
현재 타일의 값보다 크면 무너진다.


처음에는 for루프로 전부 순회해주었다가 시간초과가 났다.
. 으로 시작하는 모든 점을 queue에 넣고 시작해서 해결되었다.
queue에서 나온 값이 0 ( == '.') 이면, 주변에 있는 숫자 타일 - 1을
해주었다. 숫자 타일 - 1 한 결과가 0이면, queue에 그 타일을 삽입하고
cnt += 1 해주었다.


"""
import sys
from collections import deque
from copy import deepcopy

dirs = [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1) ]

def getInput():
    global graph, h, w, queue

    graph = []
    h, w = map(int, input().split())
    queue = deque()
    graph = [list(input()) for _ in range(h)]
    for i in range(h):
        for j in range(w):
    
            if graph[i][j] == '.':
                graph[i][j] = 0
                # 비어있는 부분의 위치를 모두 큐에 삽입 
                queue.append((i, j))
            else:
                graph[i][j] = int(graph[i][j])
def bfs():
    global h, w, graph, queue, answer

    visited = [[0 for _ in range(w + 1)] for _ in range(h + 1)]
    answer = 0

    while queue:
        y, x, = queue.popleft()
        for mv in dirs:
            ny, nx = y + mv[0], x + mv[1]
            if 0 <= ny < h and 0 <= nx < w:
                if graph[ny][nx] != 0:
                    graph[ny][nx] -= 1
                    if graph[ny][nx] == 0:
                        visited[ny][nx] = visited[y][x] + 1
                        answer = max(answer, visited[ny][nx])
                        queue.append((ny, nx))

def solve():
    # bfs로 .과 인접한 임시타일에 + 1 해준다.
    global answer
    bfs()
    print(answer)
   

if __name__ == "__main__":
    getInput()
    solve()