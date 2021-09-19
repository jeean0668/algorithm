import sys
from collections import deque

input = sys.stdin.readline
l = int(input())
Ml, Mk = map(int, input().split())
c = int(input())

que = []
for _ in range(l):
    que.append(int(input()))
    
part_s = Mk
flag = True
end = 0
bomb = Ml - 1
for now in range(len(que)):
    damage = Mk * Ml - bomb * Mk
    if damage < que[end]:
        
        bomb = 0
print('YES') if flag else print('NO')