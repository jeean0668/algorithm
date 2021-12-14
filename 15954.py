import sys
import math
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(float, input().split()))

def cal(s, e):
    result = 0
    mean = float(sum(arr[s : e]) / (e - s))
    for i in range(s, e): result += (arr[i] - mean) * (arr[i] - mean)
    return result / (e - s)
answer = sys.maxsize
for i in range(0, n-k+1): 
    for j in range(n-k-i+1):
        answer = min(answer, cal(i, i+k+j))
print(math.sqrt(answer))