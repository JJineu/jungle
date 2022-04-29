# https://www.acmicpc.net/problem/18258
# 큐2

from collections import deque
from sys import stdin 
input = stdin.readline

n = int(input())
q = deque()

for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'push':
        q.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(q) != 0:
            print(q.popleft())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if len(q) != 0:
            print(q[0])
        else:
            print(-1)
    else:
        if len(q) != 0:
            print(q[-1])
        else:
            print(-1)  