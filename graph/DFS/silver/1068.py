import sys

input = sys.stdin.readline
n = int(input())
nodes = list(map(int, input().split()))
start = int(input())
length = len(nodes)
graph = [[] for _ in range(n)]
parent = [-1] * (n+1)
             
def change(start_node):
    stack = [start_node]
    while stack:
        node = stack.pop()
        for v in graph[node]:
            if v != parent[node]:
                stack.append(v)
        graph[node] = -2

for i in range(length):
    now = nodes[i]
    if now == -1:
        #graph[i].append(-1)
        parent[i] = -2
    else:
        graph[i].append(now)
        graph[now].append(i)
        parent[i] = now
    
    
change(start)
count = 0
print(graph)
for e in graph:

    if e != -2:
        if len(e) == 1:
            count +=1 
print(count)


