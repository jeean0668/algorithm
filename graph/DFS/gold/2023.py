import sys

input = sys.stdin.readline

n = int(input()) # 자릿수
init = [2,3,5,7]

second = [1,3,7,9]
def check(num):
    # 소수인지 아닌지 판별한다. root(N)의 시간복잡도
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

def dfs(num, depth):
    if depth >= n:
        print(num)
        return num
    
    # 재귀함수로 다음 수 호출
  
    for s in second:
        next_num = num * 10 + s 
       
        if check(next_num):
            dfs(next_num, depth + 1)
   
for t in init:
    if check(t):
        dfs(t, 1)
