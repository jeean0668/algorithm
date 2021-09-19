import sys

N = int(input())

array = []
for i in range(N):
    T, S = map(int, sys.stdin.readline().split())
    array.append([S, T])
    
array.sort(reverse = True) # 끝나는 시간 기준 내림차순 정렬)

cur = sys.maxsize

for arr in array:
    cur = min([cur, arr[0]])
    cur -= arr[1]

if cur < 0 :
    print(-1)
else:
    print(cur)