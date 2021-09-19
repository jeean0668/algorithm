
money = int(input())

def solution(money):
    
    result = 0
    money = 1000-money
   
    if money >=500:
        
        result += int(money/500)
        money -= 500 * int(money/500)
       
    if money >=100:
        result += int(money/100)
        money -= 100 * int(money/100)
        
    if money >= 50:
        result += int(money/50)
        money -= 50 * int(money/50)
       
    if money >= 10 :
        result += int(money/10)
        money -= 10 * int(money/10)
        
    if money >= 5:
        result += int(money/5)
        money -= 5 * int(money/5)
    if money >= 1:
        result += int(money)
        money -= int(money)
    result += money 
    return result 

print(solution(money))