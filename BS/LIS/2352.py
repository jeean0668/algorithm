import sys, bisect
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

array = [nums[0]]
tmp = []
for num in nums:
    if array[-1] < num:
        array.append(num)
        tmp.append(len(array))
    else:
        idx = bisect.bisect_left(array, num)
        array[idx] = num
        tmp.append(idx + 1)
print(len(array))