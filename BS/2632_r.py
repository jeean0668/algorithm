import sys
from collections import defaultdict
input = sys.stdin.readline

Pizza = int(input())
m, n = map(int, input().split())
A = [int(input()) for _ in range(m)]
B = [int(input()) for _ in range(n)]

"""
A[0]에서 연속 2개 뽑았을때, 3개 뽑았을때 합.... m개 뽑았을때 합의 경우의 수를 모두 구한다.
--> 모든 연속합의 경우의 수를 구한다. 

"""
A_dict = defaultdict(int)
B_dict = defaultdict(int)
A_dict[0], B_dict[0] = 1, 1
def choose(dict, arr):
    for i in range(len(arr)):
        s = 0
        for j in range(len(arr)):
    
            s += arr[(i + j) % len(arr)]
            if s > Pizza : break
            dict[s] += 1

choose(A_dict, A)
choose(B_dict, B)
A_dict[sum(A)] = B_dict[sum(B)] = 1

ans = 0
for i in range(Pizza + 1):
    ans += (A_dict[i] * B_dict[Pizza - i])
print(ans)