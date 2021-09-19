import sys
import time

dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 4



if __name__ == "__main__":
    N = int(input())
    start = time.time()
    for i in range(5, N+1):
        dp[i] = (dp[i-3]*3)%10007
    print(dp[N])