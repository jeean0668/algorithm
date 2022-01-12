import sys
import math
from itertools import combinations
test_cases = int(input())

ans = sys.maxsize
def dfs(idx, plus_cnt, minus_cnt, n, value):
    global ans, poses
    if idx == n:
        if plus_cnt == n//2 and minus_cnt == n//2:
            ans = min(ans, round(math.sqrt(value[0] ** 2 + value[1] ** 2) , 8))
        
        return
    ny = poses[idx][0]
    nx = poses[idx][1]
    dfs(idx + 1, plus_cnt, minus_cnt + 1, n, (value[0] - ny, value[1] - nx))
    dfs(idx + 1, plus_cnt + 1, minus_cnt, n, (value[0] + ny, value[1] + nx))

while test_cases > 0:
    n = int(input())
    poses = []
    for _ in range(n):
        poses.append(list(map(int, input().split())))
    sy, sx = poses[0][0], poses[0][1]
    ans = sys.maxsize
    dfs(0, 0, 0, n, (0, 0))
    print(ans)
    test_cases -= 1
    