import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

graph = [list(input().rstrip()) for _ in range(5)]
nums = [i for i in range(25)]
selected = [False] * 25
starts = []
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]
ans = 0

def moreThanFour():
    cnt = 0
    for i in range(25):
        if selected[i]:
            y, x = i // 5, i % 5
            if graph[y][x] == 'S':
                cnt += 1
    if cnt >= 4: return True
    return False

def isAdjacent():
    
    queue = deque()
    isSelected = [[False] * 6 for _ in range(6)]
    isQueue = [[False] * 6 for _ in range(6)]
    
    tmp = 0
    for i in range(25):
        if selected[i]:
            y, x = i // 5, i % 5
            isSelected[y][x] = True
            if tmp == 0:
                queue.append((y, x))
                isQueue[y][x] = True
                tmp += 1
    
    cnt = 1
    while queue:
        y, x = queue.popleft()
        if cnt == 7:
            return True
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0<=ny<5 and 0<=nx<5:
                if isSelected[ny][nx] and not isQueue[ny][nx]:
                    isQueue[ny][nx] = True
                    queue.append((ny, nx))
                    cnt += 1
    return False

def dfs(idx, cnt):
    global ans
    if cnt == 7:
        if moreThanFour():
            if isAdjacent() : ans += 1
        return
    for i in range(idx, 25):
        if selected[i] : continue
        selected[i] = True
        dfs(i, cnt + 1)
        selected[i] = False

def solve():
    global ans
    dfs(0, 0)
    print(ans)
    

if __name__ == "__main__":
    solve()