"""
최소 피로도로 모든 목적지에 도달해야한다.
피로도는 방문한 모든 점들의 최고 고도 - 최저 고도, 방문했던 점을 다시 방문할 수도 있다. 
N이 최대 50이라 시간복잡도는 여유있다.
map에 위치한 모든 K부터 P까지 최소 피로도로 갈 수 있는 방법을 각각 구하고, 계산된 최소 피로도
들 중 최댓값을 고른다. --> 전부 실패

결국 해설을 봤다.
1. heights를 중복값 없이 저장한다.
2. left, right라고 하는 투포인터가 heights의 첫번째 원소를 가리키게 한다.
3. heights[left]~heights[right] 범위 내의 고도에서 K까지 도달할 수 있으면
left 를 +1 하고, 도달할 수 없으면 right를 +1 해준다.
4. heights[right]와 heights[left] 차의 최솟값을 구해준다. 

--> 결국 dfs나 bfs만으로 할 수 있는건
1. 경로 찾기, 2. 특정 원소의 갯수 찾기, 3. 경로 길이 찾기, 4. cycle 찾기
정도이므로, 다른 조건들이 들어간 문제는 조건을 적절히 이용하여
위의 네가지 케이스중 하나로 적용시켜야 한다.

이 문제는 heights라는 배열과 투포인터를 활용하고, 2번 특정 원소의 갯수를 찾는
bfs 알고리즘을 활용하여 해결한 것이다. 
"""

# 전역변수 선언

import sys
from collections import deque

# 위, 아래, 좌, 우, 대각선
dr = [-1,1,0,0,-1,1,1,-1]
dc = [0,0,-1,1,-1,-1,1,1]

# BFS + 투 포인터
N = int(input())
board = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(N)]
altitude = [[int(x) for x in sys.stdin.readline().split()] for _ in range(N)]

houses = 0
fatigue = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 'P':
            px, py = i, j
        elif board[i][j] == 'K':
            houses += 1
        fatigue.append(altitude[i][j])

# 1. 입력받은 pirodo에 대해서 정렬 and set을 통한 중복 제거
fatigue = sorted(set(fatigue))
#print("fatigue : ", fatigue)

left, right = 0,0
answer = sys.maxsize


def bfs(start_x,start_y):
    visit = [[False]*N for _ in range(N)]
    queue = deque([(start_x,start_y)])
    visit[start_x][start_y] = True
    K = 0   # 방문한 집의 갯수

    while queue:
        # print("queue : ", queue)
        x,y = queue.popleft()
        #print("{}, {} pop".format(x,y))

        # 수직, 수평, 대각선 탐색
        for i in range(8):
            nx,ny = x+dr[i], y+dc[i]

            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            if visit[nx][ny]:
                continue

            tired = altitude[nx][ny]

            # 현재 피로도가 left, right 사이일 경우에만 추가로 탐색
            if fatigue[left] <= tired <= fatigue[right]:
                #print("좌표={},{} , 피로도={} ({}~{})".format(nx,ny,tired,fatigue[left],fatigue[right]))

                visit[nx][ny] = True
                queue.append((nx,ny))

                # 집이면 K 증가
                if board[nx][ny] == 'K':
                    K += 1
    return K


while left<len(fatigue):
    #print("left : ", left,", right : ",right, end='  - ')
    #print("{} ~ {}".format(fatigue[left], fatigue[right]))
    K=0

    # 3. 시작점의 고도가 최대 고도와 최소 고도 사이일 경우에만 BFS를 시작
    if fatigue[left] <= altitude[px][py] <= fatigue[right]:
        #print("BFS start!")
        K = bfs(px, py)

    # 집을 모두 방문함
    if K == houses:
        # 최소 피로도 구하기
        answer = min(answer, fatigue[right]-fatigue[left])
        #print("집을 모두 방문! answer : ", answer)

        left += 1  # 최소 높이 증가
    elif (right+1) < len(fatigue):
        # 아직 최대고도가 남아있을 때 최대 고도 증가
        #print("아직 최대 고도가 남음.. ")
        right += 1
    else:
        #print("모두 아닐 때,, ")
        break
    #print()

print(answer)
    