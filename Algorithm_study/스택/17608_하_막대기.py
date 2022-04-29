# https://www.acmicpc.net/problem/17608
# 막대기

# 중간 막대기가 크면 그다음 막대기가 보이지 않음

from sys import stdin 
input = stdin.readline

n = int(input())
top_li = list(int(input()) for _ in range(n))

count = 1
std = top_li.pop()

for i in top_li[::-1]:
    if i > std:
        count += 1
        std = i

print(count)