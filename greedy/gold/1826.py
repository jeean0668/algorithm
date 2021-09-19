import sys
import heapq

input = sys.stdin.readline

N = int(input())
P = []
for i in range(N):
    P.append(list(map(int, input().split())))
last, init = map(int, input().split())
P.append([last, 0])
P.sort(key = lambda x : x[0])

D = [P[0][0]]
for i in range(1, N+1):
    D.append(P[i][0] - P[i-1][0])
    
fuel = init
count = 0
heap = []

for i in range(N+1):
    fuel -= D[i]
    #print('fuel :',fuel)
    if fuel >= 0:
        heapq.heappush(heap, -P[i][1])
    else:
        while fuel < 0:
            if len(heap) == 0:
                print(-1)
                sys.exit()
            top = -heapq.heappop(heap)
            #print("top :",top)
            fuel += top
            count +=1
        heapq.heappush(heap, -P[i][1])
        
print(count) 
    
