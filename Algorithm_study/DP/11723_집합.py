# https://www.acmicpc.net/problem/11723

from sys import stdin
input = stdin.readline

m = int(input())
bit = 0
for _ in range(m):
    cmd = input().split()
    if cmd[0] == 'all':
        bit = (1<<20)-1
    elif cmd[0] == 'empty':
        bit = 0
    else:
        op = cmd[0]
        num = int(cmd[1])-1

        if op == 'add':
            bit |= (1<<num) # 0100 | 1000 = 1100
        elif op == 'remove':
            bit &= ~(1<<num)    # 1000 & 0111 = 0000 // 0000 & 0111 = 0000
        elif op == 'check':
            if bit & (1<<num) == 0:
                print(0)
            else:
                print(1)
        elif op == 'toggle':
            bit = bit^(1<<num)  # 1 1 이면 0이고, 0 1 이면 1 대입된다.

