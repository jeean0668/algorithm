import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

left, right = 1, k
ans = -1
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    # 개수를 세는 방법을 알아내는것이 핵심이다. 
    # ex) 10보다 작은 것의 갯수 = (1*1, 1*2 .. 1* 5) => min(5, 10//1)
    #                            (3*1, 3*2, 3*3) => min(5, 10//3) = 3개
    
    for i in range(1, n+1):
        cnt += min(n, mid//i)

    if cnt >= k:
        ans = mid
        right = mid - 1
    elif cnt < k:
        left = mid + 1
print(ans)
