import sys
input = sys.stdin.readline
n = int(input())
eles = [list(map(int, input().split())) for _ in range(n)]

answer = sys.maxsize
def dfs(index, cnt, cal1, cal2):
    global answer
    if index == n:
        if cnt == 0:
            return
        answer = min(answer, abs(cal2 - cal1))
        return
    dfs(index + 1, cnt, cal1, cal2)
    dfs(index + 1, cnt + 1, cal1 * eles[index][0], cal2 + eles[index][1])

dfs(0, 0, 1, 0)
print(answer)