

import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

N, M, K, X = map(int ,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append([B,1])
heap = []
dist = [INF for _ in range(N+1)]

def bfs(start):
    global dist
    heapq.heappush(heap, [0, start])
    dist[start] = 0
    while heap:
        cur_d, dest = heapq.heappop(heap)
        if dist[dest] < cur_d:
            continue
      
        for n_dest, n_d in graph[dest]:
            
            if dist[n_dest] > cur_d + n_d:
        
                dist[n_dest] = cur_d + n_d
                
                heapq.heappush(heap, [cur_d + n_d, n_dest])
    result = []
    for i in range(1, N+1):
        #rint(dist[i], i)
        if dist[i] == K:
            result.append(i)
            
    return result

result = bfs(X)

if result:
    for city in result:
        print(city)
else:
    print(-1)