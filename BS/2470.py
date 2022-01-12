import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
l.sort()
left, right = 0, n-1
save = [l[left], l[right]]
max_l = abs(l[0] + l[-1]) 

while left < right:
    temp_l = l[left] + l[right]
    if abs(temp_l) < max_l:
        max_l = abs(temp_l)
        save = [l[left], l[right]]
    if temp_l < 0:
        left += 1
    else:
        right -= 1
print(*save)