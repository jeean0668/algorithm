import sys
input = sys.stdin.readline
from collections import deque

n, T = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(n)]
points.insert(0, [0, 0])
points.sort()

def BS(sy, sx, s_idx):

    left, right = s_idx, n
    ret = []
    while left <= right:
        mid = (left + right)//2
        np = points[mid]
        if abs(np[0] - sx) <= 2 and abs(np[1] - sy) <= 2:
            if not(np[0] == sx and np[1] == sy): 
                ret.append(np)
            left = mid + 1
        elif abs(np[0] - sx) <=2 and abs(np[1] - sy) > 2:
            right = mid - 1
        elif abs(np[0] - sx) > 2:
            right = mid - 1
    return ret

def BFS():
    queue = deque()
    queue.append([0, 0, 0])
    visited = [[0, 0]]

    while queue:
        x, y, cnt = queue.popleft()
        if y == T:
            return cnt
        possible = BS(y, x, points.index([x, y]))
        
        #print(x, y, possible)
        for p in possible:
            if p not in visited:
                ny, nx = p[0], p[1]
                visited.append(p)
                queue.append([ny, nx, cnt + 1])
    return -1

print(BFS())