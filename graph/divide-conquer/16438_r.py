import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)
def getInput():
    global n, graph
    n = int(input())
    graph = [['A' for _ in range(n)] for _ in range(7)]

def solve(start, end, day):
    global n, graph
    if day == 7:
        return
    mid = (start + end)//2
    # 절반만 바꿔준다.
    for i in range(start, mid):
        graph[day][i] = 'A'
    for j in range(mid, end):
        graph[day][j] = 'B'
    solve(start, mid, day + 1)
    solve(mid, end, day + 1)

if __name__ == "__main__":
    getInput()
    solve(0, n, 0)
    for row in graph:
        if 'A' not in row:
            row[0] = 'A'
        print("".join(row))