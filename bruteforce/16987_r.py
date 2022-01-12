import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = 0
def dfs(index):
    global answer
    if index == n:
        # 끝까지 다 찾아본 후, 내구도가 0인 것들을 찾는다.
        cnt = 0
        for i in range(n):
            if arr[i][0] <= 0 : cnt+=1
        answer = max(answer, cnt)
        return
    if arr[index][0] <=0 : dfs(index + 1)
    else:
        flag = False
        for i in range(n):
            if index == i or arr[i][0] <= 0: continue
            arr[index][0] -= arr[i][1]
            arr[i][0] -= arr[index][1]
            flag = True
            dfs(index + 1)
            arr[i][0] += arr[index][1]
            arr[index][0] += arr[i][1]
        if not flag:
            dfs(n)

dfs(0)
print(answer)