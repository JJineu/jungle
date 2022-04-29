#x보다 작은 수/반복문
from sys import stdin
N, X = map(int, stdin.readline().split())
s = list(map(int, stdin.readline().split()))

for i in s:
    if i < X:
        print(i, end=" ")