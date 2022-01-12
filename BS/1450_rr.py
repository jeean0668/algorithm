
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
w = list(map(int, input().split()))

A_result, B_result = [], []
A = w[:n//2]
B = w[n//2:]

def brute_force(index, w, things, size, result):
    if index >= size:
        result.append(w)
        return
    brute_force(index + 1, w, things, size, result)
    brute_force(index + 1, w+things[index], things, size, result)
    
brute_force(0, 0, A, len(A), A_result)
brute_force(0, 0, B, len(B), B_result)
B_result.sort()

def search(value):
    left, right = 0, len(B_result)
    while left < right:
        mid = (left + right) // 2
        if B_result[mid] <= value:
            left = mid + 1
        else:
            right = mid
    return right
    
cnt = 0
for a in A_result:
    if c - a < 0:
        continue
    cnt += search(c-a)
print(cnt)
    

