"""
0인 칸에 인접한 숫자들을 밀어넣을 수 있다.(원래 있던 공간은 0이 된다.)
이때 [[1,2,3], [4,5,6], [7,8,0]] 으로 만들 수 있는 최소 횟수를 구하라


아이디어가 중요한 문제였다. map으로 주어진 수를 하나의 string으로 바꿔서 
queue에 넣어주면, queue에 계속 그래프를 넣어주는 것보다 훨씬 메모리를 아낄 수 있다. 
"""
from collections import deque
import sys
input = sys.stdin.readline
from copy import deepcopy
dy = [-1, 0, 0, 1]
dx = [0, 1, -1, 0]

def getInput():
    global array, graph
    array = ''
    for i in range(3):
        row = input().rstrip()
        row = row.replace(' ', '')
        array += row
    array = array.replace('0', '9')

def solve():
    global array, graph
    queue = deque()
    queue.append(array)
    distance = dict()
    distance[array] = 0
    while queue:
        now = queue.popleft()
        if now == '123456789':
            return distance[now]
        now_pos = now.find('9')
        y, x = now_pos//3, now_pos%3
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0<=ny<3 and 0<=nx<3:
                # 인접한 숫자와 자리바꿈한 문자열로 변환
                next_pos = 3 * ny + nx
                next = list(now)
                next[next_pos], next[now_pos] = next[now_pos], next[next_pos]
                next = ''.join(next)
                if not distance.get(next):
                    queue.append(next)
                    distance[next] = distance[now] + 1
    return -1

if __name__ == "__main__":
    getInput()
    print(solve())
