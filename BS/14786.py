import sys
import math
input = sys.stdin.readline

a, b, c = map(int, input().split())
left, right = (c-b)/a, (c+b)/a

def calculation(x):
    return a * x + b * math.sin(x)

stopper = 50000
mid = 0 
while left < right and stopper > 0:
    mid = (left + right) / 2
    cal = calculation(mid)
    if mid > (c - b * math.sin(mid)) / a:
        right = mid
    elif mid < (c - b * math.sin(mid)) / a:
        left = mid + 10 ** (-19)
    stopper -= 1
    
print(round(mid, 19))