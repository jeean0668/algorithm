import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
members = list(range(1, n+1))

first = list(combinations(members, n//2))

def cal(team):
    
    ret = 0
    for i in range(len(team) - 1):
        idx1 = team[i]
        for j in range(i+1, len(team)):
            idx2 = team[j]
            ret += s[idx1-1][idx2-1] + s[idx2-1][idx1-1]
    return ret


ans = sys.maxsize
for i in range(len(first)//2):
    team1 = first[i]
    team2 = first[-i-1]
    ans = min(ans, abs(cal(team1) - cal(team2)))
    
print(ans)