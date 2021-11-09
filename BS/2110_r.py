""" 
라우터의 갯수를 어떻게 셀 것이냐가 관건인 문제 

"""

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
routers = [int(input()) for _ in range(n)]
routers.sort() #[1, 2, 4, 8, 9, 10] -> [0, 1, 3, 7, 8, 9]
max_d = max(routers) - min(routers)

def search(left, right):

    ans = 0
    while left <= right:
        mid = (left + right) // 2
        cnt = 1
        start = routers[0]
        # 특정 간격(mid) 보다 멀리 떨어진 라우터들을 설치한다. 
        for i in range(1, n):
            d = routers[i] - start
            if mid <= d:
                cnt += 1
                start = routers[i]
        # 총 설치된 라우터들의 갯수와 c를 비교한다. 
        if cnt >= c:
            # 설치된 공유기 수가 더 많을 경우 -> 간격 넓힌다.
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    print(ans)


search(1, max_d)