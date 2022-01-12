import sys
input = sys.stdin.readline

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]

maximum = 0

def change(y, x, ny, nx):
    graph[y][x], graph[ny][nx] = graph[ny][nx], graph[y][x]
    return

def count(y, x):
    #연속된 열의 갯수
    final, final2 = 0, 0
    row_max, col_max = 0, 0
    for i in range(n):
        start = graph[i][0]
        cnt = 0
        result = []
        for j in range(n):
            if start == graph[i][j]:
                cnt += 1
            else:
                start = graph[i][j]
                result.append(cnt)
                cnt = 1
        result.append(cnt)
        final = max(result)
        row_max = max(row_max, final)
    for i in range(n):
        start = graph[0][i]
        cnt = 0
        result = []
        for j in range(n):
            if start == graph[j][i]:
                cnt += 1
            else:
                start = graph[j][i]
                result.append(cnt)
                cnt = 1
        result.append(cnt)
        final2 = max(result)
        col_max = max(col_max, final2)
    return max(row_max, col_max)

for i in range(n):
    for j in range(n):
        now = graph[i][j]
        if j + 1 < n:
            right = graph[i][j+1]
            change(i, j, i, j+1)
            cnt = count(i, j)
            change(i, j, i, j+1)
            if cnt > maximum:
                maximum = cnt
        if i + 1 < n:
            bottom = graph[i+1][j]
            change(i, j, i+1, j)
            cnt = count(i, j)
           
            change(i, j, i+1, j)
            if cnt > maximum:
                maximum = cnt
print(maximum)