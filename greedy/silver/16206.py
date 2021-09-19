

import sys
from queue import PriorityQueue

N, M = map(int, sys.stdin.readline().split())
cakes = list(map(int, sys.stdin.readline().split()))
que = PriorityQueue()
for cake in cakes:
    que.put(cake)

history = 0 
cake = 0
while not que.empty():
    cur = que.get()
    if cur % 10 != 0:
        cut = cur//10
    
        if history + cut <= M:
            history += cut
            cake += cur//10
            
        else:
            max_cut = M-history
            cake += max_cut 
            break
    elif cur % 10 == 0:
        cut = cur // 10 - 1
        if history + cut <= M:
            history += cut
            cake += cut + 1
        else:
            max_cut = M-history
            if max_cut == cur//10 - 1:
                cake += max_cut+1
            else:
                cake += max_cut
        
print(cake)