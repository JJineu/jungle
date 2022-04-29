# https://www.acmicpc.net/problem/1904

#dp_b
# 피보나치

from sys import stdin 
input = stdin.readline

n = int(input())

d = [0]*1000001
d[1] = 1
d[2] = 2

for i in range(3, n+1):
    d[i] = (d[i-1] + d[i-2])%15746
print(d[n])