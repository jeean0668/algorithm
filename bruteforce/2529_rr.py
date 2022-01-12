import sys
input = sys.stdin.readline

n = int(input())
signs = list(map(str, input().split()))
isUsed = [False] * 10
ans_max = '' 
ans_min = ''
def dfs(idx, tmp):
    global ans_max, ans_min
    if idx == n+1:
        if len(ans_min) == 0:
            ans_min = tmp
        else:
            ans_max = tmp
        return
   
    for i in range(10):
        if isUsed[i]: continue
        if idx == 0:
           
            isUsed[i] = True
            dfs(idx + 1, tmp + str(i))
            isUsed[i] = False
        
        elif signs[idx - 1] == '<' and tmp[-1] < str(i):
           
            isUsed[i] = True
            dfs(idx + 1, tmp + str(i))
            isUsed[i] = False
        elif signs[idx - 1] == '>' and tmp[-1] > str(i):
          
            isUsed[i] = True
            dfs(idx + 1, tmp + str(i))
            isUsed[i] = False
dfs(0, '')
print(ans_max)
print(ans_min)