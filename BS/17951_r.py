import sys
input = sys.stdin.readline

n, k = map(int, input().split())
papers = list(map(int, input().split()))

"""
def search(cases, num, start ):
    if num == 1:
        return sum(papers[start:])
    cnt, result,c  = 0, 0, 0
    for i in range(start, start + cases):
        cnt += papers[i]
        c += 1
        r = search(cases - c, num-1, i+1)
        result = max(result , min(cnt, search(cases - c, num-1, i+1)))
    return result
"""
#print(search(n, k, 0))


"""
오랜만에 index 기준이 아니라 score 기준으로 이분탐색하는 문제이다.
최댓값을 right로 설정하고 이분탐색을 진행하면 되는 문제 
"""
def BS():
    left, right = 0, 0
    for i in range(n):
        right += papers[i]
    while left <= right:
        cnt, sum, mid = 0, 0, (left + right) // 2
        for i in range(n):
            sum += papers[i]
            if sum >= mid:
                sum = 0
                cnt += 1
        if cnt >= k:
            left = mid + 1
        else:
            right = mid - 1
    print(left - 1)
BS()