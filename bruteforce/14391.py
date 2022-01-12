import sys

n, m = map(int, input().split())
paper = [list(input()) for _ in range(n)]
ans = 0
selected = [[False for _ in range(m+1)] for _ in range(n+1)]

def result():
    
    ret = 0
    for i in range(n):
        tmp = 0
        for j in range(m):
            if selected[i][j]:
                tmp = tmp * 10 + int(paper[i][j])
            else:
                ret += tmp
                tmp = 0 
        ret += tmp        

    
    for j in range(m):
        tmp = 0
        for i in range(n):
            if not selected[i][j]:
                tmp = tmp * 10 + int(paper[i][j])
            else:
                ret += tmp
                tmp = 0
        ret += tmp
    return ret
    
def dfs(y, x):
    global ans
    if y == n:
        ans = max(ans, result())
        return
    if x == m:
        dfs(y+1, 0)
        return
    selected[y][x] = True
    dfs(y, x+1)
    selected[y][x] = False
    dfs(y, x+1)
    
dfs(0, 0)
print(ans)