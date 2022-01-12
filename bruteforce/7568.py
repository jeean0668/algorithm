import sys
input = sys.stdin.readline

n = int(input())
man = [list(map(int, input().split())) for _ in range(n)]

result = []
for i in range(len(man)):
    w = 1
    for j in range(len(man)):
        if i == j:
            continue
        if man[i][0] < man[j][0] and man[i][1] < man[j][1]:
            w += 1
    result.append(w)
    
print(*result)