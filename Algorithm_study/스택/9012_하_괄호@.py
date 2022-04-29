# https://www.acmicpc.net/problem/9012
# 괄호

from sys import stdin 
input = stdin.readline

t = int(input())

for _ in range(t):
    ps = input()
    count = 0   # 지표를 만들 것
    for i in ps:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        if count < 0: break

    if count == 0:
        print("YES")
    else:
        print("NO")