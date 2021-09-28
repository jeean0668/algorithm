
"""1. 가능한 모든 m개의 조합을 찾는다.
2. 그 조합에 대해서 bfs로 최댓값을 저장한다.
3. 최댓값들 중 최솟값을 출력한다.  """
ections import deque
import sys
import math
from copy import deepcopy
from itertools import combinations
input = sys.stdin.readline

n, c = map(int, input().split())
maps = []
starts = []
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for y in range(n):
    a = list(map(int, input().split()))
    for x in range(n):
        if a[x] == 2:
            starts.append((y, x, 0))
    maps.append(a)
def check(maps):
    for y in range(len(maps)):
        for x in range(len(maps)):
            if maps[y][x] == 0:
                return -1
    return 0

def bfs(start, maps):
    visited = [[0 for _ in range(len(maps))] for _ in range(len(maps))]
    maps = deepcopy(maps)
    queue = deque()

    queue.extend(start)
    last_change = 0
    while queue:
        cy, cx, cnt = queue.popleft()
        visited[cy][cx] = 1
        for i in dirs:
            ny, nx = cy + i[0], cy + i[1]
            if not(0<=ny<len(maps) and 0<=nx<len(maps)):
                continue
            if visited[ny][nx]:
                continue
            if maps[ny][nx] == 1:
                continue
            visited[ny][nx] = 1
            if maps[ny][nx] == 0:
                maps[ny][nx] = 2
                last_change = cnt + 1
            queue.append((ny, nx, cnt + 1))
    val = check(maps)
    print(maps)
    if val == 0:
        return last_change
    else:
        return -1

candidates = list(combinations(starts,c))
mins = math.inf
for value in candidates:
    print(value)
    result = bfs(value, maps)
    if mins > result and result != -1:
        mins = result
if mins == math.inf:
    print(-1)
else:
    print(mins)