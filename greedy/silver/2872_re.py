import sys

N = int(input())

ans = []
for i in range(N):
    ans.append(int(input()))

max_num = N

for index in range(N-1, -1, -1):
    if ans[index] == max_num:
        max_num -= 1

print(max_num)