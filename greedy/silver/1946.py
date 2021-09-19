#silver 1
import sys

def solve(N):
    
    ans = []
    
    for i in range(N):
        score1, score2 = map(int, sys.stdin.readline().split())
        ans.append([score1, score2])
    ans.sort()
    
    select = ans[0]
    count = 1
    highest = select[1] # 면접 최고 순위

    for index in range(1, len(ans)):
        now = ans[index]
        # 면접 순위가 더 높을 경우 선발 
        if now[1] < highest: 
            count+=1
            highest = now[1]
    return count

if __name__ == "__main__":
    
    time = int(input())
    while time:
        N = int(input())
        print(solve(N))
        time -= 1