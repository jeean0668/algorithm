import sys
input = sys.stdin.readline
"""
hashing 문제였는데, 익숙하지 않아서 결국 답을 봤다.
1. string에 대응할 소수 리스트 primes를 만든다.
2. str2에 대해서 hashing을 진행하는데, 길이가 다르고 hashing 값은 같은 경우가
있을 수 있으므로, hash_list를 선언하여 이중 hashing을 해주었다.
-> hash_list[해쉬 값1] = (해쉬값2, 문자열 길이)
3. str3에 대해서 hashing을 진행한다. 이때 hashing_list에 저장된
hash값과 같은 결과가 있을 경우 그 길이를 저장한다. 
-> hash_list[hash1][k] == (hash2, length) -> 길이 저장.
"""
str1 = input().rstrip()
str2 = input().rstrip()
mod = 999979
ans = 0

primes = {}

idx = 0
for i in range(2,1000):
    flag = 1
    for j in range(2,int(i**0.5)):
        if i % j == 0:
            flag = 0
            break
    if flag == 1:
        primes[idx] = i
        idx += 1

hash_list = [[] for _ in range(mod)]
    
for i in range(len(str2)):
    hash1 = 1
    hash2 = 1
    for j in range(i,len(str2)):
        length = j - i + 1
        chr_idx = ord(str2[j]) - ord('a')
        num = primes[chr_idx]
        hash1 *= num
        hash1 %= mod
        hash2 *= primes[chr_idx + 26]
        hash2 %= mod
        hash_list[hash1].append((hash2, length))

for i in range(len(str1)):
    hash1 = 1
    hash2 = 1
    for j in range(i, len(str1)):
        length = j - i + 1
        chr_idx = ord(str1[j]) - ord('a')
        num = primes[chr_idx]
        hash1 *= num
        hash1 %= mod
        hash2 *= primes[chr_idx + 26]
        hash2 %= mod
        
        for k in range(len(hash_list[hash1])):
            if(hash_list[hash1][k] == (hash2, length)):
                ans = max(ans, length)

print(ans)