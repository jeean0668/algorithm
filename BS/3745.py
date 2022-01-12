import sys
import bisect
input = sys.stdin.readline

try:
    while input():
        array = list(map(int, input().split()))

        tmp = [array[0]]
        index = [] 
        for i in range(len(array)):
            if tmp[-1] < array[i]:
                tmp.append(array[i])
                index.append(len(tmp))
            else:
                idx = bisect.bisect_left(tmp, array[i])
                tmp[idx] = array[i]
                index.append(idx+1)

        print(len(tmp))
except:sys.exit()