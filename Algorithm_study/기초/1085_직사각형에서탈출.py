#직사각형에서 탈출/조건문
from sys import stdin
x,y,w,h = map(int, stdin.readline().split())

print(min(x,y,w-x,h-y))


# 빗변의 길이
# print(((a-c)**2 + (b-d)**2)**0.5)