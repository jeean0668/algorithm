import sys

n = int(input())
m = int(input())
arr = {str(i) for i in range(10)}
if m!=0:
    arr -= set(map(str, input().split()))

answer = abs(100 - n)

for i in range(1000001):
    num = str(i)
    for j in range(len(num)):
        if num[j] not in arr:
            break
        elif j == len(num) - 1:
            answer = min(answer, abs(n - int(num)) + len(num))

print(answer)
    