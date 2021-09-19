import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [False] * n

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start, depth):
    
    if depth == 5:
        print(1)
        exit()
    for v in graph[start]:
        if not visited[v]:
            visited[v] = True
            dfs(v, depth+1)
            visited[v] = False


for i in range(n):
    visited[i] = True
    dfs(i, 1)
    visited[i] = False

print(0)
    