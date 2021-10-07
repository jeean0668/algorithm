# -*- coding: utf-8 -*-
import sys
from collections import deque
input = sys.stdin.readline


def getInput():
    global n, graph, start, end, end_dir
    n = int(input())
    graph = []
    start, end = [], []
    for i in range(n):
        row = list(map(str, input().rstrip()))
        graph.append(row)
        for j in range(len(row)):
            if graph[i][j] == "B":
                start.append([i, j])
            elif graph[i][j] == "E":
                end.append([i, j])
    if end[0][0] - end[1][0] == 1:
        end_dir = 1
    else:
        end_dir = 0
def canmoveRight(center, dir):
    global graph
    
    # horizontal 할 경우
    if dir == 0:
        first_y, first_x = center[0], center[1] - 1
        last_y, last_x = center[0], center[1] + 1
        if not(0<= last_x + 1 < n):
            return False
        if graph[last_y][last_x + 1] == '1':
            return False
        return True
    # vertical 할경우
    elif dir == 1:
        first_y, first_x = center[0]-1, center[1]
        last_y, last_x = center[0]+1, center[1]
        if not(0<=first_x+1<n or 0<=center[1]+1<n or 0<=last_x+1<n):
            return False
        if graph[first_y][first_x + 1] == '1' or graph[center[0]][center[1] + 1] == '1' or graph[last_y][last_x + 1] == '1':
            return False
        return True
    
def canmoveLeft(center, dir):
    global graph
    
    # horizontal 할 경우
    if dir == 0:
        first_y, first_x = center[0], center[1] - 1
        last_y, last_x = center[0], center[1] + 1
        if not(0<=first_x-1<n):
            return False
        if graph[first_y][first_x - 1] == '1':
            return False
        return True
    # vertical 할경우
    elif dir == 1:
        first_y, first_x = center[0]-1, center[1]
        last_y, last_x = center[0]+1, center[1]
        if not(0<=first_x-1<n or 0<=center[1]-1<n or 0<=last_x-1<n):
            return False
        if graph[first_y][first_x - 1] == '1' or graph[center[0]][center[1] - 1] == '1' or graph[last_y][last_x - 1] == '1':
            return False
        return True
def canRotate(center, dir):
    if dir == 0:
        first_y, first_x = center[0], center[1] - 1
        last_y, last_x = center[0], center[1] + 1
        if not(0<=first_y-1<n or 0<=center[0]-1<n or 0<=last_y-1<n):
            return False
        if not(0<=first_y+1<n or 0<=center[0]+1<n or 0<=last_y+1<n):
            return False
        if graph[first_y-1][first_x] == '1' or graph[center[0]-1][first_x] == '1' or graph[last_y - 1][last_x] == '1':
            return False
        if graph[first_y+1][first_x] == '1' or graph[center[0]+1][first_x] == '1' or graph[last_y + 1][last_x] == '1':
            return False
    if dir == 1:
        first_y, first_x = center[0]-1, center[1]
        last_y, last_x = center[0]+1, center[1]
        if not(0<=first_x-1<n or 0<=center[1]-1<n or 0<=last_x-1<n):
            return False
        if not(0<=first_x+1<n or 0<=center[1]+1<n or 0<=last_x+1<n):
            return False
        if graph[first_y][first_x-1] == '1' or graph[center[0]][center[1]-1] == '1' or graph[last_y][last_x-1] == '1':
            return False
        if graph[first_y][first_x+1] == '1' or graph[center[0]][center[1]+1] == '1' or graph[last_y][last_x+1] == '1':
            return False
        
def canmoveUp(center, dir):
    global graph
    
    # vertical 할경우
    if dir == 1:
        first_y, first_x = center[0]-1, center[1]
        last_y, last_x = center[0]+1, center[1]
        if not(0<=first_y-1<n):
            return False
        if graph[first_y - 1][first_x] == '1':
            return False
        return True
    #horizontal 할 경우
    elif dir == 0:
        first_y, first_x = center[0], center[1] - 1
        last_y, last_x = center[0], center[1] + 1
        if not(0<=first_y -1 < n or 0<=center[0] - 1 <n or 0<=last_y-1<n):
            return False
        if graph[first_y - 1][first_x] == '1' or graph[center[0] - 1][center[1]] == '1' or graph[last_y - 1][last_x] == '1':
            return False
        return True

def canmoveDown(center, dir):
    global graph
    # vertical 할경우
    if dir == 1:
        first_y, first_x = center[0]-1, center[1]
        last_y, last_x = center[0]+1, center[1]

        if not(0<=last_y+1<n):
            return False
        if graph[last_y + 1][last_x] == '1':
            return False
        return True
    #horizontal 할 경우
    elif dir == 0:
        first_y, first_x = center[0], center[1]-1
        last_y, last_x = center[0], center[1]+1
        if not(0<=first_y+1<n or 0<=center[0]+1<n or 0<=last_y+1<n):
            return False
        if graph[first_y + 1][first_x] == '1' or graph[center[0] + 1][center[1]] == '1' or graph[last_y + 1][last_x] == '1':
            return False
        return True
def solve():
    global n, graph, start, end, end_dir
    queue = deque()
    # visited는 [center y][center x][vertical or horizontal] 로 선언
    visited = [[[False for _ in range(2)] for _ in range(n+1)] for _ in range(n+1)]
    # 시작을 horizontal하게 시작할때 
    if abs(start[0][0] - start[1][0])== 1:
        queue.append([start[1], 0, 1])
        visited[start[1][0]][start[1][1]][1] = True
    elif abs(start[0][1] - start[1][1]) == 1:
        queue.append([start[1], 0, 0])
        visited[start[1][0]][start[1][1]][0] = True
    
    while queue:
        center, cnt, dir = queue.popleft() # center 좌표, 갯수, 누워있는 방향
        y, x = center[0], center[1]
        print(y, x, dir)
        if y == end[1][0] and x == end[1][1] and dir == end_dir:
            return cnt
        
        if canmoveLeft(center, dir):
            
            ny, nx = y, x-1
            if 0<=ny<n and 0<=nx<n:
                if ny == 12 and nx == 10:
                    print(y, x, ny, nx, dir)
                if not visited[ny][nx][dir]:
                    queue.append([[ny, nx], cnt + 1, dir])
                    visited[ny][nx][dir] = True
        if canmoveRight(center, dir):

            ny, nx = y, x+1
            if 0<=ny<n and 0<=nx<n:
                if ny == 12 and nx == 10:
                    print(y, x, ny, nx, dir)
                if not visited[ny][nx][dir]:
                    queue.append([[ny, nx], cnt + 1, dir])
                    visited[ny][nx][dir] = True
        if canmoveUp(center, dir):
          
            ny, nx = y-1, x
            if 0<=ny<n and 0<=nx<n:
                if ny == 12 and nx == 10:
                    print(y, x, ny, nx, dir)
                if not visited[ny][nx][dir]:
                    queue.append([[ny, nx], cnt + 1, dir])
                    visited[ny][nx][dir] = True
        if canmoveDown(center, dir):
           
            ny, nx = y+1, x
            if 0<=ny<n and 0<=nx<n:
                if ny == 12 and nx == 10:
                    print(y, x, ny, nx, dir)
                if not visited[ny][nx][dir]:
                    queue.append([[ny, nx], cnt + 1, dir])
                    visited[ny][nx][dir] = True
        if canRotate(center, dir):
         
            ny, nx = y, x
            if 0<=ny<n and 0<=nx<n:
                if ny == 12 and nx == 10:
                    print(y, x, ny, nx, dir)
            
                if dir == 1:
                    n_dir = 0
                else:
                    n_dir = 1
                if not visited[ny][nx][n_dir]:
                    queue.append([[ny, nx], cnt + 1, n_dir])
                    visited[ny][nx][n_dir] = True
                
    return 0


if __name__ == "__main__":
    getInput()
    print(solve())