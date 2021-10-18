
import sys
import math
input = sys.stdin.readline


"""
라인스위핑 문제인데, 파이썬으로 구현하기가 어렵다. 
"""

def getInput(num):
    global points
    points = []
    for _ in range(num):
        x, y = map(int, input().split())
        points.append([x, y])
    points.sort(key=lambda x : x[0])

def calDistance(first, second):
    fx, fy, sx, sy = first[0], first[1], second[0], second[1]
    return (fx - sx) ** 2 + (fy - sy) ** 2
def makeCandidate(arr, bound, min):
    temp = []
    x = arr[bound][0]
    y = arr[bound][1]

    for i in range(bound - 1, -1, -1):
        if abs(x - arr[i][0]) < min:
            if abs(y - arr[i][1]) < min:
                temp.append(arr[i])
        else:
            return temp
    return temp
def lower_bound(target, limit):
    left, right = 0, len(target)
    while left < right:
        mid = left + (right - left) // 2
        if target[mid][0] > limit[0] and target[mid][1] > limit[1]:
            left = mid + 1
        else:
            right = mid
    return right

def upper_bound(target, limit):
    left, right = 0, len(target)
    while left < right:
        mid = left + (right - left) // 2
        if target[mid][0] < limit[0] and target[mid][1] < limit[1]:
            left = mid + 1
        else : 
            right = mid
    return right
    
def solve():
    global n
    
    ans = calDistance(points[0], points[1])
    candidates = [points[0], points[1]]
    start = 0
    result = sys.maxsize
    for i in range(2, n):
        now = points[i]
        while start < i:
            cmp = points[start]
            x_dist = now[0] - cmp[0]
            if x_dist ** 2 > ans:
                candidates.remove(cmp)
                start += 1
            else:
                break

        d = int(math.sqrt(ans)) + 1
        lower_point = [-100000, now[1] - d]
        upper_point = [10000, now[1] + d]
        # lower_point와 upper_point가 결정하는 bound(네모 모양 상자) 안에 들어 가는 candidates 들만 본다.
        lower = lower_bound(candidates, lower_point)
        upper = upper_bound(candidates, upper_point)
        
if __name__ == "__main__":
    global n
    n = int(input())
    getInput(n)
    solve()
