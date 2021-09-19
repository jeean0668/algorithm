

if __name__ == "__main__":
    N = int(input())
    array = []
    for i in range(N):
        array.append(int(input()))
    array.sort()
    
    count = 0
    for index in range(1, N+1):
        count += abs((index) - array[index-1])
    
    print(count)