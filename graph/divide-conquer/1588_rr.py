import sys
input = sys.stdin.readline

first = int(input())
left = int(input())
right = int(input())
n = int(input())

def solve(seed, time, start, end):
    if end < left or right < start:
        return [0, 0, 0]
    if left <= start and end <= right:
        answer = [0,0,0]
        answer[seed-1] = 1
        for i in range(time):
            temp = answer[:]
            answer[0] = temp[0] + temp[1]*2
            answer[1] = temp[0] + temp[1] + temp[2] * 2
            answer[2] = temp[0] + temp[2]
        return answer

    answer = [0,0,0]
    changed = ((1,3,2),(2,2,1),(2,3,2))
    t = (end - start + 1)//3
    for i in range(3):
        part = solve(changed[seed-1][i], time - 1, start + t * i, start + t * (i+1) - 1)
        for j in range(len(part)):
            answer[j] += part[j]
    return answer
    
print(*solve(first, n, 0, 3**n-1))



