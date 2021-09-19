

"""
같은 색깔로 이루어진 cycle의 존재 여부를 찾는 문제
1. 첫번째 난관 : 오른쪽으로 갔다가 왼쪽으로 돌아오는 경우를 해결해야함 
 -> 이전 좌표를 매개변수로 받아, next pos가 prev pos와 다른지 검사한다. 
"""

# 전역변수 선언
import sys
input = sys.stdin.readline
graph = []
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

# dfs 함수               
def dfs(y, x, k, py, px):
    
    if visited[y][x]:
        return True
    visited[y][x] = True

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<n and 0<=nx<m:
            
            if ny == py and nx == px:
                continue # 예외사항 적발되면 continue하는 방식의 재귀 참고! 
            if graph[ny][nx] != k:
                continue
            if dfs(ny, nx, k, y, x):
                return True
    return False
                    
# main
n, m = map(int, input().split())
visited = [[False for _ in range(m)] for _ in range(n)]
for _ in range(n):
    # 그래프 입력
    row = list(input().strip())
    graph.append(row)

for y in range(n):
    for x in range(m):
        if not visited[y][x]:
            if dfs(y,x,graph[y][x], -1, -1):
                print("Yes")
                exit()
print("No")
