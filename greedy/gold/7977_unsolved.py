import sys

input = sys.stdin.readline
N = int(input())
dna = list(input().strip())
ans = []
for v in dna:
    if v not in ans:
        ans.append(v)
ans.reverse()
length = 0
if len(ans) < 4:
    length = 0
else:
    if len(dna) % 4 == 0:
        length = len(dna)//4
    else:
        length = len(dna)//4 + 1
        
result = ''
for i in range(len(dna)):
    result += ans[i%4]

print(length)
print(result)