"""
1. 무작정 DFS로 접근하는 방법 -> n이 최대 500이라서 recursion error뜸
2. dynamic programming 으로 접근 : nxn 행렬에서 경로의 갯수를 구하는 방법은
거의 dynamic programming으로 푸는것 같다. 
"""

# 전역변수

import sys
input = sys.stdin.readline

#입력
n = int(input())
forest = []
c = [[0 for _ in range(n)] for _ in range(n)]
dy = [1,0,0,-1]
dx = [0,1,-1,0]

for _ in range(n):
    row = list(map(int, input().split()))
    forest.append(row)

# dfs함수, 특정 지점에서 갈 수 있는 최댓값을 c[y][x]에 저장한다. 
def dfs(y, x):
   
    # 이미 방문한적이 있는 곳이면, 그 좌표에 저장된 값을 반환하면 된다. 
    if c[y][x] != 0: 
        return c[y][x]
    
    c[y][x] = 1
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0<=ny<n and 0<=nx<n:
            if forest[y][x] < forest[ny][nx]:
                c[y][x] = max(c[y][x], dfs(ny, nx) + 1)
                # c[y][x] = max(c[y-1][x], c[y+1][x], ....) + 1
                # 위의 점화식을 dfs로 구현한다. 
    return c[y][x]
            
def solve():
    # c[][]에 저장된 값중 가장 큰 값을 print한다.
    answer = 0
    for i in range(n):
        for j in range(n):
            answer = max(answer, dfs(i,j))
    print(answer)
# 임의의 점에서 dfs 시작한다.abs()
if __name__ == "__main__":
    dfs(0, 0)
    solve()