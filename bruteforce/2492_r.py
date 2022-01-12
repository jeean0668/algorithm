import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m, t, k = map(int, input().split())

minx, miny = INF, INF
maxx, maxy = 0, 0
array = []
for _ in range(t):
    x, y = map(int, input().split())
    array.append((x, y))
    
def check(x, y):
    cnt = 0
    for arr in array:
        if x <= arr[0] <= x + k and y <= arr[1] <= y + k:
            cnt += 1
    return cnt
    
ans_x, ans_y = 0, m
ans_cnt = 0

# 슬라이딩 윈도우 기법 
# 중복되는 요소들
for i in range(t):
    if array[i][0] + k > n : 
        xx = n - k
    else: 
        xx = array[i][0]
    for j in range(t):
        if array[j][1] + k > m : 
            yy = m - k
        else: 
            yy = array[j][1]
        cnt = check(xx, yy)
        if ans_cnt < cnt:
            ans_x, ans_y = xx, yy + k
            ans_cnt = cnt
            
print(ans_x, ans_y)
print(ans_cnt)