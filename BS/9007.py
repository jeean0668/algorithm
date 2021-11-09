import sys
input = sys.stdin.readline
"""[summary]
    1. 클래스를 두 반씩 나눠서 모든 합들을 구하여 각각 array로 저장한다.
    2. 이분 탐색으로 각 array들의 합 중 k와 가장 가까운 값을 구한다. 
"""
def solve(k, n , classes):
    # 2개 반에서 가능한 모든 합을 구해준다.
    array1 = []
    for i in range(n):
       for j in range(n):   
           array1.append(classes[0][i] + classes[1][j])
    array1.sort()
    array2 = []
    for i in range(n):
        for j in range(n):
            array2.append(classes[2][i] + classes[3][j])
    array2.sort()
    gap = sys.maxsize
    ans = sys.maxsize
    
    first, second= 0, len(array2) - 1 
    # array1은 작은 순서부터, array2 는 큰 순서부터 탐색한다. 
    while first < len(array1) and second >= 0:
        tmp = array1[first] + array2[second]
        if abs(k - tmp) < gap:
            ans = tmp
            gap = abs(k - tmp)
        elif abs(k - tmp) == gap:
            ans = min(ans, tmp)
        if tmp >= k : second -= 1
        else: first += 1
    print(ans)
cases = int(input())
while cases > 0:
    k, n = map(int, input().split())
    classes = [list(map(int, input().split())) for _ in range(4)]
    solve(k, n, classes)
    cases -= 1