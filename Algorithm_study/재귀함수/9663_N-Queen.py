#N-Queen/재귀함수
# from re import I
# from sys import stdin
# # from collections import Counter

# n = int(stdin.readline())

# # N개의 row, 각 1개씩 놓고 시작
# # 첫번째 놓았을때 가로세로, 대각선2개 겹치는 promising함수

# # i번째 row의 col의 위치 반환
# col = [0]*n

# # 대각선은 col[i]-col[k] == i-k  or col[i]-col[k] == k-i

# count = 0
# def queen(i, col):
#     n=len(col)
#     if (promising(i, col)):
#         if i==(n-1):
#             print(col)

#         else:
#             for j in range(n):
#                 col[i] =j
#                 queen(i+1, col) # i+1행 j열(1-n) 탐색

# def promising(i,col):
#     k = 0
#     flag = True
#     while (k<i & flag):
#         if col[i] == col[k] or abs(col[i]-col[k])==i-k:
#             flag = False
#         k += 1
#     return flag

# queen(0,col)



# #해인
# import sys

# def solution(n: int):
#     return search([0] * n, 0)


def search(queen: list, row: int):
    n = len(queen)
    count = 0

    if n == row:
        return 1
    
    for col in range(n):
        queen[row] = col
        if check(queen, row):
            count += search(queen, row + 1)
            
    return count


def check(queen: list, row: int):
    for i in range(row):
        if queen[i] == queen[row] or abs(queen[i] - queen[row]) == row - i:
            return False

    return True

# n = int(sys.stdin.readline())
# print(solution(n))


#민우

# def dfs(board, n, row): #보드의 한 행 할당, 길이, 행(행값 대입하면 열 좌표 나옴)
#     count = 0
#     if n == row: #행 0~n-1까지 재귀후에 row가 n이 되면 끝남
#         return 1

#     for col in range(n): #전 행에 대한 열의 값을 구할건데
#         board[row] = col #현재 행에 열의 값 0~n-1까지 대입해보는데,
#         for r in range(row+1): #현재 row까지, 뒤의 조건에 대해 확인
#             if board[r] == board[row] or abs(board[r]-board[row]) == row-r:
#                 #현재행에 대한 열의 값과 이전의 열의값들 비교,
#                 continue 
#             count += dfs(board, n, row+1) #겹치는 부분이 없으면 다시 재귀
            
#         return count
    

# n = int(input())
# print(dfs([0]*n, n, 0))

#윤우
#각 조건에 대한 배열식 구함.


#책
# n= int(input())
# pos=[0]*8
# flag_a = [False]*n
# flag_b = [False]*(2*n-1)
# flag_c = [False]*(2*n-1)

# def put() ->None:
#     for i in range(n):
#         print(pos, end=" ")
#     print()

# def set(i:int)->None:
#     for j in range(n):
#         if(not flag_a[j] and not flag_b[i+j] and not flag_c[i-j+n-1]):
#             pos[i]=j
#             if i == n-1: 
#                 put()
#             else:
#                 flag_a[j] = flag_b[i+j] = flag_c[i-j+n-1] = True
#                 set(i+1)
#                 flag_a[j] = flag_b[i+j] = flag_c[i-j+n-1] = False

# set(0)

# 연습

# 행, 대각선up, 대각선down
# 재귀 카운트
# 초기화
from sys import stdin

N = int(stdin.readline())
row = [False]*N
up = [False]*(2*N-1)
down = [False]*(2*N-1)
pos = [0]*N

def queen(i: int):
    count = 0
    for j in range(N):
        if (not row[j] and not up[i+j] and not down [i-j+N-1]):
            pos[i]=j
            if i == N-1:
                return 1

            else:
                row[j] = up[i+j] = down [i-j+N-1] = True
                put(row)
                count += queen(i+1)
                row[j] = up[i+j] = down [i-j+N-1] = False

            return count

def put():
    count +=1
    
queen(0)