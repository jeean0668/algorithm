"""
트리 : 사이클이 없는 연결요소
1. input에 주어진 그래프에 있는 트리 갯수 + input에 주어지지 않은 노드 개수를 구한다.
2. 첫 시도 : dfs로 cycle 찾는 법에 대해 미숙하다. 매우 중요!!!  
3. 20%에서 틀려서, 노드를 구분하지 않고 통째로 실행 -> 계속 틀림 

한 노드에서 인접한 노드를 찾고, 그 노드에서 인접한 노드를 찾는 방식을 반복 -> 재귀함수 
 => 노드와 다음 노드 사이의 관계가 중요할 때 사용 ex) visited를 재사용 해야할때
그 외 -> stack을 이용한 재귀함수 . 
"""

# 전역변수 선언
import sys
import copy
input = sys.stdin.readline

# 그래프 입력
def isTree(node, prev):
    
    visited[node] = True
    for child in graph[node]:
        
        if child == prev:
            continue
        if visited[child]:
            return False
        if not isTree(child, node):
            return False
    return True
    
            
# main 함수
index = 1
while True:
    n, e = map(int, input().split())
    
    if n == 0 and e == 0:
        break
    visited = [False] * (n+1)
    graph = [[] for _ in range(int(n * (n - 1) / 2) + 1)]
    #parent = [[-1] for _ in range(int(n * (n - 1) / 2) + 1)]
    for _ in range(e):
        p, c = map(int, input().split())
        # 그래프에 노드 추가 
        graph[p].append(c)
        graph[c].append(p)
 
    # dfs로 트리 여부 탐색
    result = 0
    for ele in range(1, n+1):
        
        if not visited[ele]:
            if isTree(ele, 0):
                visited[ele] = True
                result += 1
    if result == 1:
        print("Case {}: There is one tree.".format(index))
    elif result > 1:
        print("Case {}: A forest of {} trees.".format(index, result))
    else:
        print("Case {}: No trees.".format(index))
    index += 1
        
    