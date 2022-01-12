import sys
n, m = map(int, input().split())
graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]

"""
1. 사각형을 세 직사각형으로 나눈다.
2. 세 직사각형 범위 내의 값들을 더해 모두 곱한다.
3. answer 값을 더 큰 값으로 갱신한다. 
"""

def cal(sy, ey, sx, ex):
    ret = 0
    for i in range(sy, ey):
        for j in range(sx, ex):
            ret += graph[i][j]
    return ret

answer = 0
# 1번 모양
for i in range(1, n):
    for j in range(1, m):
        first = cal(0, i, 0, m)
        second = cal(i, n, 0, j)
        third = cal(i, n, j, m)
        answer = max(answer, first * second * third)

# 2번 모양
for i in range(1, n-1):
    for j in range(i+1, n):
        first = cal(0, i, 0, m)
        second = cal(i, j, 0, m)
        third = cal(j, n, 0, m)
        #print(i, j, first * second * third)
        answer = max(answer, first * second * third)

# 3번모양
for i in range(1, m-1):
    for j in range(i+1, m):
        first = cal(0, n, 0, i)
        second = cal(0, n, i, j)
        third = cal(0, n, j, m)
        answer = max(answer, first * second * third)

# 4번 모양

for i in range(1, n):
    for j in range(1, m):
        first = cal(0, i, 0, j)
        second = cal(i, n, 0, j)
        third = cal(0, n, j, m)
        answer = max(answer, first * second * third)

# 5번 모양

for i in range(1, n):
    for j in range(1, m):
        first = cal(0, n, 0, j)
        second = cal(0, i, j, m)
        third = cal(i, n, j, m)
        answer = max(answer, first * second * third)


# 6번모양
for i in range(1, n):
    for j in range(1, m):
        first = cal(0, i, 0, j)
        second = cal(0, i, j, m)
        third = cal(i, n, 0, m)
        answer = max(answer, first * second * third)

        
print(answer)
        