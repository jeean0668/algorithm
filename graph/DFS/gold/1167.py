"""
트리의 지름(트리에서 임의의 두점 사이 거리 중 가장 긴것)을 구하는 프로그램
1. 임의의 점에서 dfs로 길이를 구하고, 마지막 노드에서 다시 dfs로 길이를 구하여
두 값중 큰 값을 쓴다. 
 -> 4 퍼센트에서 오류 -> 임의의 점에서 가장 거리가 먼 leaf 노드를 찾아야 하는데 
"""

# 전역변수 선언
import sys
input = sys.stdin.readline
max_node = 0

# 입력
V = int(input())
graph = [[] for _ in range(V+1)] 

for _ in range(V):
    *temp, end = map(int, input().split())
    start = temp[0]
    i = 1
    while i < len(temp):
        end = temp[i]
        edge = temp[i+1]
        graph[start].append([end, edge])
        i += 2

def dfs(node):
    global max_node
    visited[node] = True
    ret = [0, node]
    for child in graph[node]:
        child_node = child[0]
        if visited[child_node]:
            continue
        temp = dfs(child_node)[0] + child[1]
        print(temp, ret[0], child_node)
        if ret[0] < temp:
            ret = [temp, child_node]
            
    return ret


result = 0 
visited = [False] * (V+1)
# 임의의 점에서 dfs 수행
result = dfs(3)
print(result)
visited = [False] * (V+1)
# max_node에서 dfs 수행

result = max(result, dfs(max_node))

print(result)
