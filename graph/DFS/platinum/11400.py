"""
단절선 문제이다.
시간복잡도 내에 문제를 해결하는것이 너무 어려워서, 해설을 볼수밖에 없었다.
단절선 알고리즘, 단절점 알고리즘을 확실히 파악하는것이 중요하다. 
"""

import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

def dfs(here, parent):
    #here과 here의 자식 노드가 here에서 parent노드로 가는 간선을 사용하지 않고 도달할 수 있는 정점 중 가장 먼저 dfs함수가 방문한 정점을 반환한다.

출처: https://bowbowbow.tistory.com/3 [멍멍멍]
	global cnt
	cnt += 1
	order[here] = cnt
	ret = order[here]

	for next in graph[here] :
		if next == parent :
			continue

		if order[next] :
			ret = min(ret, order[next])
			continue

		subtree = dfs(next, here)
		ret = min(subtree, ret)

		# 부모로 바로가는 간선(현재간선)을 제외하고 서브트리의 간선 중 부모보다 선조로 갈 수 없으면
		if subtree > order[here] :
			cutEdge.add(tuple(sorted([here,next])))

	return ret


# N개
V,E = map(int, sys.stdin.readline().rstrip().split(" "))
graph = defaultdict(set)
cutEdge = set()
candidates = set()

for _ in range(E) :
    a,b = map(int, sys.stdin.readline().rstrip().split(" "))
    graph[a].add(b)
    graph[b].add(a)
    candidates.add(a)
    candidates.add(b)

order = [None] * (V+1)
cnt = 0
idx =0
for vertex in candidates :
    if not order[vertex] :
        dfs(vertex,  None)


print(len(cutEdge))
cutEdge = sorted(cutEdge, key=lambda x : (x[0],x[1]))

for a,b in cutEdge :
    print(a,b)