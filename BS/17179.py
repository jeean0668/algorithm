import sys
input = sys.stdin.readline

n, m, l = map(int, input().split())
cakes = [int(input()) for _ in range(m)] + [l]

def search(left, right, cut):
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        start, cnt = 0, 0
        for i in range(len(cakes)):
            d = cakes[i] - start
            if d >= mid:
                start = cakes[i]
                cnt += 1
        if cnt > cut:
            left = mid + 1
            ans = max(ans, mid)
        else:
            right = mid - 1
    print(ans)
for _ in range(n):
    cut = int(input())
    left, right = 1, l
    search(left, right, cut)
