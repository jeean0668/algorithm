import sys

input = sys.stdin.readline

n,m,h = map(int, input().split())
graph = [[False for _ in range(n+2)] for _ in range(h+2)]
if m == 0 : 
    print(0)
    sys.exit()
cols = []
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = True

def check():
    for start in range(n):
        k = start
        for j in range(h):
            if graph[j][k]:
                k += 1
            elif k > 0 and graph[j][k-1]:
                k -= 1
        if k != start : return False
    return True
    
def dfs(cnt, y, x):
    global ans
    if check():
        ans = min(ans, cnt)
        return
    elif cnt == 3 or ans <= cnt: return
    for i in range(y, h):
        if i == x: k = y
        else: k = 0
        for j in range(k, n-1):
            if not graph[i][j] and not graph[i][j+1] and not graph[i][j-1]:
                if j > 0 and graph[i][j-1]: continue
                graph[i][j] = True
                dfs(cnt + 1, i, j + 2)
                graph[i][j] = False
          
ans = 4
dfs(0, 0, 0)      
print(ans if ans < 4 else -1)
            
    
    
    
            