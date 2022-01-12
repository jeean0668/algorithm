import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))

dic = dict()

def solve():
    cards.sort()
    for i in cards:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in range(m):
        if find[i] in dic:
            print(dic[find[i]], end = " ")
        else:
            print(0, end = ' ')

solve()