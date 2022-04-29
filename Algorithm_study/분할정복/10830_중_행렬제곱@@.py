# https://www.acmicpc.net/problem/10830
# 행렬 제곱

from sys import stdin 
input = stdin.readline

n, b = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(n)]

def multi(A,B):
    n = len(A)
    new_M = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            e = 0           
            for k in range(n):
                e += A[i][k]*B[k][j]
            new_M[i][j] = e % 1000

    return new_M


def res(M, b):
    n = len(M)
    # 입력된 행렬 A의 원소 중에 1000이 있을 수도 있기 때문, 나머지 연산을 수행 후 리턴해줘야 한다.
    if b == 1:
        for x in range(n):
            for y in range(n):
                M[x][y] %= 1000
        return M

    temp = res(M,b//2)
    if b%2:
        return multi(multi(temp,temp),M)
    else:
        return multi(temp, temp)

result = res(matrix, b)
for i in result:
    print(*i)

