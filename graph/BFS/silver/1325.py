
"""
bfs로 풀이해본 문제로, dfs로 하면 더 쉽게 풀 수 있을 것 같다.
bfs 함수에서 변수로 입력받은 노드로부터 도달할 수 있는 최대 깊이를 반환한다.
만약 그 깊이가 max_depth보다 깊다면 result list에 그 원소를 추가한다. 
"""

from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append(start)
    visit = [0 for _ in range(n + 1)]
    visit[start] = 1
    cnt = 1
    while q:
        st = q.popleft()
        for i in s[st]:
            if visit[i] == 0:
                visit[i] = 1
                cnt += 1
                q.append(i)
    return cnt
n, m = map(int, input().split())
s = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    s[b].append(a)
result = []
max_cnt = 0
for i in range(1, n + 1):
    tmp = bfs(i)
    if max_cnt == tmp:
        result.append(i)
    if max_cnt < tmp:
        max_cnt = tmp
        result = []
        result.append(i)
print(*result)
        