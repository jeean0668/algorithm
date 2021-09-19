import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
array = []
for _ in range(n):
    
    start, end = map(int, input().split())
    array.append([start, start+end])

array.sort(key=lambda x: x[0])

heap = []
heapq.heappush(heap, array[0][1])

print(array)

