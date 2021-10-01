# -*- coding: utf-8 -*- 
"""
그냥 생각하지 못했다. BFS문제만 100문제는 풀어봐야겠다는 생각이 든다.
자리를 바꾼 모든 값들을 queue에만 넣어주면 되는 문제였는데... 아쉽다.
"""
import sys
input = sys.stdin.readline
import copy

N, K = input().split()
M = len(N) #전체 자릿수
K = int(K)
#전체 숫자 범위와 모든 깊이 범위에 대해 방문 여부를 나타내는 배열
cache =[[False for i in range(11)] for i in range(1000001)]
#BFS 큐
q=[]
q.append([[ch for ch in N],0]) # 시작 숫자와 깊이를 넣어준다.
cache[int(N)][0]=True

def swap(N, idx1, idx2):
    
    a = N[idx1]
    N[idx1]
    N[idx1] = N[idx2]
    N[idx2] = a

answer = -1
while q:
    n, depth = q.pop(0)

    if depth == K: #깊이가 K면 비교해서 최대값
        answer = max(answer, int(''.join(n)))
        continue
       
    #M 자리에서 두자리를 선택한다.
    for i in range(M): 
        for j in range(i+1,M):
            if i ==0 and n[j] =='0': 
            # 바꾸는 인덱스가 맨 앞이고 바꿔야되는 값이 '0'이면 바꾸지 않는다.
            # 첫째자리가 0이 되기 때문에
                continue

            swap(n, i, j) #자리를 바꾸고
            n_int = int(''.join(n)) #정수형으로 바꾼뒤
            if not cache[n_int][depth+1]: #해당 값과 깊이를 방문하지 않았으면
                cache[n_int][depth+1] = True #방문하고
                q.append([n.copy(), depth+1]) # q에 집어넣어준다.
            swap(n, i, j) # 자리를 다시 바꿔준다.

print(answer)