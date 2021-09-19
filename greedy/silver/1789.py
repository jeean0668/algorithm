# silver 5

import math

S = int(input())


def solution(S):
    n = 1
    while n*(n+1)/2 <= S:
        n += 1
    return n-1
    
print(int(solution(S)))