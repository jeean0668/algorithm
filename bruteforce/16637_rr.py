import sys

n = int(input())
express = input()
nums, opts = [], []
for ex in express:
    if ex.isdigit() : nums.append(ex)
    else: opts.append(ex)

ans = -sys.maxsize
def dfs(idx, score):
    global ans
    if idx == len(opts):
        ans = max(ans, int(score))
        return
    first = str(eval(score + opts[idx] + nums[idx + 1]))
    dfs(idx + 1, first)
    if idx + 1 < len(opts):
        second = str(eval(nums[idx + 1] + opts[idx + 1] + nums[idx + 2]))
        second = str(eval(score + opts[idx] + second))
        dfs(idx + 2, second)
dfs(0, nums[0])
print(ans)

        
    