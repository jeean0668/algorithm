# silver 3


if __name__ == "__main__":
    
    N, L = map(int, input().split())
    pos = list(map(int, input().split()))
    pos.sort()
    
    count = 0
    now = 0
    for i in pos:
        if i < now:
            continue
        else:
            now = i + (L - 0.5)
            count += 1
    print(count)
            
      
        
            
