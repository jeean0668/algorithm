import sys
input = sys.stdin.readline

n, m = map(int, input().split())
times = [int(input()) for _ in range(n)]

left, right = 1, m * max(times)

def search(left, right):

    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for t in times:
            cnt += (mid // t)
        if cnt >= m:
            right = mid - 1
        else:
            left = mid + 1
    print(left)        
search(left, right)