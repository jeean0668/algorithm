import sys

input = sys.stdin.readline
N, w = map(int,input().split())
arr3, arr5 = [], []
for i in range(N):
    t, s = map(int, input().split())
    if t == 3:
        arr3.append([t,s])
    elif t == 5:
        arr5.append([t,s])
        
arr3.sort(reverse = True)
arr5.sort(reverse = True)

part_arr3 = [0] # 3을 선택하지 않았을때를 고려하여 0을 초기값으로 설정
part_arr5 = [0]

for i in range(len(arr3)):
    part_arr3.append(part_arr3[i] + arr3[i][1])
    
for i in range(len(arr5)):
    part_arr5.append(part_arr5[i] + arr5[i][1])
    
arr3_num = min(int(w/3), len(arr3))
max_val = 0

while arr3_num >= 0:
    arr5_num = min(int((w-arr3_num*3)/5), len(arr5))
    max_val = max(max_val, part_arr3[arr3_num] + part_arr5[arr5_num])
    arr3_num -= 1
print(max_val)