import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
paper = []

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]
ans = 0
selected = [[False for _ in range(6)] for _ in range(6)]

for _ in range(n):
    row = list(input().rstrip())
    row_int = map(int, row)
    paper.append(list(row_int))

def result():
    total = 0
    for row in range(n):
        sum = 0 
        for col in range(m):
            if selected[row][col]:
                sum = (sum * 10) + paper[row][col]
            else:
                total += sum
                sum = 0
        total += sum        
        
    for col in range(m):
        sum = 0
        for row in range(n):
            if not selected[row][col]:
                sum = (sum * 10) + paper[row][col]
            else:
                total += sum
                sum = 0
        total += sum
    return total
    

def dfs(y, x):
    global ans, selected
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