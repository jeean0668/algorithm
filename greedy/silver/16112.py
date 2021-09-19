import sys


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    quest = list(map(int, sys.stdin.readline().split()))
    quest.sort() # 오름차순 정렬
    count = 0
    j = 0
    for i in range(N):
        # i가 1일때, n=k일때 예외케이스
       
        count += quest[i] * j
        if j < K: 
            j += 1 # 
    print(count)