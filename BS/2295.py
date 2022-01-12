import sys
input = sys.stdin.readline
"""
A[x] + A[y] + A[z] = A[k] -> A[x] + A[y] = A[k] - A[z]로 변형
A[x] + A[y] 값을 저장한 array를 만든다.
이분 탐색으로 A[x] + A[y] 를 만족하는 A[k], A[z]가 있는지 탐색한다.

"""
n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
sum = []
for i in range(n):
    for j in range(i, n):
        sum.append(arr[i] + arr[j])
sum.sort()
def BS(x):
    left, right = 0, len(sum) - 1
    while left < right:
        mid = (left + right) // 2
        if x == sum[mid]:
            return True
        if x > sum[mid]:
            left = mid + 1
        else:
            right = mid - 1
         
result = 0
for i in range(n):
    for j in range(i+1, n):
        if BS(arr[j] - arr[i]):
            result = max(result, arr[j])

print(result)