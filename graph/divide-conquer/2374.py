import sys
input = sys.stdin.readline

    

def findGroup(idx, target):
    global n, array
    lower_bound = 0
    upper_bound = n
    for i in range(idx - 1, -1, -1):
        if array[i] != target:
            lower_bound = i + 1
            break
    for i in range(idx + 1, n):
        if array[i] != target:
            upper_bound = i
            break
    return (lower_bound, upper_bound)
    
def fixedarray(lower_bound, upper_bound):
    global minNum, array, n, cnt
    goal = float("inf")

    if lower_bound != 0:
        goal = array[lower_bound-1]
    elif upper_bound != n and array[upper_bound] < goal:
        goal = array[upper_bound]

    for i in range(lower_bound, upper_bound):
        array[i] = goal
    
    cnt += (goal - minNum)
def solve():

    global cnt, array, minNum, array
    # array에서 가장 작은수의 위치
    cnt = 0
    minNum = min(array)
    maxNum = max(array)

    while minNum < maxNum:
        index = array.index(minNum)

    # array[index]와 같은 크기의 수를 가진 것들의 갯수를 구한다.
        lower_bound, upper_bound = findGroup(index, minNum)
    
    # 두 bound들 중 작은수를 찾고, array[index]와 bound 사이의 차를 더해 array 갱신

        fixedarray(lower_bound, upper_bound)
        minNum = min(array)
    
    print(cnt)

if __name__ == "__main__":
    global n, array
    n = int(input().strip())
    array = [0] * n 
    for i in range(n):
        array[i] = int(input())
    solve()
    



    

