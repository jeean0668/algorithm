"""
타일의 한 숫자만 바꿔서 최대한 큰 연결요소를 만드는 문제 
1. 0 타일이 발견되면, 그 타일을 1로 바꾸고 전체 맵에서 가장 큰 연결요소를 찾는다.
 -> 시간초과 발생 ( n, m이 최대 1000)
2. 연속된 1 타일들을 그룹화하여, 1 대신 그룹의 번호로 바꿔줌.
    - 0 타일 기준으로 인접한 그룹들의 총 사이즈 - (중복해서 더해준 횟수 - 1)
    값을 구함
    - 
 -> 92프로에서 메모리 초과가 뜬다 -> DFS의 문제인것 같다. 이문제는 BFS로 해결해야 하는것 같다. 
"""

# 전역변수
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
#main
n, m = map(int, input().split())
graph = []
dy = [-1, 0, 0, 1]
dx = [0, 1, -1, 0]

# 그래프 생성
for _ in range(n):
    graph.append(list(map(int, input().split())))

    
def dfs(y,x, cnt):
    # 현재 타일이 속한 연결요소들을 그룹화한다.
    stack = [[y, x, cnt]]
    ret = 1
    global visited
    while stack:
        top = stack.pop()
        visited[top[0]][top[1]] = True
        graph[top[0]][top[1]] = top[2]
        for i in range(4):
            ny = top[0] + dy[i]
            nx = top[1] + dx[i]
            if 0<=ny<n and 0<=nx<m:
                
                if graph[ny][nx] == 0:
                    continue
                if visited[ny][nx]:
                    continue
                stack.append([ny, nx, top[2]])
                ret += 1
    return ret
                    

def search(y, x):
    
    dup = 0
    temp_size = 0 
    checked = []
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<n and 0<=nx<m:
            if graph[ny][nx] in checked:
                continue
          
            if graph[ny][nx] == 0:
                continue
            # 주변에 있는 group size + 1 저장
            temp_size += (Size[graph[ny][nx]] + 1)
            # 중복해서 더하게 되는 값 저장 
            dup += 1
            checked.append(graph[ny][nx])
    # 주변에 있는 모든 group size 합 - (중복해서 더한 값 - 1) 반환 
    return temp_size - (dup - 1)
            
            
                
# main
cnt = 1
Size = [[] for _ in range(n * m + 1)]
visited = [[False for _ in range(m)] for _ in range(n)]

for y in range(n):
    for x in range(m):
        # 타일의 값이 1일때 dfs로 그룹화 한 값 저장
        if graph[y][x] == 1 and not visited[y][x]:
            g_size = dfs(y, x, cnt)
            # cnt번호에 group size 저장 
            Size[cnt] = g_size
            cnt += 1
result = 0
for y in range(n):
    for x in range(m):
        # 0 타일 기준으로 searching
        if graph[y][x] == 0:
            result = max(result, search(y, x))
print(result)
            