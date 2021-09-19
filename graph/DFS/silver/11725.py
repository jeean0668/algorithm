import sys

input = sys.stdin.readline
n = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
parent = [[] for _ in range(n+1)]

for _ in range(1, n):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
def dfs(start_node):
    
    stack = [start_node]
    
    while stack:
        node = stack.pop()
        for v in graph[node]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)
                parent[v] = node

dfs(1)
for i in range(2, n+1):
    print(parent[i])