import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)

s,n,k,r1,r2,c1,c2 = map(int,input().split())

def inRange(y, x, border):
    if border * ((n-k)//2)<=y< border * ((n+k)//2) and border * ((n-k)//2)<=x< border * ((n+k)//2): return True
    return False

def solve(l, y, x):
    if l == 1:
        return 0
    border = l//n
    if inRange(y, x, border):
        return 1
    return solve(border, y%border, x%border)

length = n ** s
for y in range(r1, r2+1):
    for x in range(c1, c2+1):
        print(solve(length, y, x), end = "")
    print()