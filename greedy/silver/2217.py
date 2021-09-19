# silver 4



    
def solve(N):
    
    value = []
    ropes = []
    for i in range(N):
        ropes.append(int(input()))
    # ropes 정렬
    ropes.sort(reverse=True)
    
    for k in range(N):
        value.append(ropes[k] * (k+1))
    
    print(max(value))
            
    
if __name__ == "__main__":
    N = int(input())
    solve(N)