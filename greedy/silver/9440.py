# silver 4

def solve(case):
    N = case[0]
    
    numbers = sorted(case[1:])
    zeros = numbers.count(0)
    if zeros == 1:
        temp = numbers[0]
        numbers[0] = numbers[1]
        numbers[1] = numbers[2]
        numbers[2] = temp
    elif zeros > 1:
        
        numbers_min1 = numbers[zeros]
        numbers_min2 = numbers[zeros+1]
        numbers[zeros] = numbers[0]
        numbers[zeros+1] = numbers[1]
        numbers[0] = numbers_min1
        numbers[1] = numbers_min2
   
    result = 0
    if N % 2 == 0:
        left_max_digit = int(N/2) - 1
        right_max_digit = int(N/2) - 1
        index = 0
        for i in range(left_max_digit, -1, -1):
            result += (10 ** i) * numbers[index]
            result += (10 ** i) * numbers[index+1]
            index += 2
    elif N % 2 == 1:
        left_max_digit = int(N/2) - 1
        right_max_digit = int(N/2) - 1
        index = 1
        result += (10 ** (left_max_digit + 1)) * numbers[0]
        for i in range(right_max_digit, -1, -1):
            
            
            result += (10 ** i) * numbers[index]
            result += (10 ** left_max_digit) * numbers[index+1]
            
            left_max_digit -= 1
        
            index += 2 
    print(result)
           
if __name__ == "__main__":
    
    while True :
        case = list(map(int, input().split()))
        if case == [0]:
            break
        solve(case)
        