import sys
input = sys.stdin.readline

"""
cal, cal2를 어떻게 구현할 것인지가 관건인 문제였다. 
자릿수가 몇개 안되기 때문에 직접 구현해주면 되는 문제였다. 
"""
def cal(A):
    digit = [100 * 2, 100 * 2 + 9900 * 3, 100 * 2 + 9900 * 3 + 990000*5]
    if A <= digit[0]:
        return A // 2
    if A <= digit[1]:
        return 100 + (A - digit[0]) // 3
    if A <= digit[2]:
        return 10000 + (A - digit[1]) // 5

    return 1000000 + (A - digit[2]) // 7

def cal2(x):
    digits = [100, 10000, 1000000]

    if x < digits[0]:
        return x * 2
    if x < digits[1]:
        return 100 * 2 + (x - 100) * 3
    if x < digits[2]:
        return 100 * 2 + 9900 * 3 + (x - 10000) * 5
    return 100 * 2 + 9900 * 3 + 990000 * 5 + (x - 1000000) * 7
def search(left, right, t, usage):

    while True:
        mid = (left + right) // 2
        ans1 = cal2(mid)
        ans2 = cal2(usage - mid)
        diff = ans2 - ans1
        if diff == B:
            return ans1
        if diff > B:
            left = mid + 1
        else:
            right = mid - 1
while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    usage = cal(A)
    left, right = 1, usage
    print(search(left, right, B, usage))
