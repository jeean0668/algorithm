import sys


test = int(input())

for i in range(test):
    N = int(input())

    ans = list(map(int, sys.stdin.readline().split()))

    max_stock = ans[N-1]

    result = 0

    for i in range(N-1, -1, -1):
        if ans[i] > max_stock:
            max_stock = ans[i]
        else:
            result += (max_stock - ans[i])
    print(result)