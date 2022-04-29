# https://www.acmicpc.net/problem/9095

# t = int(input())
# s = [1,2,3]

# count = 0

# def func(n):
#     global count
    
#     for j in s:
#         if j + n <= n:
#             func(n - j)  

#     if n == 0:
#         count += 1
#         return
        
# for _ in range(t):
#     k = int(input())
#     func(k)



# # 9095 윤우
# import sys
# input = sys.stdin.readline
# T = int(input())

# for _ in range(T):
#     n = int(input())
#     ans = [0]
#     def solve(remain=n):
#         if remain < 0:
#             return
#         if remain == 0:
#             ans[0] += 1
#             return
#         for i in range(1, 4):
#             if remain-i<0: continue
#             solve(remain-i)

#     solve()
#     print(ans[0])

# 코치님이 코멘트 주신 내용으로 다시 풀어봤습니다.
# T = int(input())

# for _ in range(T):
#     n = int(input())

#     def solve(remain=n):
#         if remain < 0:
#             return 0
#         if remain == 0:
#             return 1

#         return solve(remain-1) + solve(remain-2) + solve(remain-3)

#     print(solve()) 


from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    d = [0]*(11)
    d[1] = 1
    d[2] = 2
    d[3] = 4
    
    for i in range(4, n+1):
        d[i] = d[i-1] + d[i-2] + d[i-3]
    
    print(d[n])