import sys
input = sys.stdin.readline

n, m = map(int, input().split())
suggest = [list(input().rstrip()) for _ in range(n)]

ans1 = []
for rnum in range(n):
    row1 = []
    for i in range(m):
        if i % 2 == 0:
            if rnum % 2 == 0: row1.append('W')
            else: row1.append('B')
        else:
            if rnum % 2 == 0: row1.append('B')
            else: row1.append('W')
    ans1.append(row1)
    
ans2 = []
for rnum in range(n):
    row1 = []
    for i in range(m):
        if i % 2 == 0:
            if rnum % 2 == 0: row1.append('B')
            else: row1.append('W')
        else:
            if rnum % 2 == 0: row1.append('W')
            else: row1.append('B')
    ans2.append(row1)
    
cnt1, cnt2 = 0, 0
for i in range(n):
    for j in range(m):
        if ans1[i][j] != suggest[i][j]:
            cnt1 += 1

for i in range(n):
    for j in range(m):
        if ans2[i][j] != suggest[i][j]:
            cnt2 += 1

print(min(cnt1, cnt2))