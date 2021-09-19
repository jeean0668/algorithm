# silver 1
# PriorityQueue를 사용하면 쉽게 정렬 가능 
from queue import PriorityQueue


def solve(N, M):
    array = list(map(int, input().split()))
    que = PriorityQueue()
    for a in array:
        que.put(a) # priority que에 삽입 -> 작은 원소가 top 
    
    
    for m in range(M):
        one = que.get()
        two = que.get()
        result = one + two
        que.put(result)
        que.put(result)
    
    result = 0
    while not que.empty():
        result += que.get()
    
    print(result)


if __name__ == "__main__":
    a = list(map(int, input().split()))
    N, M = a[0], a[1]
    
    solve(N, M)
    
