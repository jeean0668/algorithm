import sys
input = sys.stdin.readline

n = int(input())
poses = [list(map(int, input().split())) for _ in range(n)]
paper = [[0 for _ in range(101)] for _ in range(101)]

def init():
    for pos in poses:
        for i in range(pos[0], pos[0] + 10):
            for j in range(pos[1], pos[1] + 10):
                paper[i][j] = 1
    # height가 저장된 새로운 그래프 생성
    for i in range(100, -1, -1):
        for j in range(101):
            if paper[i][j] != 0:
                paper[i][j] = paper[i+1][j] + 1
def cal(hist):
    stack = [0]
    ret = 0
    for i in range(1, len(hist)):
        if hist[i] == 0:
            continue
        if hist[i] > hist[stack[-1]]:
            stack.append(i)
        else:
            while hist[i] <= hist[stack[-1]]:
                top = stack.pop()
                cur = stack[-1]
                ret = max(ret, hist[top] * (i - cur - 1))
            stack.append(i)
    return ret
def solve():
    init()
    max_size = 100
    for p in paper:
        max_size = max(max_size, cal(p))
    print(max_size)
        
        
