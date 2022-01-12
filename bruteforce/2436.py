import sys
import math
input = sys.stdin.readline

"""
gcd 구하는 방법 : 유클리드 호제법
약수 모두 구하는 방법 : 
1. target value의 제곱근을 구한다.
2. for문으로 제곱근의 약수를 모두 구한다.
3.  target value를 제곱근의 약수로 나눈 값을 모두 구한다. 
"""
gcd, lcm = map(int, input().split())

answer = [sys.maxsize, sys.maxsize]
def gcd_func(first, second):
    while first % second != 0:
        r = first % second
        first = second
        second = r
    return second

result = gcd * lcm

# result 약수들을 구한다.

arr = []
for i in range(1, int(math.sqrt(result))+1):
    if result % i == 0:
        arr.append(i)
        if i != (result // i) : arr.append(result // i)
arr.sort()
for a in arr:
    if a < gcd : continue
    if answer[0] + answer[1] > a + (result // a):
        if gcd_func(a, result//a) == gcd:
            answer = [a, result // a]

print(*answer)