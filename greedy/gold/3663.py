import sys

input = sys.stdin.readline

N = int(input())

while N > 0:
    case = list(input().strip())
    # A가 아닌 것들의 인덱스를 저장한다.
    
    non_A_index = []
    length = len(case)
    for i in range(length):
        s = case[i]
        if s != 'A':
            non_A_index.append(i)
            
    moves = sys.maxsize
    result = 0
    
    for i in range(length):
        
        j = 0
        if case[j] == 'A':
            for j in range(i+1, length):
                right = i*2 + length - j
                left = i + (length - j) * 2
                temp = min(left, right)
                moves = min(temp, moves)
    
    for i in range(length):
        s = case[i]
        result += min(ord(s)-ord('A'), ord('Z') - ord(s) + 1)
    print(result + moves)
    N -= 1