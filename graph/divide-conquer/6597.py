import sys
input = sys.stdin.readline

# preorder와 inorder로 postorder 출력하기 


def postorder(start, end, r_idx):
    for i in range(start, end):
        if inorder[i] == preorder[r_idx]:
            postorder(start, i, r_idx+1)
            postorder(i+1, end, r_idx + i - start + 1)
            print(preorder[r_idx], end = "")

for line in sys.stdin.readlines():
    preorder, inorder = line.strip().split()
    n = len(preorder)
    postorder(0, n, 0)
    print()