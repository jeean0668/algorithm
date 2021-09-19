"""
1. 시작점을 1번 노드라고 가정
2-1. 1번 노드 주변에 있는 2나 4 노드가 non-colored or red면 1번에 red 색칠가능
2-2. 2번 노드 주변에 있는 2나 4 노드가 non-colored or blue 면 '' 
3. 모든 노드를 colored 하면, blue 집합과 red 집합 인구의 차를 구함
4. 최솟값으로 갱신 
"""

import sys

n = int(input())
graph = [[] for _ in range(n+1)]
populations = list(map(int, input().split()))
for i in range(1, n+1):
    k, *near = map(int, input().split())
    graph[i] = near

print(graph)
