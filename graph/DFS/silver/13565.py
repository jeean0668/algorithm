import sys

dy = [1, 0, 0, -1]
dx = [0, 1, -1, 0]
input = sys.stdin.readline
M, N = map(int, input().split()) # M : 세로길이, N : 가로길이
material_map = [[] for _ in range(M)]
visited = [[False for _ in range(N)] for _ in range(M)]

for i in range(M):
    row = input().strip()
    row_list = [int(char) for char in row]
    for ele in row_list:
        material_map[i].append(ele)
#print(material_map)
def dfs(y, x):
    stack = [[y, x]]
    while stack:
        node = stack.pop()
        y, x = node[0], node[1]
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            if 0 <= yy < M and 0 <= xx < N:
                if not visited[yy][xx] and material_map[yy][xx] == 0:
                    visited[yy][xx] = True
                    stack.append([yy, xx])
        if y == 0:
            return True
    return False
        
flag = False
for col_index in range(len(material_map[M-1])):
    now = material_map[M-1][col_index]
    if now == 0 and not visited[M-1][col_index]:
        #print("now : {}, y pos : {}, x_pos : {}" . format(now, col_index, M-1))
        if dfs(M-1, col_index):
            flag = True
print("YES") if flag else print("NO")

