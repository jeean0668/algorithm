import sys
import operator

N = int(input())
stores = dict()
for i in range(N):
    string = list(input())
    for j in range(len(string)):
        s = string[j]
        if s not in list(stores.keys()):
            stores[s] = -10 ** (len(string) - j - 1)
        else:
            stores[s] += -10 ** (len(string) - j - 1)

stores = sorted(stores.items(), key=operator.itemgetter(1))

init = 9
result = 0
for i in range(len(stores)):
    result += init * (-stores[i][1])
    init -= 1
print(stores)
print(result)