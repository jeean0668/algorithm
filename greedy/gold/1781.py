import sys
import heapq

input = sys.stdin.readline

n = int(input())
array, heap = [], []
for _ in range(n):
    day, cup = map(int, input().split())
    array.append([day, cup])
    
array.sort(key = lambda x : -x[0])
result = 0
index = 0
for day in range(n, 0, -1):
    
    while array[index][0] == day and index < n:
        heapq.heappush(heap, -array[index][1])
        if index < n-1:
            index += 1
        else:
            break
    if len(heap) != 0:
        temp = heapq.heappop(heap)
        result += temp
    else:
        continue
print(-result)