"""
트리의 리프노드를 끊어내기 위한 최소 cost를 찾는 문제
"""

# 전역변수 선언
import sys
input = sys.stdin.readline
INF = 100000
sys.setrecursionlimit(111111)

# main
def makeGraph(n, m):
   
    for _ in range(m):
        node, next_node, edge = map(int, input().split())
        graph[node].append([next_node, edge])
        graph[next_node].append([node, edge])
        

        
def dfs(node, val):
    
    global graph
    visited[node] = True
    ret = 0
    isLeaf = False
    for child in graph[node]:
        child_node = child[0]
        edge = child[1]
        if not visited[child_node]:
            isLeaf = True
            ret += dfs(child_node, edge)
        
    if not isLeaf:
        return val
    else:
        return min(ret, val)
        
        
if __name__ == "__main__":
    test_cases = int(input())
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    makeGraph(n, m)
    visited = [False for _ in range(n+1)]
    print(dfs(1, INF))
    