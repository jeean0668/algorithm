import sys
input = sys.stdin.readline

m = int(input())

# m = 1 -> N!에 N <= 5 * 1
# m = 3 -> N!에 N <= 5 * 3
# start = 1, end =  5 * m으로 잡고 이분탐색 진행
# 만약 mid의 min(2 갯수, 5 갯수) = m이면 mid 출력

def cal(x):
    cnt5 = 0
    while x >= 5:
        cnt5 += x // 5
        x /= 5
    return cnt5


def solve(left, right):
    ans = 0
    find = False
    while left <= right:
        mid = (left + right) // 2
        cnt = cal(mid)
        if cnt < m: left = mid + 1
        elif cnt > m: right = mid - 1
        else: 
            find = True
            ans = mid
            right = mid - 1
    if find:
        print(ans)
    else:
        print(-1)

left = 1
right = m * 5
ans = 0
solve(left, right)
