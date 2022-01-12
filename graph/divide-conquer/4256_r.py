import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)

tests = int(input())

while tests > 0:
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    # 1. 전위순회로 루트를 구한다.
    # 2. 구한 루트를 기반으로 중위순회를 통해 왼쪽, 오른쪽 탐색 진행
    # 3, 부모를 출력
    def post_order(s, e, r_idx):
        for i in range(s, e):
            if inorder[i] == preorder[r_idx]:
                # 왼쪽 서브트리 탐색
                post_order(s, i, r_idx + 1)
                # 오른쪽 서브트리 탐색
                # i - s 는 왼쪽 서브트리 크기 만큼 건너뛰어야 오른쪽 서브트리만 남기 때문이다.
                post_order(i+1, e, r_idx + 1 + i - s)
                print(preorder[r_idx], end = ' ')
    post_order(0, n, 0)
    print() 
    tests-=1
    
    
    
