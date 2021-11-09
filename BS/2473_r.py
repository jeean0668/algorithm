import sys
input = sys.stdin.readline

"""
arr의 원소중 한 원소를 지정하고, 그 원소의 index + 1 ~ right 까지
탐색하여 남은 두 원소를 탐색
한 원소 + 이분탐색으로 찾아낸 두 원소의 합이 0보다 작으면 left ++ 아니면 right -- 해준다. 
"""
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
left, right = 0, n-1
save = []
gap = float('inf')
for i in range(n-2):
    if i > 0 and arr[i] == arr[i-1]:
        continue
    left, right = i+1, n - 1
    while left < right:
        temp = arr[i] + arr[left] + arr[right]
        if abs(temp) < abs(gap):
            save = [arr[i], arr[left], arr[right]]
            gap = temp
        if temp < 0:
            left += 1
        elif temp > 0:
            right -= 1
        else:
            print(*save)
            sys.exit(0)
    
print(*save)
