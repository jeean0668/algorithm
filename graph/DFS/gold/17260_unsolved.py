"""
전형적인 DFS 문제...라고 생각했으나 시간초과로 뚜드려 맞았다. 
N이 최대 20만이기 때문에, for문으로 모든 점에서 dfs 하는것은 불가능하다. 
따라서, 출발할 수 있는 점들을 추려야한다. 
2. 출발지점의 높이가 k번째보다 낮으면 pass했다. -> recursionerror 발생했다. 
3, setrecursionlimit를 키워줬더니 36프로에서 틀렸다. 
4. dfs방식을 바꿔야할 것 같다. 먼저 k로 도착하는 가장 긴 경로를 먼저 찾고(1), 높이가 가능한지 판별(2)하는
두 방식을 혼합했다. 

"""

# 전역변수 선언
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
graph = []
result = []
path = []

def getInput():
    global n, k, heights, graph, visited, c
    n, k = map(int, input().split())
    heights = list(map(int, input().split()))
    heights.insert(0, 0)
    
    graph = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    #c = [0 for _ in range(n+1)]
    
    for _ in range(n-1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        
# dfs로 경로 찾는 함수 
def dfs(node):
    global graph, n, k, visited, result, path
    visited[node] = True
    path.append(node)
    if len(graph[node]) == 1 and visited[graph[node][0]]:
       
        result.append(path.copy())
        path.pop()
    else:
        for child in graph[node]:
            if not visited[child]:
                dfs(child)
        path.pop()
    
        
    return False
    
if __name__ == "__main__":
    getInput()
    
    for i in range(1, n+1):
        # 높이가 k번째 보다 낮으면 pass한다. 
        if i == k or heights[i] < heights[k]:
            continue
        # k부터 시작하는 가장 긴 경로를 선택한다. 
        dfs(k)
        print(result)