"""
1. nxn 사이즈에서 시작한다.
2. 만약 현재 범위 ((y_1, y_2), (x_1, x_2))의 모든 원소가 0이면 0의 갯수를 반환한다.
3. 아니면 ((y_1+1, y_2), (x_1, x_2)), ((y1, y_2 - 1), (x_1, x_2)), ((y_1, y_2),(x_1+1, x_2)), ((y_1, y_2), (x_1, x_2-1)) 네가지 경우로 분할하여 재탐색
-> TLE발생, dynamic 하게 할 수 있는 다른 방법 고안 필요 

1. 부분집합 -> 000,111,000일때 최대 사이즈는 6이다!(주의)
"""

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
matrix = [list(map(int, list(input().rstrip()))) for _ in range(n)]

def transform(mat):
    ret = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0: ret[i][j] = 1-mat[i][j]
            else:ret[i][j] = 0 if mat[i][j] else ret[i-1][j]+1
    return ret
def cal(hist):
    hist = [-2] + hist + [-1]
    stack = [0]
    ret = 0
    for i in range(1, len(hist)):
        if hist[i] > hist[stack[-1]]:
            stack.append(i)
        else:
            while hist[i] <= hist[stack[-1]]:
                top = stack.pop()
                width = stack[-1]
                ret= max(ret, (i-width-1) *hist[top])
            stack.append(i)
    return ret
def solve():
    h = transform(matrix)
    result = 0
    for t in h:
        result = max(result, cal(t))
    return result
print(solve())