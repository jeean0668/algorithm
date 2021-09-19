import sys
import heapq

N = int(input())
array = []
for i in range(N):
    p, d = map(int, sys.stdin.readline().split())
    array.append([p, d])

array.sort(key = lambda x : (x[1]))

heap = []
for i in range(N):
    now = array[i]
    heapq.heappush(heap, now[0])
    if len(heap) > now[1]:
        heapq.heappop(heap)
print(sum(heap))