import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
component = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(start_node):
    stack = [start_node]
    
    while stack:
        node = stack.pop()
        
        for v in graph[node]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)
for node in range(1, n+1):
    if not visited[node]:
        dfs(node)
        component += 1
print(component)
