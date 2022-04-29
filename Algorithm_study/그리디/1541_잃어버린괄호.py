# https://www.acmicpc.net/problem/1541

from sys import stdin
input = stdin.readline

tmp = input().rstrip().split('-')

res = []
for i in tmp:
    sum = 0
    s = i.split('+')
    for j in s:
        sum += int(j)
    res.append(sum)

num = res[0]
for i in range(1, len(res)):
    num -= res[i]
print(num)