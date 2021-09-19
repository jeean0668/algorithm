import sys

string = input()

start = 0
N = len(string)
stack = []

while start < N:
    
    stack.append(string[start])
    if len(stack) >= 4:
        fourth = stack.pop()
        three = stack.pop()
        two = stack.pop()
        one = stack.pop()
        if fourth == 'P' and three == 'A' and two =='P' and one == 'P':
            stack.append('P')
        else:
            stack.append(one)
            stack.append(two)
            stack.append(three)
            stack.append(fourth)
    start += 1
            
if len(stack) == 1 and stack[0] == 'P':
    print('PPAP')
else:
    print('NP')