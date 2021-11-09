import sys
input = sys.stdin.readline

n = int(input())
liquids = list(map(int, input().split()))
liquids.sort()

save = []
result = float('inf')
for i in range(n-2):
    if i > 0 and liquids[i] == liquids[i-1]:
        continue
    left, right = i+1, n-1
    while left < right:
        mid = liquids[i] + liquids[left] + liquids[right]
        if abs(mid) < abs(result):
            save = [liquids[i], liquids[left], liquids[right]]
            result = mid
        if mid < 0: left += 1
        elif mid > 0: right -= 1
        else:
            print(*save)
            sys.exit(0)
print(*save)