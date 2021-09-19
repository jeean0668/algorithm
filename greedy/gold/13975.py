import sys
import heapq

cases = int(input())

for i in range(cases):
    N = int(input())
    
    array = list(map(int, sys.stdin.readline().split()))
    heap = []
    
    for ar in array:
        heapq.heappush(heap, ar)
    
    result1, result2 = 0, 0
    result = 0
    while len(heap) != 1:
        result1 = heapq.heappop(heap)
        result2 = heapq.heappop(heap)
        
        result += result1 + result2
        heapq.heappush(heap, result1+result2)
    
    print(result)
    
    