"""
가장 기본적인 플로이드 와샬 알고리즘 문제이다.
플로이드 와샬 알고리즘은 3중 for문을 사용하기 때문에, 굳이 bfs를 사용하는지 의문이다.

"""

import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
INF = sys.maxsize
dist = [[INF] * (n+1) for _ in range(n+1)]
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    dist[a][b] = 1
    dist[b][a] = 1
    

def floyd():
    global dist
    for k in range(1, n+1): # 거쳐가는점
        dist[k][k] = 0
        for i in range(1, n+1): # 시작점
            for j in range(1, n+1): # 끝점
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
floyd()
result = INF
temp = []
for i in range(1, n+1):
    temp.append(max(dist[i][1:]))

score = min(temp)
_count = temp.count(score)
candidate = []
for i in range(len(temp)):
    t = temp[i]
    if t == score:
        candidate.append(i+1)
print(score, _count)

candidate = " ".join(map(str, candidate))
print(candidate)
