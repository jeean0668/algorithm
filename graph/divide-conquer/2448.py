"""
c++ 해설처럼 박스를 나눠서 할수 없는 문제다. 왜냐하면 python의 print와
c++의 printf는 구동방식이 다르기 때문이다.(python은 다음 출력이 무조건 다음줄에 나오지만, c++은 그렇지 않다는 점)
그래서 결과들을 저장해놓고 나중에 한번에 출력해야한다. 
"""



import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)

n = int(input())
ans = [[' '] * 2 * n for _ in range(n)]

def drawing(y, x, n):
    if n == 3:
        ans[y][x] = '*'
        ans[y+1][x-1] = ans[y+1][x+1] = '*'
        for i in range(-2, 3):
            ans[y+2][x+i] = '*'
    else:
        next_n = n//2
        drawing(y, x, next_n)
        drawing(y + next_n, x - next_n, next_n)
        drawing(y + next_n, x + next_n, next_n) 

drawing(0,n-1, n)
for row in ans:
    print("".join(row))

