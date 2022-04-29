# https://www.acmicpc.net/problem/10828
# 스택
# 자료구조

from sys import stdin 
input = stdin.readline

n = int(input())
q = []

for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'push':
        q.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
