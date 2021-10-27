import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)

n = int(input())
s = list(map(int,input().split()))
def gcd(x, y):
    # 유클리드 호제법 
    while y != 0:
        x, y = y, x%y
    return x

def GCD(st, e):
    # s[st:mid] 에서 최대공약수를 반환하는 함수
    global s, n
    maximum = s[st]
    for i in range(st+1, e):
        # i번째 수까지의 최대 공약수는, i-1번째 까지의 최대공약수와 i번째 수의 최대공약수
        maximum = gcd(maximum, s[i])
    return maximum

def solve(st, e):
    global s, n
    ret = 0
    if e - st == 1:
        return s[st]
    mid = (st+e)//2
    # 왼쪽을 선택했을 경우 
    left = GCD(st, mid) + solve(mid, e)
    right = GCD(mid, e) + solve(st, mid)
    return max(left, right)

result = 0
if n == 1:
    print(s[0])
    sys,exit()
result = GCD(0, n//2) + solve(n//2, n)
result = max(result, GCD(n//2, n) + solve(0, n//2))
print(result)