"""
그리디 문제이자 스위핑 문제이다.... 라고 생각했지만 부분적으로만 맞았다.
아이디어는 좋았는데, 시간복잡도가 문제였다. 분리집합을 union-find라는 알고리즘으로
구현해야 했다.
union-find라는 알고리즘을 배워본적이 없어서, 그것부터 다시 시작했다.
union-find는 parent를 찾는 과정인 findParent, 누가 더 조상인지 판별하는 union이 있다.
두 원소의 조상을 findParent를 통해 재귀호출하여 찾고, x 부모보다 y 부모가 더 조상이면 
x 부모를 y로 설정한다. 
 ----> 특정 집합으로 분리해야할 경우 union-find 알고리즘을 사용한다.
 ----> union : 두 원소를 하나의 집합으로 합치는 과정(findParent로 조상 확인)
 ----> find : 두 원소의 조상이 같으면 하나의 집합으로 합친다. 
"""

# 전역변수
import sys
input = sys.stdin.readline
lines = []
groups = []

def getInput():
    global q, jump, parent, lines
    n, q = map(int, input().split())
    parent = [i for i in range(100001)]
    lines = [[-1, -1]]
    #y좌표는 중요하지 않다
    for i in range(1, n+1):
        x_1, x_2, _ = map(int, input().split()) 
        lines.append([x_1, x_2, i]) # x1 순으로 정렬
    lines.sort(key = lambda x : x[0])
def findParent(x):
    global parent
    if x == parent[x]:
        # 그래프의 가장 끝에 도달했을때,
        return x
    else:
        parent[x] = findParent(parent[x])
        return parent[x]
def union(x, y):
    global parent
    x = findParent(x)
    y = findParent(y)
    # y의 부모가 x의 부모보다 조상일 경우
    if x > y:
        parent[x] = y
    else:
        parent[y] = x
def merge():
    # 연결된 노드들을 union하는 함수
    global lines
   
    cur_start, cur_end, _ = lines[1]
    for i in range(2, len(lines)):
        start, end, _ = lines[i]
        if cur_end >= start:
            cur_end = max(cur_end, end)
            # 같은 집합으로 union 해준다.
            union(lines[i-1][2], lines[i][2])
        else:
            cur_start = start
            cur_end = end
        
if __name__ == "__main__":
    global parent
    getInput()
    merge()
    for _ in range(q):
        start, end = map(int, input().split())
        parent[start] = findParent(start)
        parent[end] = findParent(end)
        print(1) if parent[start] == parent[end] else print(0)
    