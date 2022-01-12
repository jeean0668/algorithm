import sys
import math
input = sys.stdin.readline
"""
LCM 구하는 문제
1. gcd를 구한다.(유클리드 호제법)
2. 두 수를 곱한 값을 gcd로 나눈다.
"""

a, b = map(int, input().split())

arr = []
# abs(b-a)의 약수를 구한다.
result = abs(b-a)
if result == 0:
    print(1)
    sys.exit()
for i in range(1, int(math.sqrt(result))+1):
    if result % i == 0:
        arr.append(i)
        if i != (result // i) : arr.append(result // i)
arr.sort()
n = 1
# (A+N) % 약수 == (B+N) % 약수 == 0인 N을 구한다.

ans = 10 ** 10
min_lcm = 10**19
for i in arr:
    if (a + n) % i == (b + n) % i == 0:
        lcm = math.gcd(a+n, b+n) * (a+n) * (b+n)
        if min_lcm > lcm:
            min_lcm = lcm
            ans = n
        elif min_lcm == lcm:
            ans = min(ans, n)
    n += 1
print(ans)