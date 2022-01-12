n = int(input())

def possible(value):
    value_str = str(value)
    value_list = list(value_str)
    value_list_int = list(map(int, value_list))
    
    if len(value_list_int) == 1:
        return True
    gap = value_list_int[1] - value_list_int[0]
    for i in range(1, len(value_list_int)):
        if (value_list_int[i] - value_list_int[i-1]) != gap:
            return False
    return True
cnt = 0
for i in range(1, n+1):
    if possible(i):
        cnt += 1
print(cnt)