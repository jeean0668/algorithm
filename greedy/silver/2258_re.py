import sys

def solve():
    N, M = map(int, sys.stdin.readline().split())
    ans = []
    w = 0
    for _ in range(N):
        a, b = map(int, sys.stdin.readline().split())
        ans.append([b, a]) 
    ans = sorted(ans, key = lambda x : (x[0], -x[1]))
    
    result = sys.maxsize
    weight = 0
    same = 0
    
    print(result)
    
    for i in range(N):
        weight += ans[i][1]
        
        # 앞에 선택한 것과 가격이 같을 경우
        if i >= 1 and ans[i][0] == ans[i-1][0]:
            # 지금 선택된 가격을 same에 더해준다. 
            same += ans[i][0]
        else:
            same = 0 
        if weight >= M:
            result = min(result, ans[i][0] + same)
            flag = True
    print(result if flag else -1)
    
if __name__ == "__main__":
    solve()