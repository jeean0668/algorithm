import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lectures = list(map(int, input().split()))
max_t, min_t = sum(lectures), max(lectures)

def search(left, right):

    ans = 0
    while left <= right:
        mid = (left + right) // 2
        ps, cnt = 0, 0
        for i in range(n):
            if ps + lectures[i] > mid :
                ps = 0
                cnt += 1
            ps += lectures[i]
        if ps != 0:
            cnt += 1
        if cnt <= m:
            right = mid - 1
        else:
            left = mid + 1
    print(left)
search(min_t, max_t)