import sys

init = list(input())
finish = list(input())
queue = []
length1 = len(init)

while length1 != len(finish):
    now = finish[len(finish) - 1]
    if now == 'A':
        finish.pop()
    elif now == 'B':
        finish.pop()
        while len(finish) != 0:
            queue.append(finish.pop()) #queue에 stack 원소 전부 넣음
        while len(queue) != 0:
            finish.append(queue.pop(0)) #stack에 queue 원소 전부 넣음 -> reverse됨 

a = True
for i in range(length1):
    if finish[i] != init[i]:
        a = False
        break
        
if a:
    print(1)
else:
    print(0)