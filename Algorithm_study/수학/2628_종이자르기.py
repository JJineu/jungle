#종이자르기/수학

from sys import stdin 
input = stdin.readline

col, row = map(int, input().split())

n = int(input())

col_li = [0,col]
row_li = [0,row]

cut_list = [list(map(int, input().split())) for _ in range(n)]
for i, cut in cut_list:
    if i == 0:
        row_li.append(cut)
    else:
        col_li.append(cut)

col_li.sort()
row_li.sort()

mul = 0
for i in range(1,len(col_li)):
    for j in range(1,len(row_li)):
        width = col_li[i]-col_li[i-1]
        height = row_li[j]-row_li[j-1]
        mul = max(mul, width*height)

print(mul)