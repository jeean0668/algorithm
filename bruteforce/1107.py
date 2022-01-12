import sys
input = sys.stdin.readline

n, m = int(input()), int(input())
answer = abs(100 - n)
if m:
    broken = set(input().split())
else:
    broken = set()

def possible(value):
    for n in value:
        if n in broken:
            return False
    return True

for i in range(1000001):
    if possible(str(i)):
        answer = min(answer, abs(i - n) + len(str(i)))
    
print(answer)