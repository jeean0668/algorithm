import sys
from collections import deque
input=sys.stdin.readline

"""
bfs 탐색이 방문순서에 맞게 이뤄지도록 하는 것이 핵심이다.
그래서 order라고 하는 list에 탐색순서를 저장하고, sort로
graph를 방문순서에 맞게 정렬해주었다. 
"""
 
def getInput():
    global n, graph, order, result
    n = int(input())
    graph = [[] for _ in range(n+1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    result = list(map(int, input().split()))
    order = [0] * (n+1)
    
    for i in range(len(result)):
        # result[i]의 방문 순서는 i번째 임을 기록
        order[result[i]] = i
    
    #방문 순서대로 정렬
    for i in range(len(graph)):
        graph[i].sort(key = lambda x : order[x])

def solve():
    global n, graph, order
    visited = [False for _ in range(n+1)]
    queue = deque()
    queue.append(1)
    visited[1] = True
    result = [1]
    while queue:
        now = queue.popleft()
        for child in graph[now]:
            if visited[child]:
                continue
            queue.append(child)
            visited[child] = True
            result.append(child)
    return result


if __name__ == "__main__":
    getInput()
    ret = solve()
    if ret == result:
        print(1)
    else:
        print(0)