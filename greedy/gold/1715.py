import sys
import heapq

N = int(input())

heap = []
for i in range(N):
    a = int(input())
    heapq.heappush(heap, a)

result = 0
while len(heap) != 1:
    top = heapq.heappop(heap)
    second = heapq.heappop(heap)
    a = top+second
    print(top, second, a)
    heapq.heappush(heap,a)
    result += a
print(result)