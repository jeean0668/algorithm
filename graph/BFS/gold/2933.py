"""
1. 주어진 높이에서 가장 왼쪽에 있거나 오른쪽에 있는 x를 .으로 바꾼다. 
2. 클러스터(연결 되어있는 집합)을 끝까지 조사해보았을 때, 바닥에 닿는 
좌표(n-1, _)를 가진 연결 요소가 없으면,  모든 요소들을 최대한 낮은 곳으로
내린다(bfs + while문을 활용한 graph 변형)
-> 각 column의 바닥부터 연결된 높이를 구한다.
"""
def getInput():
    global r, c, graph, n, heights
    r, c = map(int ,input().split())
    graph = [list(map(str, input().rstrip())) for _ in range(n)]
    n = int(input())
    heights = list(map(int, input().split()))

def remove(h, left = True):
    global graph, r
    selected = graph[r - h]
    if left:
        for i in range(len(selected)):
            if selected[i] == 'x':
                selected[i] = '.'
                break
    else:
        for i in range(len(selected), -1, -1):
            if selected[i] == 'x':
                selected[i] = '.'
                break

def change():
    global graph, r, c, visited
    visited = [[False for _ in range(c + 1)] for _ in range(r + 1)]
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'x' and not visited[i][j]:
                if divided(i, j):


def solve():
    for h in heights:
        remove(h, True)
        change()

if __name__ == "__main__":
    getInput()
    solve()