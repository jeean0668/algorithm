import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())
array, bags = [], []
for _ in range(n):
    m, v = map(int, input().split())
    array.append([m, v])
for _ in range(k):
    bags.append(int(input()))

array.sort()
bags.sort()

heap = []
stolen = 0

for bag in bags:
    
    while array and bag >= array[0][0]:
        m, v = heapq.heappop(array)
        heapq.heappush(heap, -v)
    if heap:
        stolen += heapq.heappop(heap)
    elif not array:
        break
        
print(-stolen)
