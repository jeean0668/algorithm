import sys
from string import ascii_lowercase
from collections import defaultdict
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())


words = [input().split() for _ in range(n)]
if m<=5:
    print(0)
    sys.exit()

cnt = m - 5
chars = ascii_lowercase
remove = 'antic'
visited = [False] * 26

chars_comb = combinations(chars, cnt)

