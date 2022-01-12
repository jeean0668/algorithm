import sys
n = int(input())
signs = input().split()
dp = [False] * 10



def possible(s, t, index):
    
    if signs[index] == "<":
        return s < t
    elif signs[index] == ">":
        return s > t
    
mx, mn = "", ""
def find(s, index):
    
    global mx, mn
    if index == n+1:
        if len(mn) == 0:
            mn = s
        else:
            mx = s
        return
    for i in range(10):
        if len(s) == 0:
            dp[i] = True
            find(s + str(i), index + 1)
            dp[i] = False
        elif not dp[i] and possible(s[-1], str(i), index - 1):
            dp[i] = True
            find(s + str(i), index + 1)
            dp[i] = False

find("", 0)
print(mx)
print(mn)