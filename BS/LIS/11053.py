import sys, bisect
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
tmp = [array[0]]
idxes = []
for a in array:
    if tmp[-1] < a:
        tmp.append(a)
        idxes.append(len(tmp))
    else:
        idx = bisect.bisect_left(tmp, a)
        tmp[idx] = a
        idxes.append(idx + 1)

m = len(tmp)
ans = []
i = n - 1
while m > 0:
    if m == idxes[i]:
        ans.append(i)
        m -= 1
    i -= 1
print(len(tmp))
print(*sorted([array[x] for x in ans]))