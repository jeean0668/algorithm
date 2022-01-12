import sys

n = int(input())
s = [0] * 8
w = [0] * 8
for i in range(n): s[i], w[i] = map(int, input().split())

answer = 0
def func(index):
    
    global answer
    if index == n:
        cnt = 0
        for i in range(n):
            if s[i] <= 0:
                cnt += 1
        
        answer = max(answer, cnt)
        return
    if s[index] <= 0:
        func(index + 1)
    else:
        flag = False
        for i in range(n):
            if i != index and s[i] > 0:
                s[i] -= w[index]
                s[index] -= w[i]
                flag = True
                func(index + 1)
                s[index] += w[i]
                s[i] += w[index]
        if not flag:
            func(n)
func(0)
print(answer)
            
    
