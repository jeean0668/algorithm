import sys
import math
input = sys.stdin.readline

def triangle(x):
    # x = n(n+1)/2 를 만족하는 n이 존재하면 True 반환
    max_n = int(math.sqrt(x * 2))
    left, right = 0, max_n
    while left <= right:
        mid = (left + right)//2
        if (mid * (mid + 1))//2 > x:
            right = mid -1
        elif (mid * (mid + 1))//2 < x:
            left = mid + 1
        else:
            return True
    return False
def tray(x):
    # x = n^2 만족하면 True 반환
    max_n = int(math.sqrt(x))
    left, right = 0, max_n
    while left <= right:
        mid = (left + right)//2
        if mid << 1 > x:
            right = mid -1
        elif mid << 1 < x:
            left = mid + 1
        else:
            return True
    return False

def search(left, right):
    cnt = 0
    for i in range(left + 1, right):
        if triangle(i-1) and tray(i):
            cnt += 1
    return cnt

i = 1
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print("Case {0}: {1}".format(i, search(a, b)))
    i += 1