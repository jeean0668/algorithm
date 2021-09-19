import sys

L, N, r_f, r_b = map(int, sys.stdin.readline().split())

array = []
for i in range(N):
    array.append(list(map(int, sys.stdin.readline().split())))
array.sort(key = lambda x : -x[1])
                 
current = 0
result = 0
for l in array:
    
    if current < l[0]: 
        result += (l[0]- current) * (r_f - r_b) * (l[1])
        current = l[0]
print(result)