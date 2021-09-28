"""
첨 생각했던대로 했더니 무한루프 
"""

import sys
from collections import deque
import math
input = sys.stdin.readline

n, k = map(int, input().split())

queue = deque()
queue.append([n, 0])
distance = [math.inf] * (100001)
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

while queue:
    now, dist = queue.popleft()
    if distance[now] < dist:
        continue
    if now == 0:
        continue
    childs = connected(now)
    for child in childs:
        print(child)
        if distance[child] > dist + 1:
            distance[child] = dist + 1
            queue.append([child, dist + 1])
print(distance[k])