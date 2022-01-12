import sys
input = sys.stdin.readline

"""
누적합을 구해야하는 문제였다.
i 높이 이상의 석순과 종유석 갯수를 구하여 저장한다는것이 핵심이다. 
특정 높이에서 장애물 갯수의 총 합이 저장된 값보다 더 작으면, 저장된 값을 갱신한다.

"""

n, h = map(int, input().split())
up, down = [0] * (h+1), [0] * (h+1)
obs_cnt = n
r_cnt = 0

for i in range(n):
    if i % 2 == 0 : down[int(input())] += 1
    else : up[int(input())] += 1

# 높이 i 이상의 석순과 종유석 갯수를 구하여 저장 -> 이분탐색으로도 가능하다.
for i in range(h-1, 0, -1):
    down[i] += down[i+1]
    up[i] += up[i+1]

for i in range(1, h+1):
    if obs_cnt > down[i] + up[h - i + 1]:
        obs_cnt = down[i] + up[h - i + 1]
        r_cnt = 1
    elif obs_cnt == down[i] + up[h-i+1]:
        r_cnt += 1
print(obs_cnt, r_cnt)
