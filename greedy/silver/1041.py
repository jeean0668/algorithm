# silver 1


def solve(N, num):
    if N == 1:
        num.sort()
        return num[0]+num[1]+num[2]+num[3]+num[4]
    num[0] = min([num[0], num[5]])
    num[1] = min([num[1], num[4]])
    num[2] = min([num[2], num[3]])
   
    num = num[:3]
    num.sort()
                  
    third = 4 * (num[0] + num[1] + num[2])
    two = (4 * (N-2) + 4 * (N-1)) * (num[0] + num[1])
    one = (4 * ((N-2) * (N-1)) + (N-2) ** 2) * (num[0])
    return third + two + one

if __name__ == "__main__":
    N = int(input())
    num = list(map(int, input().split()))
    print(solve(N, num))
