import sys, bisect
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

tmp = [array[0]]
idxes = []
for arr in array:
    if tmp[-1] < arr:
        tmp.append(arr)
        idxes.append(len(tmp))
    else:
        idx = bisect.bisect_left(tmp, arr)
        tmp[idx] = arr
        idxes.append(idx + 1)
print(n - max(idxes))