import sys
input = sys.stdin.readline

l, c = map(int, input().split())
char = list(input().split())
char.sort()
def func(index, cnt, arr):
    if cnt == l:
        vowels = 0
        Consonant = 0
        for a in arr:
            if a in ['a', 'e', 'i', 'o', 'u']: vowels += 1
            else: Consonant += 1   
        if vowels >= 1 and Consonant >= 2:
            print(arr)
            return
    if index == c:
        return
    
    func(index + 1, cnt + 1, arr + char[index])
    func(index + 1, cnt, arr)
            
func(1, 1, char[0])
func(1, 0, '')

