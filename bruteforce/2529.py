import sys

n = int(input())
signs = input().split()

mem = [False] * 10

mn, mx = '', ''
def dfs(s, size):
    global mn, mx
    if size == n+1:
        if len(mn) == 0:
            mn = s
        else:
            mx = s
        return 
    for i in range(10):
        if mem[i] : continue
        if size == 0:
            mem[i] = True
            dfs(s + str(i), size + 1)
            mem[i] = False
            continue
        if signs[size-1] == '<' and s[-1] < str(i):
            mem[i] = True
            dfs(s + str(i), size + 1)
            mem[i] = False
            continue
        if signs[size - 1] == '>' and s[-1] > str(i):
            mem[i] = True
            dfs(s + str(i), size + 1)
            mem[i] = False
            continue
dfs('', 0)
print(mx)
print(mn)