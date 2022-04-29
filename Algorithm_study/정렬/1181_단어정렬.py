#단어정렬/정렬
from sys import stdin

N = int(stdin.readline())
s = []
for _ in range(N):
    s.append(stdin.readline())

s = set(s)
s = sorted(s)
s = sorted(s, key=len)
for i in s:
    print(i, end="")
