import sys

N = int(input())
minus = []
plus = []
zero = []
for i in range(N):
    a = int(input())
    if a <= 0:
        minus.append(a)
    elif a > 0:
        plus.append(a)
    #else:
    #    zero.append(a)
        
# 1. minus부터
minus.sort()
plus.sort(reverse = True)

result = 0
for i in range(0, len(minus), 2):
    
    if i == len(minus) - 1:
        result += minus[i]
    else:
        result += (minus[i] * minus[i+1])
    
for i in range(0, len(plus), 2):
    if i == len(plus) - 1:
        result += plus[i]
    else:
        if plus[i] + plus[i+1] > plus[i] * plus[i+1]:
            result += plus[i] + plus[i+1]
        else:
            result += (plus[i] * plus[i+1])
        
print(result)