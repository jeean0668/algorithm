import sys

N = int(input())
for i in range(N):
    S = input()
    T = input()
    
    S_zero_T_one = 0
    S_one_T_zero = 0
    S_q_T_1 = 0
    S_q_T_0 = 0
    for j in range(len(S)):
        if S[j] != T[j]:
            if S[j] == '?' and T[j] == '0':
                S_q_T_0 += 1
            elif S[j] == '?' and T[j] == '1':
                S_q_T_1 += 1
            elif S[j] =='0' and T[j] == '1':
                S_zero_T_one += 1
            elif S[j] == '1' and T[j] == '0':
                S_one_T_zero += 1
    result = 0
    if S_one_T_zero > S_zero_T_one + S_q_T_1:
        print("Case {}: {}".format(i+1, -1))
        continue
        
    swap = min([S_one_T_zero, S_zero_T_one])
    S_one_T_zero -= swap
    S_zero_T_one -= swap
    result += swap
    
    if S_one_T_zero > 0:
        swap2 = min([S_one_T_zero, S_q_T_1])
        S_q_T_1 -= swap2
        
        result += swap2 * 2 # {?, 1} -> {0, 1} -> {1, 0}과 자리바꿈->2번
        result += S_q_T_1 # 남아있는 ? 모두 변환
        result += S_q_T_0 
        
    else:
        result += S_q_T_1
        result += S_q_T_0
        result += S_zero_T_one
        
    print("Case {}: {}".format(i+1, result))