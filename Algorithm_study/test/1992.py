# https://www.acmicpc.net/problem/1992

from sys import stdin 
input = stdin.readline

n = int(input())
matrix = [list(map(int, input().strip())) for _ in range(n)]
res = []

def cycle(n, r, c):
    check = matrix[r][c]

    for i in range(r,r+n):
        for j in range(c,c+n):
            if check != matrix[i][j]:
                res.append('(')
                cycle(n//2, r,c)
                cycle(n//2, r,c+(n//2))
                cycle(n//2, r+(n//2),c)
                cycle(n//2, r+(n//2),c+(n//2))
                res.append(')')
                return
 
    if check == 0:
        res.append(0)
    else:
        res.append(1)

cycle(n,0,0)

print(''.join(map(str, res)))
