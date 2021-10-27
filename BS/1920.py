import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)

n = int(input())
array = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))

array.sort()

# 1. array를 sort한다.
# 2. find에 있는 원소 하나하나씩 array에 있는지 확인한다.

def search(left, right, e):
    if left >= right:
        return 0
    elif array[left] == e:
        return 1
    elif array[right] == e:
        return 1
    mid = (left + right) // 2
    if e <= array[mid]:
        return search(left, mid, e)
    elif e > array[mid]:
        return search(mid + 1, right, e)

def solve():
    array.sort()
    for f in find:
        print(search(0, n-1, f))

solve()