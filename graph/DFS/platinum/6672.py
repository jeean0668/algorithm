"""
단절점 문제로, platinum 1의 문제이다.
특정 노드가 없을때, 그 노드의 자식노드들이 특정 노드를 거치지 않고 특정 노드보다 더 작은 방문번호를 가진 노드로 이동할 수 있는지 여부를 판단하는 문제이다.
"""

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
MAX = 5000
graph = [[] for _ in range(MAX+1)] 
isCut = []
cnt = 0

n, m = map(int, input().split())
while True:
    start, end = map(int, input().split())
    if start == 0 and end == 0:
        break
    graph[start].append(end)
    graph[end].append(start)
    
order = [None] * (MAX+1)

def dfs(here, parent):
    global cnt
    cnt += 1
    order[here] = cnt
    ret = order[here]
    
    for child in graph[here]:
        # 이미 방문된 점 -> 현재의 방문순서와 탐색된 방문순서 중 작은값을 잧는다.
        if child == here:
            continue
        if order[child]:
            ret = min(ret, order[child])
            continue
        prev = dfs(child, here) # child부터 시작하는 subtree에서 방문순서가 제일 작은 것
        if prev >= order[here]:
            # subtree 방문순서가 here보다 크다는 건, here를 지나야 child로 갈 수 있다는 의미.
            isCut.append(here)
        ret = min(ret, prev)
    return ret

for i in range(1, n+1):
    if not order[i]:
        dfs(i, None)
print(isCut)
        

