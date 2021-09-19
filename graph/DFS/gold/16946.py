"""
특정 위치의 1을 0으로 바꾸었을때, 인접한 0 타일의 갯수를 모두 세는 문제이다.
N과 M이 최대 1000까지 주어졌기 때문에, 모든 원소들을 다 탐색하는건 불가능하다.
2. 인접한 타일들을 group으로 묶는 문제인데, 미숙해서 어렵다.
그리고 DFS로는 풀수 없다. 무조건 시간초과 난다. BFS로 해결해야한다.


"""

# 전역변수 선언

import sys
from collections import deque

r, c = map(int, sys.stdin.readline().rsplit())
visited = [[False for _ in range(c)] for _ in range(r)]
arr = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(r)]
answer = [[0 for _ in range(c)] for _ in range(r)]
d = ((0,1), (0,-1), (1,0), (-1,0))

for i in range(r):
    for j in range(c):
        if arr[i][j] == 1: answer[i][j] = 1

def bfs(sy, sx):
    q = deque()
    q.append((sy, sx))
    cnt = 1
    ones = []

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + d[i][0]
            nx = x + d[i][1]

            if -1<ny<r and -1<nx<c:
                if visited[ny][nx]: 
                    continue
                visited[ny][nx] = True
                if arr[ny][nx] == 1:
                    ones.append((ny, nx))
                    continue
                
                visited[ny][nx] = True
                q.append((ny,nx))
                cnt += 1
    # bfs는 queue 루프가 끝나고 추가사항들을 정리해주는게 편리하다. 
    
    for y, x in ones:
        visited[y][x] = False
        answer[y][x] += cnt
        if answer[y][x] >= 10: answer[y][x] %= 10

for i in range(r):
    for j in range(c):
        if arr[i][j] == 0:
            if not visited[i][j]:
                visited[i][j] = True
                bfs(i,j)

for i in range(r):
    print(''.join(map(str,answer[i])))