import sys
input = sys.stdin.readline

N = int(input())
gram = list(map(int, input().split()))

gram.sort()

temp = 0
finish = False
for i in range(N):
    now = gram[i]
    if now >= temp + 2:
        temp += 1
        finish = True
        break
    temp += now

print(temp) if finish else print(temp+1)
