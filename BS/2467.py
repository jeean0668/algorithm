import sys
input = sys.stdin.readline

n = int(input())
liquids = list(map(int, input().split()))
liquids.sort()

# 기존과는 다르게 인덱스를 기준으로 한다. 
left, right = 0, n-1
save = [liquids[left], liquids[right]]
max_liquid = abs(liquids[left] + liquids[right])
ans = 0
while left < right:
    temp = liquids[left] + liquids[right]
    if abs(temp) < max_liquid:
        max_liquid = abs(temp)
        save = [liquids[left], liquids[right]]
    if temp < 0:
        left += 1
    else:
        right -= 1
print(*save)