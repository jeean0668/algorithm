"""
방식은 맞았으나 어디선가 틀린부분이 발견되어 코드 참조함.
분할정복 전형적인 문제로, row_start, row_end, col_start, col_end 로
사분면을 나누는게 핵심, 종료조건은 star>=2, star == 1 and impure == 1, star == 0 일때 0 반환, 
star == 1일때 1 반환한다. 


"""


import sys
N = int(input())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def solve(sy, sx, ey, ex, direction):
    count = [0] * 3
    for i in range(sy, ey + 1):
        for j in range(sx, ex + 1):
            if table[i][j]:
                count[table[i][j]] += 1
    if count[1] < count[2] - 1:
        return 0
    elif count[1] == 0 and count[2] == 1:
        return 1

    out = 0
    # 0이 가로로 1이 세로로 자르는 경우
    if direction != 1:
        for row in range(sy + 1, ey):
            isDirty, isCrystal = False, False
            for col in range(sx, ex + 1):
                if table[row][col] == 1:
                    isDirty = True
                elif table[row][col] == 2:
                    isCrystal = True
            if isDirty and not isCrystal:
                out += solve(sy, sx, row - 1, ex, 1) * solve(row + 1, sx, ey, ex, 1)
    if direction != 0:
        for col in range(sx + 1, ex):
            isDirty, isCrystal = False, False
            for row in range(sy, ey + 1):
                if table[row][col] == 1:
                    isDirty = True
                elif table[row][col] == 2:
                    isCrystal = True
            if isDirty and not isCrystal:
                out += solve(sy, sx, ey, col - 1, 0) * solve(sy, col + 1, ey, ex, 0)
    return out


result = solve(0, 0, N-1, N-1, -1)
print(result if result else -1)