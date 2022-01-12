import sys
from collections import defaultdict
input = sys.stdin.readline

dict = defaultdict(int)

n, k, d = map(int, input().split())
rules = [list(map(int, input().split())) for _ in range(k)]

def func(p):
    total = 0
    for start, end, step in rules:
        betas = min(end, p)
        if start <= betas:
            cal = (betas - start) // step + 1
            total += cal
    return total


left, right = 0, 1000000
ans = 0
while left <= right:
    mid = (left + right) // 2
    cal = func(mid)
    
    if cal >= d:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)