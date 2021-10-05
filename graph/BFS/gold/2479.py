"""
해밍 경로 : 모든 인접한 해밍 거리가 1인 경로
해밍 거리 : 서로 다른 비트의 갯수 
가장 짧은 해밍 경로를 찾아라

N : 주어진 비트 갯수, K : 비트 길이, 마지막 줄 : (시작점, 도착점)
경로 없으면 -1, 있으면 경로를 출력

1. 시작점을 기준으로, 해밍 경로가 1인 점을 queue에 삽입한다.
2. queue에서 pop한 비트의 index가 종점의 index와 같다면, 지금까지의 경로를
출력한다.

"""
import sys
from collections import deque
input = sys.stdin.readline

def getInput():
    global n, k, array
    n, k = map(int, input().split())
    array = []
    for _ in range(n):
        row = list(map(str, input().rstrip()))
        array.append(row)
def distance(A, B):
    global k
    A = list(map(int, A))
    B = list(map(int, B))
    # A와 B의 자릿값중 다른 것들을 카운트한다. 
    cnt = 0 
    for i in range(k):
        if A[i] != B[i]:
            cnt += 1
    return cnt

def findPath(start_idx, val):
    global prev, result
    if start_idx == val:
        result.append(str(val + 1))
        return
    result.append(str(val + 1))
    findPath(start_idx, prev[val])




def bfs(start_index, end_index):
    
    global array, n, prev, result
   
    visited = [False for _ in range(n + 1)]
    prev = [-1 for _ in range(n+1)]
    result = []
    queue = deque()

    start = array[start_index]
    visited[start_index] = True
    queue.append([start, 0])

    while queue:
        now, cnt = queue.popleft() 
        now_idx = array.index(now)
        if now_idx == end_index:
            #print(array[end_index], prev[end_index])
            findPath(start_index, end_index)
            result.reverse()
            result = list(map(str, result))
            s = " ".join(result)
            print(s)
            return 
        for i in range(0, now_idx):
            if distance(array[i], now) == 1 and not visited[i]:
                visited[i] = True
                queue.append([array[i], cnt + 1])
                prev[i] = now_idx
        for i in range(now_idx, len(array)):
            if distance(array[i], now) == 1 and not visited[i]:
                visited[i] = True
                queue.append([array[i], cnt + 1])
                prev[i] = now_idx
    print(-1)


def solve():
    s_idx, e_idx = map(int,input().split())
    bfs(s_idx-1, e_idx-1)

if __name__ == "__main__":
    getInput()
    solve()