# https://www.acmicpc.net/problem/3190
# 뱀

from sys import stdin
from collections import deque

q = deque([])
n = int(stdin.readline())
k = int(stdin.readline())
apple = [list(map(int, stdin.readline().split()) for _ in range(n))]
l = int(stdin.readline())
snake = q.append(list(map(str, stdin.readline().split()) for _ in range(l)))

rotate_x = [0,1,0,-1]
rotate_y = [1,0,-1,0]
