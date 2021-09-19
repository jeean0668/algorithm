import sys
import operator

N = int(input())
stores = dict()
for i in range(N):
    string = list(input())
    for i in range(len(string)):
        s = string[i]
        if s not in list(stores.keys()):
            stores[s] = -10 ** (len(string) - i - 1)
        else:
            stores[s] += -10 ** (len(string) - i - 1)

stores = sorted(stores.items(), key=operator.itemgetter(1))

init = 9
result = 0
for i in range(len(stores)):
    result += init * (-stores[i][1])
    init -= 1

print(result)