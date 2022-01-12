import sys

n, i, m = map(int, input().split())
pos = []
for _ in range(m):
    y, x = map(int, input().split())
    pos.append((y-1, x-1))
    
def check(y, x, h, w):
    sy, sx = y, x
    ey, ex = y+h, x+w
    ret = 0
    for i in range(m):
        if sy <= pos[i][0] <= ey and sx <= pos[i][1] <= ex:
            ret += 1
    return ret
#1. 그물을 놓을 위치 후보들을 찾는다(물고기들의 교차점, 물고기 위치가 후보군)
for i in range(m-1):
    for j in range(i, m):
        if 

#2. y+h, x+w 내에 물고기들의 갯수를 센다.

h, w = 1, i//2 - 1
ans = 0
while w > 0:
    for i in range(len(pos)):
        y, x = pos[i][0], pos[i][1]
        cnt = check(y, x, h, w)
        ans = max(ans, cnt)
    w -= 1
    h += 1

print(ans)
