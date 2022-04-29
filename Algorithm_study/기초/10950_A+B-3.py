#A+B-3/반복문
from sys import stdin
N = int(stdin.readline())
for _ in range(N):
    A, B = map(int, stdin.readline().split())
    print(A+B)
