# https://www.acmicpc.net/problem/5397

# from sys import stdin
# input = stdin.readline
t = int(input())

for _ in range(t):
    left = []
    right = []
    pwd = input()

    for x in pwd:
        if x == ">":    # 오른쪽을 왼쪽에 붙임(오른쪽 스택 필요)
            if right:
                left.append(right.pop()) 
        elif x=="<":    # 왼쪽을 오른쪽에 붙임(왼쪽 스택 필요)
            if left:
                right.append(left.pop())
        elif x=="-":    # 왼쪽 스택 지움(왼쪽 스택 필요)
            if left:
                left.pop()
        else:
            left.append(x)

    print("".join(left)+"".join(reversed(right)))