import sys

n = int(input())
nums = list(map(int, input().split()))

if n == 1:
    print('A')
    sys.exit()
if n == 2:
    if nums[0] == nums[1] :
        print(nums[0])
    else:
        print('A')
    sys.exit()
if nums[1] != nums[0]:
    a = (nums[2] - nums[1]) // (nums[1] - nums[0])
else:
    a = 0
b = nums[1] - nums[0] * a

flag = True
for i in range(1, n):
    if nums[i] != nums[i-1] * a + b:
        print('B')
        flag = False
        break
if flag:
    print(nums[n-1] * a + b)