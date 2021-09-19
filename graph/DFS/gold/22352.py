import sys

input = sys.stdin.readline
n, m = map(int, input().split())
before = []
after = []
visited = [[False] * m for _ in range(n)]
dy = [-1, 0, 0, 1]
dx = [0, 1, -1, 0]
for _ in range(n):
    row = list(map(int, input().split()))
    before.append(row)
for _ in range(n):
    row = list(map(int, input().split()))
    after.append(row)

def dfs(y, x, start_e, change_e):
    before[y][x] = change_e
    visited[y][x] = True
   
    for i in range(4):
        yy = y + dy[i]
        xx = x + dx[i]
        
        if 0 <= yy < n and 0 <= xx < m :
            #print(yy, xx)
            if not visited[yy][xx] and before[yy][xx] == start_e:
            
                dfs(yy, xx, start_e, change_e)
def check_ans():
    for j in range(n):
        for k in range(m):
            if before[j][k] != after[j][k]:
                return "NO"             
    return "YES"
            
for y in range(n):
    for x in range(m):
        if before[y][x] != after[y][x]:
            dfs(y, x, before[y][x], after[y][x])
        print(check_ans())
        exit()
  
            
            