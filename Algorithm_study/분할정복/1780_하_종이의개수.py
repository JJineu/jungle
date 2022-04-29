# https://www.acmicpc.net/problem/1780
# 종이의 개수

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

minus = 0; zero = 0; plus = 0
def recursion(n,x,y):
    global minus
    global zero
    global plus
    check = paper[x][y]
    size = n//3
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check != paper[i][j]:
                recursion(size,x,y)
                recursion(size,x,y+size)
                recursion(size,x,y+2*size)

                recursion(size,x+size,y)
                recursion(size,x+size,y+size)
                recursion(size,x+size,y+2*size)

                recursion(size,x+2*size,y)
                recursion(size,x+2*size,y+size)
                recursion(size,x+2*size,y+2*size)
                return

    if check == -1:
        minus += 1
    elif check == 0:
        zero += 1
    elif check == 1:
        plus += 1

recursion(n,0,0)
print(minus)
print(zero)
print(plus)
