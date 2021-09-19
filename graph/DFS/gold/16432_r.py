import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
graph = []
visited = [[False for _ in range(10)] for _ in range(n+1)]
cakes = []
for day in range(n):
    m, *temp = list(map(int, input().split()))
    graph.append(temp)


def dfs(day, yesterday):
    
    if day == n:
        for c in cakes:
            print(c)
        exit()
    for cake in graph[day]:
       
        #print("cake : {}, yesterday : {}".format(cake, yesterday))
        
        if cake != yesterday and not visited[day][cake-1]:
            
            visited[day][cake-1] = True
            cakes.append(cake)
            dfs(day + 1, cake)
dfs(0, 0)
print(-1)
