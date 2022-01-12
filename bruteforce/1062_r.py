import sys
from itertools import combinations
input = sys.stdin.readline

n, k = map(int, input().split())

# k가 5 미만이면 0 출력
if k < 5 :
    print(0)
    sys.exit()
else:
    k -= 5
    possible = {'a', 'n', 't', 'i', 'c'}
    input_chars = []
    # possible을 제외한 알파벳을 alpha에 bit로 저장
    alpha = {ky : v for v, ky in enumerate(
        set(map(chr, range(ord('a'), ord('z') + 1))) - possible)}
    cnt = 0
    for _ in range(n):
        tmp = 0
        for c in set(input().rstrip()) - possible:
            tmp |= (1<<alpha[c])
        print(tmp)
        # 입력받은 문장에서 {'a', 'n', 't', 'i', 'c'}를 빼고 bit로 바꿔 저장
        input_chars.append(tmp)
    power_by_2 = (2 ** i for i in range(21))
    # k개의 조합들에 대해서 모두 검사해본다.
    for comb in combinations(power_by_2, k):
        test = sum(comb)
        ct = 0
        for cb in input_chars:
            # 순회중인 단어를 만들수 있으면 ct + 1
            if test & cb == cb:
                print(test, cb)
                ct += 1
        cnt = max(cnt, ct)
    print(cnt)