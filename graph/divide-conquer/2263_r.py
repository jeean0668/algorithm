"""
1. 주어진 inorder와 postorder를 가지고 트리를 만든다
2. 트리에서 preorder를 출력한다.
https://donggoolosori.github.io/2020/10/15/boj-2263/ 참조

"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)
def getInput():
    global n, in_order, post_order, idx
    n = int(input())
    in_order = list(map(int, input().split()))
    post_order = list(map(int, input().split()))
    idx = [-1] * (n+1)
    for i in range(n):
        idx[in_order[i]] = i
def preOrder(inStart, inEnd, postStart, postEnd):
    global n, in_order, post_order, idx
    if inStart > inEnd or postStart > postEnd:
        return 
    root = post_order[postEnd]
    print(root, end = " ")
    preOrder(inStart, idx[root] - 1, postStart, postStart + (idx[root] - inStart) - 1)
    preOrder(idx[root] + 1, inEnd, postStart + (idx[root] - inStart), postEnd - 1)


def solve():
    global n, post_order
    # 주어진 두 순서를 가지고 트리를 생성한다.
    preOrder(0, n-1, 0, n-1)
    

if __name__ == "__main__":
    getInput()
    solve()