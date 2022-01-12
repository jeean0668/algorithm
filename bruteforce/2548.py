import sys

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

ans = nums[0]
maximum = sys.maxsize
for i in range(n):
    cnt = 0
    for j in range(n):
        cnt += abs(nums[j] - nums[i])
    if cnt < maximum:
        maximum = cnt
        ans = nums[i]
print(ans)