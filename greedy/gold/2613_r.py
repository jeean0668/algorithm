import sys
from itertools import accumulate

input = sys.stdin.readline

def maxMarbleSum(val):
    cnt, _sum = 1, 0
    for i in range(n):
        if marble[i] > val:
            return False
        if _sum + marble[i] <= val:
            _sum += marble[i]
        else:
            cnt += 1
            _sum = marble[i]
    return cnt <= m

if __name__ == "__main__":
    n, m = map(int,input().split())
    marble = list(map(int, input().split()))
    left = 1
    right = n * 100
    while left <= right:
        mid = (left + right)//2
        if maxMarbleSum(mid):
            right = mid - 1
        else:
            left = mid + 1
    print(left)
    
    cnt, _sum, group = 0, 0, 1
    ans = []
    for i in range(n):
        _sum += marble[i]
        if _sum > left:
            ans.append(cnt)
            _sum = marble[i]
            cnt = 0
            group+=1
        cnt += 1
    ans.append(cnt)
    pos = len(ans) - 1
    while group < m:
        if ans[pos] == 1:
            pos-=1
        else:
            ans[pos] -=1
            ans.append(1)
            group+=1
    print(*ans, sep = " ")
    
        
        
        
        
        
        
        
        