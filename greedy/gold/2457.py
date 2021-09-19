import sys

N = int(input())
array = []
for i in range(N):
    start_m, start_d, end_m, end_d = map(int, sys.stdin.readline().split())
    array.append([start_m * 100 + start_d, end_m * 100 + end_d])
array.sort(key = lambda x : (x[0], -x[1]))

date = 301
idx = 0
result, maxdate = 0, 0

while date <= 1130:
    for i in range(idx, N):
        if array[i][0] > date:
            break
        if array[i][1] > maxdate:
            maxdate = array[i][1]
            idx = i
            
    if maxdate == date:
        print(0)
        sys.exit()
    else:
        date = maxdate
        result +=1
print(result)
    