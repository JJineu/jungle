# https://www.acmicpc.net/problem/9461

from sys import stdin
input = stdin.readline

d = [0,1,1,1,2,2,3,4,5,7,9] + [0]*90
def P(n):
    if d[n]!=0:
        return d[n]
    d[n] = P(n-1)+P(n-5)
    return d[n]

t = int(input())
for _ in range(t):
    print(P(int(input())))
