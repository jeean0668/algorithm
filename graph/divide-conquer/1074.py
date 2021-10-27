import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

def solve(rs, re, cs, ce):
    if re-rs == 2:
        cnt = 1
        for i in range(rs, re):
            for j in range(cs, ce):
                if i == r and j == c:
                    return cnt
                cnt += 1
    if rs<=r<(rs+re)//2 and cs<=c<(cs+ce)//2:
        return solve(rs, (rs+re)//2, cs, (cs+ce)//2)
    elif rs<=r<(rs+re)//2 and (cs+ce)//2<=c<ce:
        return (((re-rs)//2)**2 + solve(rs, (rs+re)//2, (cs+ce)//2, ce))
    elif (rs+re)//2<=r<re and cs<=c<(cs+ce)//2:
        return (((re-rs)//2)**2)*2 + solve((rs+re)//2, re, cs, (cs+ce)//2)
    elif (rs+re)//2<=r<re and (cs+ce)//2<=c<ce:
        return (((re-rs)//2)**2)*3 + solve((rs+re)//2, re, (cs+ce)//2, ce)

print(solve(0, 2**n, 0, 2**n) - 1)