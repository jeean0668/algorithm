import sys

array = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
result = ''

def classified(value):
    if value >= 90:
        return 'A'
    elif 80 <= value < 90:
        return 'B'
    elif 70 <= value < 80:
        return 'C'
    elif 50 <= value < 70:
        return 'D'
    elif value < 50:
        return 'F'
columns = []
for i in range(5):
    column = [scores[i] for scores in array]
    columns.append(column)
def onlytop(arr, value):
    cnt = 0
    for a in arr:
        if a >= value:
            cnt += 1
    if cnt > 1:
        return False
    else:
        return True

def onlybottom(arr, value):
    cnt = 0
    for a in arr:
        if a <= value:
            cnt += 1
    if cnt > 1:
        return False
    else:
        return True
print(column)
for i in range(len(column)):
    col = column[i]
    exe = False
    cnt = 0
    for j in range(len(col)):
        if i == j and (onlytop(col, col[i]) or onlybottom(col, col[i])):
            exe = True
            continue
        cnt += col[j]
    average = 0
    if exe :
        average = cnt // (len(col) - 1)
    else:
        average = cnt // len(col)
    result += classified(average)
print(result)
    