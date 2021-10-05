""" 
최소 이동횟수를 구하는 문제인데, 최대 x, y 방향으로 최대 두칸까지 떨어진 타일까지
이동할 수 있다.

이분 탐색이 어색해서 버벅거렸다. 시작점(mid)를 기준으로 하여 왼쪽, 오른쪽 범위를 각각
탐색 해주는 것이 이분 탐색이다. 즉, for i in range(0, mid) 범위에서 값을 찾고, for i in range(mid, n) 범위에서
값을 따로 또 찾아주어 queue에 넣어주면 된다. 
"""

import sys
input = sys.stdin.readline
from collections import deque

dy = [-2, -1, 0, 1, 2]
dx = [-2, -1, 0, 1, 2]
# distance[][t] = min(distance[][t-2], distnace[][t-1])

start = (0, 0)

def getInput():
    global graph, n, T

    graph = []
    n, T = map(int, input().split())
    for _ in range(n):
        x, y = map(int, input().split())
        graph.append((x, y))
    # y좌표 기준으로 오름차순 정렬한다. 
    graph.sort( key = lambda x : (x[0], x[1]))

def solve():
    global graph, n, T
    start = (0, 0 ,0, 0)
    queue = deque()
    queue.append(start)
    visited = [False] * 50001
    
    while queue:
        x, y, cnt, idx = queue.popleft()
        if y == T:
            return cnt
        for i in range(idx, n):
            nx, ny = graph[i][0], graph[i][1]
            if not visited[i]:
                if abs(x - nx) <= 2 and abs(y - ny) <= 2:
                    visited[i] = True
                    queue.append((nx, ny, cnt + 1, i))
                elif abs(x - nx) > 2 and abs(y - ny) > 2:
                    break
        for i in range(0, idx):
            nx, ny = graph[i][0], graph[i][1]
            if not visited[i]:
                if abs(x - nx) <= 2 and abs(y - ny) <= 2:
                    visited[i] = True
                    queue.append((nx, ny, cnt+1, i))
                elif abs(x - nx) > 2 and abs(y - ny) > 2:
                    break
    return -1
         



if __name__ == "__main__":
    getInput()
    result = solve()
    print(result)
