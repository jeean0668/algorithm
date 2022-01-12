import sys
input = sys.stdin.readline

n, m = map(int, input().split())
K = list(map(int, input().split()))
mem = [False for _ in range(1001)]

result = 0

for k in K:
    iter = k
    while k <= n:
        if mem[k]:
            k+=iter
            continue
        mem[k] = True
        result += k
        k += iter
        
print(result)
    