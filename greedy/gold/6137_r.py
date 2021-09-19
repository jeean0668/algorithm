N = int(input())
arr = [input() for _ in range(N)]

start = 0
end = N-1

result = []

while start <= end:
    if arr[start] < arr[end]:
        result.append(arr[start])
        start += 1
    elif arr[start] > arr[end]:
        result.append(arr[end])
        end -= 1
    else:
        next_start = start
        next_end = end
        flag = True
        while arr[next_end] == arr[next_start]:
            if next_end >0:
                next_end -= 1
            if next_start < N:
                next_start += 1
            if arr[next_start] < arr[next_end]:
                flag = True
            elif arr[next_start] > arr[next_end]:
                flag = False

        if flag:
            result.append(arr[start])
            start += 1
        else:
            result.append(arr[end])
            end -= 1




lens = len(result)

if lens <= 80:
    print(''.join(result))
else:
    for ind in range(lens//80+1):
        if ind == lens//80:
            print(''.join(result[ind*80:]))
        else:
            print(''.join(result[ind*80:(ind+1)*80]))