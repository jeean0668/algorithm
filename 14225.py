import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

sum_combinations = set()
for e in arr:
    sum_combinations.add(e)

def preprocess(index, value, cnt):
    global sum_combinations
    if index == n:
        if cnt == 0: return
        sum_combinations.add(value)
        return
    preprocess(index + 1, value, cnt)
    preprocess(index + 1, value + arr[index], cnt + 1)

preprocess(0, 0, 0)

for i in range(1, sum(arr) + 2):
    if i not in sum_combinations:
        print(i)
        break
