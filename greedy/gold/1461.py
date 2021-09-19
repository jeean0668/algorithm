import sys

N, M = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

plus = []
minus = []

for l in array:
    if l > 0:
        plus.append(l)
    else:
        minus.append(-l)

plus.sort()
minus.sort()
L1 = len(plus)
L2 = len(minus)

k = 0
temp = 0
while (L1 - k) % M != 0:
    temp = plus[k]
    k += 1

plus_result = temp * 2

while k != L1:
    plus_result += plus[k+M-1] * 2
    k += M


k = 0
temp = 0
while(L2 - k) % M != 0:
    temp = minus[k]
    k += 1

minus_result = temp * 2
while k != L2:
    minus_result += minus[k+M-1] * 2
    k += M

deepest = 0
if len(minus) == 0:
    deepest = max(plus)
    print(plus_result - deepest)
elif len(plus) == 0:
    deepest = max(minus)
    print(minus_result - deepest)
else:
    deepest = max([max(plus), max(minus)])
    print(plus_result + minus_result - deepest)
    


