import sys

input = sys.stdin.readline
N = int(input())
array = list(map(int, input().split()))

length = len(array)
minus, r = 0, 0
for i in range(length):
    now = array[i]
    divide = 0
    while now > 0:
        if now % 2 == 1:
            now -= 1
            minus += 1
        else:
            now /= 2
            divide += 1
    r = max(r, divide)
print(r + minus)