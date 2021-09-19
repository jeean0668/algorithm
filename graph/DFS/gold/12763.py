"""
1번부터 N번 노드까지 T 시간안에 최소 cost로 이동하는 비용
16퍼센트에서 틀렸다. 이미 불가능하다고 판정된 경로를 반대방향으로 다시 찾아가는게 문제다. 
문제는 경로 탐색에 실패했을 경우를 처리하지 않아서 생겼다. 예외처리 해주니 정답이 됨. 
"""

# 전역변수 선언
import sys
sys.setrecursionlimit(111111)
input = sys.stdin.readline
INF = 100000001

# 그래프 생성

def makeGraph(n, L):
    
    global graph
    global time_table
    global cost_table
    global visited
    global c
    time_table = [[[] for _ in range(n+1)] for _ in range(n+1)]
    cost_table = [[[] for _ in range(n+1)] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    for _ in range(L):
        start, end, time, cost = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)
        time_table[start][end] = time
        time_table[end][start] = time
        cost_table[start][end] = cost
        cost_table[end][start] = cost
    c = [INF for _ in range(n+1)]
        

# dfs로 탐색

def dfs(node, time, cost):
    
    global visited
    global T
    global M
    global n
    global c
    
    if node == n:
        return cost
    visited[node] = True
    
    for child in graph[node]:
        if visited[child]:
            continue
        next_time = time + time_table[node][child]
        
        next_cost = cost + cost_table[node][child]
        if next_time > T:
            continue
        if next_cost > M:
            continue
        
        c[node] = min(c[node], dfs(child, next_time, next_cost))
        #rint("search :",node, child, next_time, next_cost)
    
    visited[node] = False
    return c[node]
        


# main
if __name__ == "__main__":
    n = int(input())
    T, M = map(int, input().split())
    L = int(input())
    makeGraph(n, L)
    result = dfs(1, 0, 0)
    if result >= INF:
        print(-1)
    else:
        print(result)
    
    
    
    
    