import sys
input = sys.stdin.readline
n = int(input())
budgets = list(map(int, input().split()))
total = int(input())

left, right = 0, max(budgets)

while left <= right:
    mid = (left + right) // 2
    temp = 0
    for budget in budgets:
        temp += min(budget, mid)
    if temp <= total:
        left = mid + 1
    else:
        right = mid - 1
print(right)