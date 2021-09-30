"""
접근하는 방식은 맞았는데, bfs로 거리를 구하는 과정, bfs를 거쳐 최단거리에 있는 점을 뽑아내는 과정
이 미흡했다. 
# 택시와 가장 거리가 가까운 손님을 찾는다 -> prioirity queue를 활용한 bfs로 찾아낸다.
 => 모든 손님에 대한 거리를 찾을 필요가 없어 시간이 단축된다. 
 
"""


import sys
from collections import deque
import heapq

def findPassenger():
    global  fuel, tr, tc, mat, dx, dy
    priorque = []
    que = deque([(tr, tc, 0)])
    visited = [ [False] * N for _ in range(N)]
    visited[tr][tc] = True
    passengerId = -1
    minD = float('inf')

    while que:
        cr, cc, cd = que.popleft()

        if mat[cr][cc] >= 2 and minD >= cd:
            heapq.heappush(priorque, (cr, cc))
            minD = cd
            
        elif minD < cd:
            continue

        for idx in range(4):
            nr, nc = cr+dy[idx], cc+dx[idx]
            if 0 <= nr < N and 0 <= nc < N and mat[nr][nc] != 1 and not visited[nr][nc]:
                visited[nr][nc] = True
                que.append((nr, nc, cd+1))
    # 이 과정을 잘 못했다. 
    if len(priorque) > 0:
        pr, pc = heapq.heappop(priorque)
        tr, tc = pr, pc
        passengerId = mat[pr][pc]-2
        mat[pr][pc] = 0

    fuel -= minD
    return passengerId

def goToDestination(dr, dc):
    global  fuel, tr, tc, mat, dx, dy
    que = deque([(tr, tc, 0)])
    visited = [ [False] * N for _ in range(N)]
    visited[tr][tc] = True
    minD = float('inf')

    while que:
        cr, cc, cd = que.popleft()

        if cr == dr and cc == dc:
            minD = cd
            tr, tc = dr, dc
            break
        
        for idx in range(4):
            nr, nc = cr+dy[idx], cc+dx[idx]
            if 0 <= nr < N and 0 <= nc < N and mat[nr][nc] != 1 and not visited[nr][nc]:
                visited[nr][nc] = True
                que.append((nr, nc, cd+1))

    fuel -= minD
    return minD
    

if __name__ == "__main__":
    N, M, fuel =  map(int, sys.stdin.readline().strip().split())
    mat = [ list(map(int, sys.stdin.readline().strip().split())) for _ in range(N) ]
    tr, tc = map(int, sys.stdin.readline().strip().split())
    tr, tc = tr -1 ,tc - 1
    destinations = []

    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    for idx in range(M):
        pr, pc, dr, dc = map(int, sys.stdin.readline().strip().split())
        mat[pr-1][pc-1] = idx+2
        destinations.append((dr-1, dc-1))

    while M > 0:
        pid = findPassenger()
        print(pid)
        M -= 1

        if fuel <= 0:
            fuel = -1
            break

        dr, dc = destinations[pid]
        d = goToDestination(dr, dc)

        if fuel < 0:
            fuel = -1
            break

        fuel += d*2

    print(fuel)
