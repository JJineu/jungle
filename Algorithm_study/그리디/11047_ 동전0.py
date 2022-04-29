# https://www.acmicpc.net/problem/11047

from sys import stdin 
input = stdin.readline

n, k = map(int, input().split())
coins = list(int(input()) for _ in range(n))

res = 0
for coin in coins[::-1]:
    res += k//coin
    k %= coin
print(res)