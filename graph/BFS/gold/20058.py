# -*- coding: utf-8 -*- 
"""
회전이 어려웠던 문제
총 세단계로 구성되어있다.
1. 회전, 2. 맵 갱신, 3. 연결요소 길이
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)
n, q = 0, 0

visited = [[False for _ in range(65)] for _ in range(65)]
temp = [[0 for _ in range(65)] for _ in range(65)]
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]
graph = []
def dfs(y, x):
    visited[y][x] = True
    ret = 1
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0<=ny<2**n and 0<=nx<2**n:
            if visited[ny][nx]:
                continue
            if graph[ny][nx] > 0:
                ret += dfs(ny, nx)
    return ret

def getBiggest():
    ret = 0
    for i in range(2**n):
        for j in range(2**n):
            if graph[i][j] > 0 and not visited[i][j]:
                ret = max(ret, dfs(i, j))
    return ret

def getSum():
    ret = 0
    for i in range(2**n):
        for j in range(2**n):
            ret += graph[i][j]
    return ret

# L 크기의 타일을 시계방향으로 회전하는 공식, 외워두는게 좋을것 같다.
def rotate(y, x, L):
    for i in range(L):
        for j in range(L):
            
            temp[i][j] = graph[y+L-1-j][x+i]
            # y, x = 0, 0 이고 L=2일때 
            # ex) [0, 0] = graph[0+2-1-0][0+0]
            # ex) [0. 1] = graph[0+2-1-1][0+0]
            # ex) [1, 0] = graph[0+2-1-0][0+1]
            # ex) [1, 1] = graph[0_2-1-1][0+1]
    for i in range(L):
        for j in range(L):
            graph[y+i][x+j] = temp[i][j]

def solve(L):
    L = 2 ** L

    # 모든 격자에 대해서 회전
    for i in range(0, 2**n, L):
        for j in range(0, 2**n, L):
            
            rotate(i, j, L)
    # 얼음 녹이기
    checkmelted = [[False for _ in range(65)] for _ in range(65)]
    for i in range(2**n):
        for j in range(2**n):
            if graph[i][j] == 0:
                continue
            cnt = 0
            for k in range(4):
                ny = i + dy[k]
                nx = j + dx[k]
                
                if not(0<=ny<2**n and 0<=nx<2**n):
                    continue
                if graph[ny][nx] > 0:
                    cnt += 1
            
            if cnt < 3:
                checkmelted[i][j] = True
    for i in range(2**n):
        for j in range(2**n):
            
            if checkmelted[i][j]:
                graph[i][j] -= 1
   
if __name__ == "__main__":
    n, q = map(int, input().split())
    for _ in range(2**n):
        graph.append(list(map(int, input().split())))
    quest = list(map(int, input().split()))
    for con in quest:
        solve(con)
    print(getSum())
    print(getBiggest())