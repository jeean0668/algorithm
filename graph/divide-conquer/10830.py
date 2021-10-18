import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)

n, b = map(int, input().split())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

def matmul(m1, m2):
    global n
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += (m1[i][k] * m2[k][j])
            result[i][j] %= 1000
    
    return result


def solve(m, b):
    
    if b == 1:
        for i in range(n):
            for j in range(n):
                m[i][j]  %= 1000
        return m 
    if b % 2 == 0:
        temp = solve(m, b//2)
        return matmul(temp, temp)
    else:
        return matmul(m, solve(m, b-1))

result = solve(matrix, b)
for li in result:
    for p in li:
        print(p, end = ' ')
    print()