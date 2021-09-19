import sys

N = int(input())
array = list(map(int, sys.stdin.readline().split()))
array.sort(reverse = True)

max_value = array[0]
result = 0
result += max_value * (N-1)
for index in range(1, len(array)):
    l = array[index]
    result += l

print(result)