import sys
input = sys.stdin.readline
from collections import deque
dp = [0] * 1000010
n = int(input())

queue = deque()
for i in range(1, 10):
    queue.append(i)
    dp[i] = i
if 0<=n<=10:
    print(n)
    sys.exit()
    
cnt = 10
while cnt <= n and queue:
    now = queue.popleft()
    x = now % 10
    for i in range(x):
        queue.append(now * 10 + i)
        dp[cnt] = now * 10 + i
        cnt += 1
if cnt >= n and dp[n] != 0: print(dp[n])
else : print(-1)