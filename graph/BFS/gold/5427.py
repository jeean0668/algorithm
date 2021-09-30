import sys
from collections import deque
input = sys.stdin.readline
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]
graph = []

def getInput():
    global graph
    graph = []
    w, h = map(int, input().split())
    fires, start = [], []
    for i in range(h):
        row = list(map(str, input().rstrip()))
        for j in range(len(row)):
            if row[j] == "*":
                fires.append([i, j])
            if row[j] == "@":
                start = [i, j]
                row[j] = 0
            if row[j] == ".":
                row[j] = 0
        graph.append(row)
    return h, w, start, fires
def changeGraph(fires, h, w):
    global graph
    visited = [[False for _ in range(w)] for _ in range(h)]
    queue = deque()
    while fires:
        fire = fires.pop()
        graph[fire[0]][fire[1]] = 1
        visited[fire[0]][fire[1]] = True
        queue.append([fire[0], fire[1]])
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<h and 0<=nx<w:
                if graph[ny][nx] == "#":
                    continue
                if visited[ny][nx]:
                    continue
                if graph[ny][nx] == 0:
                    graph[ny][nx] = graph[y][x] + 1
                    queue.append([ny, nx])

def BFS(start, h, w):
    global graph
    visited = [[False for _ in range(w+1)] for _ in range(h+1)]
    queue = deque()
    start = [start[0], start[1], 1]
    queue.append(start)
    visited[start[0]][start[1]] = True
   
    while queue:
        y, x, count = queue.popleft()
        if y == 0 or y == h-1 or x == 0 or x == w-1:
            return count
            
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<h and 0<=nx<w:
                if graph[ny][nx] == "#":
                    continue
                if visited[ny][nx]:
                    continue
                #print(ny, nx, graph[ny][nx], count)
                
                if graph[ny][nx] - 1 > count or graph[ny][nx] == 0:
                    queue.append([ny, nx, count + 1])
                    visited[ny][nx] = True
    return "IMPOSSIBLE"
       
if __name__ == "__main__":
    tests = int(input())
    while tests > 0:
        h, w, start, fires = getInput()
        changeGraph(fires, h, w)
        print(BFS(start, h, w))
        tests -= 1