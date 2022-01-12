import sys
input = sys.stdin.readline

"""
답을 봤다.
1. 색종이가 덮여진 곳을 모두 1로 기록한다.
2. 1로 기록된 (i,j) 부터 rectangle 사이즈를 잰다.
3. 2중 for문으로 x좌표, y좌표를 하나씩 늘려가며, ((x, x+i), (y, y+j))가 모두 1로 덮여있는지 확인한다.
4. 만약 모두 덮여있다면 1의 총 갯수를 반환하고, 하나라도 0이 있다면 0을 반환한다. 

"""
def find_rectangle(x, y):
    max_size = 100
    for i in range(100):
        if x + i > 100:
            break
        for j in range(100):
            if y + j > 100:
                break
            max_size = max(max_size, cal(x,y, x+i, y+j))
    return max_size
def cal(x, y, h, w):
    cnt = 0
    for i in range(x, h+1):
        for j in range(y, w+1):
            if not paper[i][j]:
                return 0
            else:
                cnt += 1
    return cnt 


n = int(input())
paper = [[0] * 101 for _ in range(101)]
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1
max_size = 100
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            max_size = max(max_size, find_rectangle(i, j))
print(max_size)

