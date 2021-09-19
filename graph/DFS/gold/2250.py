"""
이진트리의 inorder로 해결하는 문제로 추측됨
1. root가 1이 아닐수 있음을 생각하지 못했다. 
2. findroot로 root을 찾아줬는데 92퍼센트에서 에러 
3. 극단적인 케이스에 대해서 고려해 줬더니 정답 통과(루트 노드만 있을때를 
고려해주었다. )
"""

# 전역변수 선언

import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)

# 그래프 입력 
def makeGraph(n):
    global graph
    global c
    global pointer
    global parent
    graph = [[] for _ in range(n+1)]
    c = [[] for _ in range(n+1)]
    parent = [[] for _ in range(n+1)]
    for _ in range(n):
        node, left, right = map(int, input().split())
        graph[node].append(left)
        graph[node].append(right)
        if left != -1:
            parent[left].append(node)
        if right != -1:
            parent[right].append(node)
        # graph[node][0]에는 left, graph[node][1] 에는 right이다.
       
    pointer = n
# 루트 찾는 함수

def findRoot(n):
    # parent[node]의 길이가 0인것을 반환한다. -> root는 parent가 없기 때문
    for i in range(1, n+1):
        node = parent[i]
        if len(node) == 0:
            return i
    
def dfs(node, depth):
    
    global pointer
    global graph
    global c
    
    children = graph[node]
    left = children[0]
    right = children[1]
    if right != -1:
        dfs(right, depth+1)
    c[depth].append(pointer)
    pointer -= 1
    if left != -1:
        dfs(left, depth + 1)
# main
if __name__=="__main__":
    n = int(input())
    makeGraph(n)
    root = findRoot(n)
    dfs(root, 1)
    result = 0
    result_depth = 1 # default depth = 1
    for i in range(1, n+1):
        row = c[i]
        if len(row) == 0:
            break
        cmp = max(row) - min(row)
        if result < cmp:
            result_depth = i
            result = cmp
    print(result_depth, result+1)
    