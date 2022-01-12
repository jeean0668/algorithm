import sys
input = sys.stdin.readline
from itertools import combinations as cb

"""
1. 경기 수의 합이 모두 5가 아니면 불가능
2. 모든 승수의 합 != 모든 패수의 합 -> 불가능
3. 무승부 횟수가 같은 팀이 짝수개가 아니라면 불가능
"""

def solution(count):
    global ans, res
    if count == 15:
        ans = 1
        for sub in res:
            if sub.count(0) != 3:
                ans = 0
                break
        return
    
    t1, t2 = game[count]
    for x, y in ((0, 2), (1, 1), (2, 0)):
        if res[t1][x] > 0 and res[t2][y] > 0:
            res[t1][x] -= 1
            res[t2][y] -= 1
            solution(count+1)
            res[t1][x] += 1
            res[t2][y] += 1
        

game = list(cb(range(6), 2))
answer = []
for _ in range(4):
    data = list(map(int, input().split()))
    res = [data[i:i + 3] for i in range(0, 16, 3)]
    ans = 0
    solution(0)
    answer.append(ans)

print(*answer)