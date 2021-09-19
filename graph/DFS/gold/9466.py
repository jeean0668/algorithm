"""
그래프 내에 존재하는 모든 사이클들의 길이 합을 구하는 문제이다.
그래프 사이클의 길이를 어떻게 구할것인지가 관건
"""

# 전역변수 선언
import sys
input = sys.stdin.readline

# input

def dfs(node, count):
    
    global visited
    global depth
    global finished
    visited[node] = True
    depth[node] = count
    
    ret = 0
    for child in graph[node]:
        if not visited[child]:
            ret = dfs(child, count + 1)
            continue
        if finished[node]:
            # 이미 방문했는데 탐색도 완전히 끝난 경우
            continue
        if finished[child]:
            # 자녀가 이미 방문한 노드인데 탐색도 끝나버린 경우 
            ret = 0
            continue
        ret += (depth[node] - depth[child] + 1)
        #print(node, child, depth[node], depth[child])
    finished[node] = True
    return ret
            
    
    
def solve(num):
    CycleSize = 0
    for i in range(1, n+1):
        cnt = 1
        if not visited[i]:
            
            temp = dfs(i, cnt)
            CycleSize += temp
    print(num - CycleSize)

if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        n = int(input())
        graph = [[] for _ in range(n+1)]
        visited = [False] * (n+1)
        finished = [False] * (n+1)
        depth = [0] * (n+1)
        nodes = list(map(int, input().split()))
        # 그래프 생성 
        for i in range(1, n+1):
            graph[i].append(nodes[i-1])
        # dfs 실행
        solve(n)
        
                