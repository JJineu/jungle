# https://www.acmicpc.net/problem/12852

# bfs

# from collections import deque
# from sys import stdin
# input = stdin.readline

# def bfs(node, dp):
#     q = deque()
#     q.append((node, dp))
#     while q:
#         node, dp = q.popleft()
#         for n in [node+1, node*2, node*3]:
#             if n <= N and check[n] == 0:
#                 if n == N:
#                     return check[node]+1, dp+[n]
#                 q.append((n, dp+[n]))
#                 check[n] = check[node]+1

# N = int(input())
# if N == 1:
#     print(0)
#     print(1)
# else:
#     check = [0]*(N+1)
#     cnt, dp = bfs(1, [1])
#     print(cnt)
#     print(*dp[::-1])


# # 민우

# from collections import deque
# from sys import stdin
# input = stdin.readline
# def bfs():
#     while q:
#         x, ans = q.popleft()

#         if x == 1:
#             return ans

#         if not visited[x]:
#             visited[x] = True
#             if x % 3 == 0:
#                 q.append((x//3, ans+[x//3]))
#             if x % 2 == 0:
#                 q.append((x//2, ans+[x//2]))
#             q.append((x-1, ans+[x-1]))
# N = int(input())
# q = deque()
# q.append((N, [N]))
# visited = [False] * (N+1)
# answer = bfs()
# print(len(answer) - 1)
# print(*answer)


# dp

from sys import stdin
input = stdin.readline

n=int(input())
d=[0]*(n+1)     # 최솟값
pre=[0]*(n+1)   # 경로리스트

for i in range(2,n+1):
    # f(x-1)+1
    d[i]=d[i-1]+1
    pre[i]=i-1
    # f(x//2)+1
    if(i%2==0 and d[i]>d[i//2]+1):
        d[i]=d[i//2]+1
        pre[i]=i//2
    # f(x//3)+1
    if(i%3==0 and d[i]>d[i//3]+1):
        d[i]=d[i//3]+1
        pre[i]=i//3
print(d[n])

cur=n
while 1:
    print(cur, end=' ')
    if cur==1:
        break
    cur=pre[cur]

