import sys
input = sys.stdin.readline

S, N, K, R_1, R_2, C_1, C_2 = map(int, input().split())

def solve(length, y, x):
    # length: 사분면 한변의 길이
    # border : 사분면의 중앙에 있는 k*k 정사각형 한변의 길이
    if length == 1: return 0
    border = length//N
    if border*((N-K)//2)<=y<border*((N+K)//2) and border*((N-K)//2)<=x<border*((N+K)//2):
        return 1
    return solve(border, y%border, x%border)
    # 한 변의 길이가 l 인 평면의 가운데 k*k에 속해있을 경우-> 검정석
    # border = l/n 이라고 했을때, y, x가 (border * (n-k)/2, border*(n-k)/2 + k)에 있으면 가능

length = 1
while S > 0: 
    length *= N
    S -= 1
length *= N
for y in range(R_1, R_2+1):
    for x in range(C_1, C_2+1): print(solve(length, y, x), end = "")
    print()
    

        