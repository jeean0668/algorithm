import sys

n, m, k = map(int, input().split())
graph = [[0] * m] * n

# 비트마스킹 문제인듯.

def draw(sy, sx, tile):
    for i in range(sy, sy + len(tile)):
        for j in range(sx, sx + len(tile[0])):
            if graph[i][j] == 0:
                graph[i][j] = tile[i-sy][j-sx]
    
def rotate(tile):
    r, c = len(tile), len(tile[0])
    ret = [[0] * r] * c
    for i in range(c):
        for j in range(r):
            
            ret[i][j] = tile[r - j - 1][i]
    return ret
    
def colored(tile, cnt):
    
    if cnt == 4:
        return False
    r, c = len(tile), len(tile[0])
    possible = False
    for i in range(n):
        for j in range(m):
            possible = True
            if i + r <= n and j + c <= m:
                for x in range(r):
                    for y in range(c):
                        if graph[i + x][j + y] == 1 and tile[x][y] == 1:
                            possible = False
                            break
                    if not possible:
                        break
            else: 
                possible = False
            if possible:
                draw(i, j, tile)
                return True
    if not possible:
        rotate_tile = rotate(tile)
        if colored(rotate_tile, cnt + 1) : return True
        return False
    
        
for _ in range(k):
    r, c = map(int, input().split())
    tile = [list(map(int, input().split())) for _ in range(r)]
    colored(tile, 0)

cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt += 1
print(cnt)
 