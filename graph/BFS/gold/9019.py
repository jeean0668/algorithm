"""
단순하게 bfs로 풀어줬을 때 시간초과가 났다. 
오른쪽 회전, func_S를 수정해주었는데, 역시 시간초과가 났다.
회전하는 방식에서 새로운 아이디어가 필요했는데
"""


import sys
from collections import deque
input = sys.stdin.readline

def solve(num):
    for _ in range(num):
        a, b = map(int, input().split())
        result = bfs(a, b)
        print(result)

def func_D(num):
    # 두배로 바꾼 값을 반환
    res = num*2
    if res > 9999:
        return res % 10000
    return res
    
def func_S(num):
    # n-1을 반환
    if num == 0:
        return 9999
    return num-1

def func_L(num):
    # 왼쪽으로 회전시킨 값 반환
    front = num % 1000
    back = num // 1000
    return front * 10 + back
def func_R(num):
    # 오른쪽으로 회전시킨 값 반환
    back = num % 10
    front = num // 10
    return back * 1000 + front
    
def bfs(start, end):
   

    queue = deque()
    queue.append((start, ''))
    visited = [False for _ in range(10001)]
    visited[start] = True
    
    while queue:
        now, s = queue.popleft()
        
        if now == end:
            return s
        _next = func_D(now)
        if not visited[_next]:
            visited[_next] = True
            queue.append((_next, s + 'D'))
        _next = func_S(now)
        if not visited[_next]:
            visited[_next] = True
            queue.append((_next, s + 'S'))
        _next = func_L(now)
        if not visited[_next]:
            visited[_next] = True
            queue.append((_next, s + 'L'))
        _next = func_R(now)
        if not visited[_next]:
            visited[_next] = True
            queue.append((_next, s + 'R'))


if __name__ == "__main__":
    num = int(input())
    solve(num)