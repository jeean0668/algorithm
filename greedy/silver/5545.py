import sys

N = int(input())
dow, topping = map(int, sys.stdin.readline().split())
calories = []

dow_calory = int(input())
for i in range(N):
    top_carlory = int(input())
    calories.append(top_carlory)

calories.sort(reverse = True)
result = dow_calory/dow

for i in range(1, N):
    
    now = (dow_calory + sum(calories[:i]))/(dow + topping * i)
    result = max(result, now)

print(int(result))
