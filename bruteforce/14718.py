import sys
from itertools import combinations
input = sys.stdin.readline

# 1. n명중 k개의 조합을 구한다.
# 2. [k1[0], k2[0]...kk[0]] 의 최댓값, [k2[1], k2[1]...kk[1]] 의 최댓값 ...
# 을 모두 더한다.
# 3. ans값과 비교하여 갱신한다.

n, k = map(int, input().split())
soldiers = []
x, y, z = [], [], []
for _ in range(n): 
    a,b,c = list(map(int, input().split()))
    soldiers.append([a, b, c])
    x.append(a)
    y.append(b)
    z.append(c)

ans = sys.maxsize
for xx in x:
    for yy in y:
        for zz in z:
            cnt = 0 
            for one, two, three in soldiers:
                if one <= xx and two <= yy and three <= zz:
                    cnt += 1
            if cnt >= k:
                ans = min(ans, xx + yy + zz)
print(ans)
