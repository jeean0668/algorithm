import sys
input = sys.stdin.readline

n, m, t, k = map(int, input().split())
pos = []
for _ in range(t):
    x, y = map(int, input().split())
    pos.append((x, y))

def check(x, y):
    cnt = 0 
    for p in pos:
        if x <= p[0] <= x+k and y <= p[1] <= y+k:
            cnt += 1
    return cnt
 
result = 0
result_pos_x, result_pos_y = 0, m
for i in range(t):
    for j in range(t):
        x = pos[i][0]
        y = pos[j][1]
        if x + k > n:
            x = n-k
        if y + k > m:
            y = m - k
        ans = check(x, y)
        if result < ans:
            result_pos_x, result_pos_y = x, y+k
            result = ans

print(result_pos_x, result_pos_y)
print(result)