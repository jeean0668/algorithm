"""
첨 생각했던대로 했더니 무한루프 
"""

import sys
from collections import deque
import math
import heapq
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, k = map(int, input().split())

queue = []
heapq.heappush(queue, [0, n])
distance = [math.inf] * (100001)
prev = [0] * 100001
distance[n] = 0

def connected(node):
    # 연결된 세개의 노드를 반환한다.
    result = []
    if node > 0:
        result.append(node - 1)
    if node < 100000:
        result.append(node + 1)
    if 0 < node * 2 < 100001:
        result.append(node * 2)
    return result
def path(x):
    arr = []
    temp = x
    for _ in range(distance[x] + 1):
        arr.append(temp)
        temp = prev[temp]
    print(' '.join(map(str, arr[::-1])))
while queue:
    temp = heapq.heappop(queue)
    now, dist = temp[1], temp[0]
    if now == k:
        print(distance[k])
        path(now)
        break
    if distance[now] < dist:
        continue
    childs = connected(now)
    for child in childs:
        if distance[child] > dist + 1:
            distance[child] = dist + 1
            prev[child] = now
            heapq.heappush(queue, [dist + 1, child])



            
