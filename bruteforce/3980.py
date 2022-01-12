import sys
input = sys.stdin.readline
test_cases = int(input())

while test_cases > 0:
    positions = [list(map(int, input().split())) for _ in range(11)]
    selected = [False for _ in range(11)]

    ans = 0
    def dfs(row, cnt):
        global ans
        if row == 11:
            ans = max(ans, cnt)
            return
        for i in range(11):
            if selected[i] : continue
            if not positions[row][i] : continue
            selected[i] = True
            dfs(row + 1, cnt + positions[row][i])
            selected[i] = False
        
    dfs(0, 0)
    print(ans)
    test_cases -= 1