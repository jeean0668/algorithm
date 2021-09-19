import sys
input = sys.stdin.readline

N, K, S = map(int, input().split())

A = []
B = []
for i in range(N):
    p, m = map(int, input().split())
    if p > S:
        B.append([p, m])
    elif p < S:
        A.append([p, m])
A.sort()
B.sort(reverse = True)
print(A, B)

i, temp = 0, 0
result1 = 0
max_d = 0
trail = 0
if len(A) > 0:
    while i < len(A):
        if trail > 0:
            #print(A[i], trail)
            max_d = max(max_d, S-A[i][0])
        if trail > A[i][1]:
            trail -= A[i][1]
            A[i][1] = 0
            i += 1
        elif trail < A[i][1]:
            A[i][1] -= trail
            trail = 0
        else:
            A[i][1] = 0
            trail = 0
            i += 1
        if trail == 0 or i >= N:
            result1 += 2 * max_d
            max_d = 0
            trail = K
i = 0
result2 = 0
max_d = 0
trail = 0 # 
if len(B) > 0:
    while i < len(B):
        if trail > 0:
            max_d = max(max_d, B[i][0]-S)
    
        if trail > B[i][1]:
            trail -= B[i][1]
            B[i][1] = 0
            i += 1
        elif trail < B[i][1]:
            B[i][1] -= trail
            trail = 0
        else:
            B[i][1] = 0
            trail = 0
            i += 1
        if trail == 0 or i >= N:
            result2 += 2 * max_d
            max_d = 0
            trail = K
print(result1, result2)
print(result1 + result2)