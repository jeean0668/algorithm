import sys
import heapq

tests = int(input())

for test in range(tests):
    N = int(input())
    array = list(map(int, sys.stdin.readline().split()))
    
    heap = []
    for ar in array:
        heapq.heappush(heap, ar)
    
    result = 1
    while len(heap) != 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        result *= first*second
        heapq.heappush(heap, first*second)
        
    print(result)