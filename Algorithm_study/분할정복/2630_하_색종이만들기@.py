# https://www.acmicpc.net/problem/2630
# 색종이 만들기

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white = 0; blue = 0

def dfs(n, r, c):
    global white, blue
    check = paper[r][c]

    for i in range(r, r+n):
        for j in range(c, c+n): 
            if check != paper[i][j]:
                dfs(n//2, r, c)
                dfs(n//2, r, c+n//2)
                dfs(n//2, r+n//2, c)
                dfs(n//2, r+n//2, c+n//2)
                return

    if check == 0:
        white += 1
    elif check == 1:
        blue += 1

dfs(n, 0, 0)
print(white)
print(blue)
