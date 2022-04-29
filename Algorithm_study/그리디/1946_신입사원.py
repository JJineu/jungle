# https://www.acmicpc.net/problem/1946

# from sys import stdin
# input = stdin.readline

# t = int(input())
# for _ in range(t):
#     n = int(input())   
#     A = []
#     for i in range(n):
#         paper, interview = map(int, input().split())
#         A.append((paper, interview))
    
#     A.sort()
#     i_std = A[0][1]
#     cnt = 1
    
#     for i in range(1,n):
#         if i_std > A[i][1]: # 숫자가 작다 = 순위가 높다
#             cnt += 1
#             i_std = A[i][1]

#     print(cnt)
                

import sys
t = int(sys.stdin.readline())

def solve(n):
    score = [0] * (n + 1)
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        score[x] = y

    limit = score[1]
    cnt = 0
    for i in range(1, n + 1):
        if score[i] > limit:
            cnt += 1
            # n -= 1
        else:
            limit = score[i]
            # limit = min(limit, score[i])    # min(총인원수, 현재 면접순위)
    return n-cnt

for _ in range(t):
    print(solve(int(sys.stdin.readline())))