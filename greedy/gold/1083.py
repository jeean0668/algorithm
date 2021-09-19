import sys

N = int(input())
array = list(map(int, sys.stdin.readline().split()))
S = int(input())


for i in range(N):
    maximum = array[i]
    maximum_index = i
    for j in range(i+1, N):
        if S - j + i >= 0:
            if array[j] > maximum:
                maximum = array[j]
                maximum_index = j
    for j in range(maximum_index, i, -1):
        array[j], array[j-1] = array[j-1], array[j]
    S -= (maximum_index-i)
    if S <= 0:
        break
result = ""
for ar in array:
    result += str(ar)
    result += " "
    
print(result)