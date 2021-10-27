import sys
input = sys.stdin.readline
#sys.setrecursionlimit(111111)

def getInput():
    global n, graph
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

def checked(row_s, row_e, col_s, col_e, color):
    global graph
    for i in range(row_s, row_e):
        for j in range(col_s, col_e):
            if graph[i][j] != color:
                return False
    return True


def solve(row_s, row_e, col_s, col_e, color):
    global n, graph
    
    check = checked(row_s, row_e, col_s, col_e, color)
    if check:
        return 1
    if not check and row_e - row_s == 1:
        return 0
    points_r = [row_s, int((row_s + row_e)/2), row_e]
    points_c = [col_s, int((col_s + col_e)/2) , col_e]
    first = solve(points_r[0], points_r[1], points_c[0], points_c[1], color)
    second = solve(points_r[1], points_r[2], points_c[0], points_c[1], color)
    third = solve(points_r[0], points_r[1], points_c[1], points_c[2], color)
    fourth = solve(points_r[1], points_r[2], points_c[1], points_c[2], color)
    return first + second + third + fourth

if __name__ == "__main__":
    getInput()
    print(solve(0, n, 0, n, 0))
    print(solve(0, n, 0, n, 1))