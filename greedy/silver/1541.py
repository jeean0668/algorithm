import sys

string = list(input())

N = len(string)
digit = 0
final = 0
result = 0
for i in range(N-1, -1, -1):
    s = string[i]
    if s == "+":
        digit = 0
        continue
    elif s == "-":
        digit = 0
        final = final - result
        result = 0
        # somthing
    else:
        result += int(s) * (10**digit)
        digit += 1
        
final = final + result
print(final)
