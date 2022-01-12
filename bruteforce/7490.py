import sys
input = sys.stdin.readline

test_cases = int(input())


def isZero(array):
    
    tmp = array.replace(' ', '')
    if eval(tmp) == 0:
        print(array)

def dfs(num, arr):
    global ans, n
    if num == n+1:
        isZero(arr)
        return
    dfs(num + 1, arr + ' ' + str(num))
    dfs(num + 1, arr + '+' + str(num))
    dfs(num + 1, arr + '-' + str(num))
    
for _ in range(test_cases):
    n = int(input())
    ans = []
    dfs(2, '1')
    print()
    