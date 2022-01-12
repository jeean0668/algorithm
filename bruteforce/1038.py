import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
dp = [0] * 1000010
if 0<=n<=10:
    print(n)
    sys.exit()
queue = deque()
for i in range(11):
    queue.append(i)
    dp[i] = i
cnt = 10
while queue:
    now = queue.popleft()
    x = now % 10
    for i in range(x):
        dp[cnt] = now * 10 + i
        queue.append(now * 10 + i)
        cnt += 1
if cnt >= n and dp[n] != 0:
    print(dp[n])
else:
    print(-1)