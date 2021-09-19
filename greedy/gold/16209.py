import sys
import heapq

array = []
queue = []

input = sys.stdin.readline

N = int(input())
temp = list(map(int, input().split()))

# 음수, 0, 양수로 나눈다.
minus = []
plus = []
zero = []

for t in temp:
    if t < 0:
        minus.append(t)
    elif t > 0:
        plus.append(t)
    else:
        zero.append(t)
# minus는 오름차순 정렬
minus.sort()
plus.sort(reverse = True)

mm, pp = [], []
for i in range(len(plus)):
    if i & 1:
        pp.append(plus[i])
    else:
        pp.insert(0, plus[i])

for i in range(len(minus)):
    if i & 1:
        mm.append(minus[i])
    else:
        mm.insert(0, minus[i])
        
if len(pp) and pp[0] > pp[len(pp)-1] :
    pp.reverse()
if len(mm) and mm[0] > mm[len(mm)-1] :
    mm.reverse()
    

print(*(mm + zero + pp))
    
# 왜 틀렸는지 모르겠는 문제. 