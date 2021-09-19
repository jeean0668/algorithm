"""
9466 개선된 방식
"""

import sys
sys.setrecursionlimit(111111)

def dfs(x):
    global ans
    visited[x] = 1
    num = numbers[x-1]
    cycle.append(x)

    if visited[num] == 1: 
        if num in cycle:
            # 이미 방문한 점인데 cycle list에 포함된 점일경우
            ans.extend(cycle[cycle.index(num):])
            # ans라고 하는 global list에 num부터 마지막 cycle 원소까지 추가한다.
        return
    else:
        dfs(num)
  
for _ in range(int(input())):
    n = int(input())
    numbers = list(map(int,input().split()))
    visited = [0] * (n+1)
    ans = []

    for i in range(1,n+1):
        if visited[i] == 0:
            cycle = []
            dfs(i)

    print(n - len(ans))