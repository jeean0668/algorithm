import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

ans = 0

def search(target, i):
    left, right = 0, n-1
    ret = False
    while left < right:
        mid = arr[left] + arr[right]
        if mid == target:
            if arr[left] == 0 and right == i:
                right -= 1
            elif arr[right] == 0 and left == i:
                left += 1
            else:
                return True
        elif mid > target:
            right -= 1
        elif mid < target:
            left += 1
    return ret

for i in range(n):
    if search(arr[i], i):
        ans += 1
print(ans)