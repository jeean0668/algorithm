import sys
from collections import deque

N=int(input())
L=list(map(int,input().split()))
money=int(input())

minCost=min(L)
minNum=L.index(minCost)
if N==1:
    print(0)
    sys.exit()

#digit 자리수 검사해야함
def add(remainMoney,digit):
    #print(remainCost,pick)
    #가장 큰 오른쪽 숫자부터 가장 큰거 넣어보기
    for i in range(digit,-1,-1):
        if pick[i]!=N-1:
            #큰거부터 넣어봄
            for j in range(N-1,pick[i],-1):
                nowCost=L[j]-L[pick[i]]
                if nowCost<=remainMoney:
                    pick[i]=j # i번째 digit에 j를 넣는다. ->(10**i) * j
                    add(remainMoney-nowCost,digit-1)
                    return
    #모두다 0이면
    if not any(pick):
        if not pick:
            print(0)
            sys.exit()
        pick.pop()
        add(remainMoney+L[0],digit-1)

num=money//minCost
pick=[minNum for i in range(num)] # dynamic programming을 위한 배열
# if len(pick) == 4 => 최대 네자릿수까지 만들 수 있음 
cost=num*minCost
add(money-cost,num-1)
ans=0
for i in range(len(pick)):
    ans+=(10**i)*pick[i]
print(ans)










def add2(remainMoney, digit):
    for i in range