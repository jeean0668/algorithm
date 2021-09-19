import sys

if __name__ == "__main__":
    N = int(input())
    length = list(map(int, sys.stdin.readline().split()))
    cities = list(map(int, sys.stdin.readline().split()))
    
    index = 0
    price = 0
    min_price = sys.maxsize
    
    for city_index in range(len(cities) - 1):
        citie = cities[city_index]
        if citie < min_price:
            min_price = citie
            
        price += min_price * length[index]
        index += 1
    
    print(price)
        